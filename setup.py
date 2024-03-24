import setuptools

#setuptools is a Python library that facilitates packaging, distribution, and installation of Python projects. 
# It is commonly used to define metadata about Python packages and to manage dependencies.

with open("README.md","r",encoding = "utf-8") as f :
    long_description = f.read()
    
    #it's important to specify the encoding parameter, especially when dealing with text files. 
    # The encoding parameter specifies the character encoding used to interpret the contents of the file
    
    #specifying encoding="utf-8" when opening a file ensures that Python correctly interprets the characters in the file, 
    # especially when dealing with non-ASCII characters or multilingual content.
__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer-NLP-project"
AUTHOR_USER_NAME = "sibrikhanr98"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rmsifrikan6500@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for NLP app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", 
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
)