from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    README = file.read()

setup(
    name="molick",
    version="0.0.0",
    author="yourmoln",
    author_email="yourmoln@outlook.com",
    description="Hacker's exclusive library",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/molick-tech/molick", 
    project_urls={
                "Bug Report": "https://github.com/molick-tech/molick/issues/new"
            },
    packages=find_packages(),

    classifiers = [
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3',
    ]
)