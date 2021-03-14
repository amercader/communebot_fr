import requests
from munibot.profiles.base import BaseProfile
from munibot.config import config


class CommuneBotFr(BaseProfile):
    """
    A Munibot profile for tweeting images of French communes
    """

    # Mandatory properties

    """
    A unique identifier for the profile, that will be used when running the
    commands and on the configuration file.
    """
    id = "fr"

    """
    A longer description of the profile.
    """
    desc = "Communes de France (Orthophoto IGN)"

    # Mandatory hooks

    """
    Given a feature id, returns a tuple with the extent and the geometry of the
    the boundaries of the feature.

    The extent is a tuple containing (minx, miny, maxx, maxy). The geometry is a
    dict containing the geometry in GeoJSON format.
    """

    def get_boundaries(self, id_):

        cadastre_url = "https://apicarto.ign.fr/api/cadastre/commune"

        params = {"code_insee": id_}

        r = requests.get(cadastre_url, params=params)

        feature_collection = r.json()

        bbox = feature_collection["bbox"]

        extent = (
            bbox[0],
            bbox[2],
            bbox[1],
            bbox[3],
        )

        geom = feature_collection["features"][0]["geometry"]

        return (extent, geom)

    """
    Returns a base image for the given extent (minx, miny, maxx, maxy).

    The return value is a file-like object containing the raster image for the
    provided extent.
    """

    def get_base_image(self, extent):

        bbox = (extent[0], extent[2], extent[1], extent[3])

        bbox = self.extend_bbox(bbox)

        wms_url = "https://wxs.ign.fr/{}/geoportail/r/wms".format(
            config["profile:fr"]["ign_key"]
        )

        headers = {"User-Agent": "munibot-fr"}

        wms_options = {
            "url": wms_url,
            "layer": "ORTHOIMAGERY.ORTHOPHOTOS.BDORTHO",
            "version": "1.3.0",
            "crs": "EPSG:4258",
            "bbox": bbox,
            "format": "image/geotiff",
            "headers": headers,
        }

        img = self.get_wms_image(**wms_options)

        if img.info().get("Content-Type") == "application/xml":
            raise ValueError("Error retrieving WMS image: {}".format(img.read()))

        return img

    """
    Returns the text that needs to be included in the tweet for this particular
    feature.
    """

    def get_text(self, id_):

        raise NotImplementedError

    """
    Returns the id of the next feature that should be tweeted.

    This is used if the ``munibot tweet`` command is called withot providing
    an id.
    """

    def get_next_id(self):

        raise NotImplementedError

    # Optional hooks

    """
    Return a tuple with the longitude and latitude that should be associated
    with the tweet.

    The bot account should have location information on tweets activated.
    """

    def get_lon_lat(self, id_):

        return None, None

    """
    Function that will be called after sending the tweet, that will receive
    the feature and the status id of the tweet sent.
    """

    def after_tweet(self, id_, status_id):

        pass
