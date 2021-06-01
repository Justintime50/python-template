import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    # Add your list of production dependencies here, eg:
    # 'requests == 1.*',
]

DEV_REQUIREMENTS = [
    'coveralls == 3.*',
    'flake8',
    'mock == 4.*',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

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
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS
    },
    entry_points={
        'console_scripts': [
            'PROJECT_NAME=python_project.my_module:main'
        ]
    },
    python_requires='>=3.6',
)
