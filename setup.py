from setuptools import setup

setup(
    name='nakiri',
    packages=['nakiri'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy'
    ],
)
