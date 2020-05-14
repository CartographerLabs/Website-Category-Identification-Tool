import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Website-Category-Identification-Tool",
    version="0.0.1",
    author="James Stevenson",
    author_email="hi@jamesstevenson.me",
    description="A Python script that can be provided with a JSON configuration to identify websites that fit a specific category or criteria.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user1342/Website-Category-Identification-Tool",
    packages=["Identifier"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Newspaper3k","tweepy","gensim","spacy","nltk","beautifulsoup4","requests"],
)