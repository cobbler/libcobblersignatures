from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="libcobblersignatures",
    version="0.0.1",
    description="This library manages the operating system distribution signatures to enable cobbler to detect it "
    "correctly.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://cobbler.github.io/",
    author="Cobbler",
    author_email="cobbler.project@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="cobbler",
    packages=find_packages(exclude="tests"),
    python_requires=">=3",
    install_requires=["questionary"],
    extras_require={
        "lint": ["pylint"],
        "test": ["coverage", "pytest"],
        "docs": ["sphinx_rtd_theme"],
    },
    entry_points={
        "console_scripts": [
            "cobbler-manage-signatures=libcobblersignatures.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/cobbler/cobbler/issues",
        "Source": "https://github.com/cobbler/cobbler",
    },
)
