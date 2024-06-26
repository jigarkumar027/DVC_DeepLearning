from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="jigarkumar027",
    description="A small package for dvc ml pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jigarkumar027/dvc_ml",
    author_email="parmarjigarkumar147@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow==2.3.4",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3",
    ]
)