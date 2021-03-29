# Commune Bot

A friendly Twitter bot built with [Munibot](https://github.com/amercader/munibot) that tweets aerial pictures of France's [communes](https://en.wikipedia.org/wiki/Communes_of_France).

## Install and setup

Install it with pip:

```
pip install communebot_fr
```

And follow the instructions on [Munibot's documentation](https://github.com/amercader/munibot#usage) regarding configuration and setup.

This particular bot requires:

* An [IGN geoservices](https://geoservices.ign.fr/) key to access the WMS service, which you can obtain [here](https://geoservices.ign.fr/documentation/diffusion/formulaire-de-commande-geoservices.html)
* The backend SQLite database with communes data, which you can download from this repo (`data` folder)


Both these should be referenced in the `[profile:fr]` section of your `munibot.ini` file:

```
[profile:fr]
ign_key=CHANGE_ME
twitter_key=CHANGE_ME
twitter_secret=CHANGE_ME
db_path=/path/to/data/communes_fr.sqlite
```

### License

[MIT](/amercader/munibot/blob/master/LICENSE.txt)
