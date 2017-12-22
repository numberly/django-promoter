from os import path
from codecs import open

from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
PROMOTER_VER = '0.4'

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-promoter',

    version=PROMOTER_VER,

    description='Django commands used to promote or demote users',
    long_description=long_description,

    url='https://github.com/numberly/django-promoter',

    author='Theo Massard',
    author_email='theo.massard@1000mercis.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='django auth admin cli python3.5',

    packages=find_packages(),
)
