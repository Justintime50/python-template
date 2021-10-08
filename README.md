<div align="center">

# Python Template

A Python project template to save you time and energy.

[![Build Status](https://github.com/Justintime50/python-template/workflows/build/badge.svg)](https://github.com/Justintime50/python-template/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/python-template/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/python-template?branch=main)
[![Licence](https://img.shields.io/github/license/justintime50/python-template)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/python-template/showcase.png" alt="Showcase">

</div>

Python projects take a long time to setup with all the various files, the virtual environment, and keeping things uniform across projects. With this Python template, you can quickly setup boilerplate code and miscellaneous items for your Python project saving you time and energy so you can get back to coding. 

## Install

Click the `Use this template` button at the top of this project's GitHub page, it looks like this:

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/templates/use_template_button.png" alt="Use Template Button">

## Usage

**Easy text replacements**

1. Replace all instances of `project_name` with the name of your project
    * These are the Python snake_case references (eg: `project_name`)
1. Replace all instances of `PROJECT_NAME_URL` with the name of your project
    * These are the references to your project that will appear in URLs and are typically hyphenated (eg: `project-name`)
1. Replace all instances of `USERNAME` with the name of the author or owner of the project
    * These are references typically found in the URL of your project as it appears on GitHub

**File configuration**

1. Configure the `setup.py` file
1. Configure the `Makefile` targets
1. Update the name in the `LICENSE` or swap it out entirely
1. Configure the `.github/workflows/build.yml` file
1. Update the `CHANGELOG.md` with your own info
1. Rename other files/folders as needed and configure their content
1. Delete this `README` and rename `README_project.md` to `README.md`

**GitHub configuration**

1. Add a `PYPI_API_TOKEN` GitHub secret to your project so that automated releasing can occur from GitHub Actions to PyPI and uncomment the final step on the `release` job in `.github/workflows/release.yml`

## Attribution

* Watch [the video](https://youtu.be/ZMfcl3CnRhA) where I built this template.
