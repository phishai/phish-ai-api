#!/usr/bin/env python

from setuptools import setup
from codecs import open


def readme():
    with open('README.rst', 'r', 'utf-8') as f:
        return f.read()


setup(name='phish-ai-api',
      version='1.7',
      description='Phish.AI API wrapper',
      long_description=readme(),
      author='Yevgeny Pats',
      author_email='yp@phish.ai',
      url='https://github.com/phishai/phish-ai-api',
      packages=['phish_ai_api'],
      classifiers=['Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5']
     )
