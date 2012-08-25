import codecs
import os
from setuptools import setup, find_packages


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    return codecs.open(filepath, encoding='utf-8').read()


setup(
    name='djlint',
    version='0.1.dev',
    license='ISC',
    description='A tool to analyze Django projects and apps for outdated staff.',
    long_description=read('README.rst'),
    url='https://github.com/alfredhq/djlint',
    author='Alfred Developers',
    author_email='team@alfred.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
)
