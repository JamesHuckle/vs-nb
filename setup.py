from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='vs_nb',
    version='0.1.0',
    description='Converts .ipynb into .py and vice-versa',
    #single-file Python modules that aren’t part of a package
    py_modules=['vs_nb'],
    ##list of multi-file packages
    #packages=find_packages(include=['sample', 'sample.*']) 
    python_requires='>=3',
    install_requires = [# 
        'jupytext'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Operating Systme :: OS Independent",
    ],
)