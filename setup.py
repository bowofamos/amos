from setuptools import setup

setup(
    name='AmosMsg',
    version='0.0.1',
    author='ganyu',
    author_email='amosbow@163.com',
    url='https://github.com/bowofamos/amos#readme',
    description=u'MQ Consumer',
    packages=['AmosMsg'],
    install_requires=[
        "PyYAML",
        "pika"
    ]
)