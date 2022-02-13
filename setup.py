from setuptools import setup

with open("README.md", "r")as f:
    long_description =f.head()

setup(
	name='vscode_notebook_convert',
	version='0.1.0',
	packages=['vscode_notebook_convert'],
	python_requires='>=3',
	install_requires = [
		'jupytext'
    ]
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating Systme :: OS Independent",
    ],
)