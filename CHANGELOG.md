# CHANGELOG

## v1.10.0 (2023-08-24)

- Drops Python 3.7 support
- Swaps the Makefile for a Justfile
- Overhauls version constant and usage (uniform between `setup.py` and package code)
- Cleans up GitHub Action workflows
- Adds `bandit` dev dependency

## v1.9.1 (2023-05-08)

- Fixes a replacement typo in setup.py for `package_data`
- Bumps all dependencies

## v1.9.0 (2022-11-02)

- Removes the `coveralls` dev dependency and instead updates `pytest-cov` to v4 which now supports `lcov` generation

## v1.8.0 (2022-05-15)

- Overhaul the build process (uses the `build` package instead of the legacy `python setup.py` command)
- Simplifies the GitHub release workflow by using the new Makefile build targets
- Ignores the test directory in the build
- Pins all development dependencies

## v1.7.1 (2022-02-10)

- Update Makefile install target to not symlink to the home directory
- Update Black to use the `preview` flag
- Bump dev dependencies

## v1.7.0 (2021-11-29)

- Adds `mypy` and type hinting via `py.typed`
- Simplifies template module (removes unused class)
- Adds missing `__all__` variable to `__init__.py`
- Simplifies the lint step of the build by only running checks once (previously some checks were getting run twice)
- Tests against Python `3.10`

## v1.6.0 (2021-10-08)

- Adds `Black` and `iSort` as dev dependencies
- Adds a `pyproject.toml` file to configure Python tools
- Completely refactors the `Makefile` to include new tools and better ways of invoking previous ones
- Removes `.github/FUNDING.yml` file in favor of `.github` global files

## v1.5.0 (2021-09-10)

- Drops support for Python 3.6
- Removes the `mock` library in favor of the builtin `unittest.mock` library
- Fix some typos

## v1.4.0 (2021-07-12)

- Clarified various pieces of info
- Unified more text replacements for easier usage of the template when getting started

## v1.3.0 (2021-05-31)

- Pins dependencies and moves them to a constant
- Adds missing lines to code coverage report

## v1.2.0 (2021-01-30)

- Fixed the Coveralls command in GitHub Actions, builds now pass with their new platform requirement flag
- Added a `release.yml` file to automate PyPI releasing via GitHub Actions

## v1.1.1 (2021-01-09)

- Removed all references to Travis-CI and replace with GitHub Actions
- Bumped the year in LICENSE
- Added clarifying statement in README to remove all extra assets

## v1.1.0 (2021-01-05)

- Added GitHub Actions
- Added `conftest.py`
- Updated `README` with much more verbose instructions on changing details of the project to get you started
- Added test coverage
- Correcting lint Makefile target to point to the unit folder

## v1.0.0 (2020-11-19)

- Initial release
- Makefile, README, setup.py, .travis.yml, LICENSE, test suite, module, assets, and more included to save time and energy on your next Python project
