import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()


__version__ ="0.0"
SRC_REPO ="ccnClassifier"
AUTHOR_USER_NAME = "DIKSHANT PATEL"
REPO_NAME = "Chicken-Disease-Classification-EndtoEnd-DLProject"
AUTHOR_EMAIL = "dikshantpatel2210@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    version= __version__,
    author_email=AUTHOR_EMAIL,
    description="A small python packages for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages= setuptools.find_packages(where="src")




)