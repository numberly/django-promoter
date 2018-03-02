from os import path
from codecs import open

from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
PROMOTER_VER = '1.0.1'

setup(
    name='django-promoter',

    version=PROMOTER_VER,

    description='Django commands used to promote or demote users',
    long_description=open('README.rst').read(),

    url='https://github.com/numberly/django-promoter',

    author='Theo Massard',
    author_email='theo.massard@1000mercis.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Framework :: Django',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='django auth admin cli python3.5',

    packages=find_packages(),
)
