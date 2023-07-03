from setuptools import find_packages
from setuptools import setup

setup(
    name="backend",
    version="0.0.1",
    author="Simon Fong",
    author_email="simonfong6@gmail.com",
    description="A package.",
    long_description="A longer description.",
    long_description_content_type="text/markdown",
    url="https://github.com/simonfong6/template-python-flask",
    packages=find_packages(),
    install_requires=[
        'flask == 2.2.2',
        'pymongo == 3.10.1',
        'Faker == 4.1.2',
        'pytest == 6.0.1',
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
