#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(name='phish-ai-api',
      version='1.0',
      description='Phish.AI API wrapper',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author='Yevgeny Pats',
      author_email='yp@phish.ai',
      url='https://github.com/phishai/',
      packages=['phish_ai_api'],
      classifiers=['Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5']
     )
