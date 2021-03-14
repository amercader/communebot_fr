import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="communebot_fr",
    version="0.0.1",
    author="Adrià Mercader",
    author_email="amercadero@gmail.com",
    description="A Twitter bot built with munibot that tweets aerial imagery pictures of France communes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amercader/communebot_fr",
    packages=setuptools.find_packages(),
    install_requires=["munibot", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "munibot_profiles": [
            "fr=communebot_fr.profile:CommuneBotFr",
        ],
    },
)
