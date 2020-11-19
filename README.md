<div align="center">

# Python Template

A Python project template to save you time and energy.

[![Build Status](https://travis-ci.com/justintime50/python-template.svg?branch=main)](https://travis-ci.com/justintime50/python-template)
[![Licence](https://img.shields.io/github/license/justintime50/python-template)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

Python projects take a long time to setup with all the various files, the virtual environment, and keeping things uniform across projects. With this Python template, you can quickly setup boilerplate code and miscellaneous items for your Python project saving you time and energy so you can get back to coding. 

## Install

Click the `Use this template` button on this project's GitHub page.

<img src="assets/use_template_button.png" alt="Use Template Button">

## Usage

Replace/rename files as needed:

1. Configure the `setup.py` file
1. Update the Makefile targets to use your directory
1. Update name in LICENSE
1. Update `.travis.yml` file as needed
1. Rename files/folders as needed 
1. Delete this `README` and rename `README_project.md` to `README.md`

**Travis-CI**

To add a secure PyPi API key to your `.travis.yml` file, run the following command and replace `your-api-token` with your real API token.

```bash
travis encrypt your-api-token --add deploy.password --com
```
