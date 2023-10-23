from setuptools import setup, find_packages


name = "sfu_api_wrapper"
version = "1.0.0"
description = "SFU API wrapper."
author = "Leaf Turners"
url = "https://github.com/Leaf-Turners/fall-hacks-2023"
long_description = "SFU API wrapper."

install_requires = [
    'aiohttp',
]

packages = find_packages()

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    url=url,
    long_description=long_description,
    packages=packages,
    package_data={'sfu_api_wrapper': ['course_name_to_ids.json']},
    install_requires=install_requires,
)
