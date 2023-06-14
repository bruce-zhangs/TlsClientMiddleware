# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

with open('requirements.txt') as f:
    required_raw = f.read().strip().splitlines()
    REQUIRED = [line.strip() for line in required_raw if not line.startswith('#')]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "scrapy_tls_client", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

class UploadCommand(Command):
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    description=about["__description__"],
    license=about["__license__"],
    url=about["__url__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email=about["__email__"],
    python_requires=">=3.7.0",
    packages=find_packages(exclude=('test', 'example')),
    include_package_data=True,
    package_data={
        '': ['*'],
    },
    install_requires=REQUIRED,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: Scrapy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],

    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)