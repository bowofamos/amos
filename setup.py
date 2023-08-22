from setuptools import setup

setup(
    name='AmosMsg',
    version='0.0.2',
    author='ganyu',
    author_email='amosbow@163.com',
    url='https://github.com/bowofamos/amos#readme',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='MQ Consumer',
    packages=['AmosMsg'],
    install_requires=[
        "PyYAML",
        "pika"
    ]
)