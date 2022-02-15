import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="heliumapipy",
    version="1.3",
    author="mkrasulin2020",
    author_email="mkrasulin2020@gmail.com",
    description="Unofficial api for Helium Explorer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikhailkrasulin/HeliumAPI-Python",
    project_urls={
        "Bug Tracker": "https://github.com/mikhailkrasulin/HeliumAPI-Python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)