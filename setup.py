import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# REQUIREMENTS = [
#     'requests >= 1.0.0',
# ]

setuptools.setup(
    name='PROJECT_NAME',
    version='1.0.0',
    description='Your project description here',  # noqa
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/USERNAME/PROJECT_NAME',
    author='USERNAME',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
            'mock >= 4.0.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'PROJECT_NAME=python_project.my_module:main'
        ]
    },
    python_requires='>=3.6',
)
