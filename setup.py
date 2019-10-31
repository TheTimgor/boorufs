from setuptools import setup
setup(
    name='fs-booru',  # Name in PyPi
    author="timgor",
    author_email="egor.vladone@gmail.com",
    description="danbooru filesystem",
    install_requires=[
        "fs~=2.4.11"
    ],
    entry_points = {
        'fs.opener': [
            'booru = opener:BFSOpener',
        ]
    },
    license="WTFPL",
    packages=[],
    version="0.0.1",
)