"""setup."""
import os
import setuptools
# try:  # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError:  # for pip <= 9.0.3
#     from pip.req import parse_requirements


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

requirements_path = os.path.join(
    os.path.dirname(__file__), 'requirements.txt')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='pumpwood-database-error',
    version='0.0.4',
    include_package_data=True,
    license='BSD-3-Clause License',
    description=(
        'Package with classes to treatment of database ' +
        'associated errors'),
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/Murabei-OpenSource-Codes/pumpwood-communication',
    author='André Andrade Baceti',
    author_email='a.baceti@murabei.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=[
        "psycopg2-binary",
        "SQLAlchemy>=2.0.37",
        "pandas",
        "loguru>=0.7.3",
        "pumpwood-communication>=2.2.26"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.12",
)
