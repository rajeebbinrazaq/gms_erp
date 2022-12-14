from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gms_erp/__init__.py
from gms_erp import __version__ as version

setup(
	name="gms_erp",
	version=version,
	description="Custom app for GMS",
	author="tacten",
	author_email="tech@tacten.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
