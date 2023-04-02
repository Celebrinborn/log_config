from setuptools import setup

setup(
    name='log_config',
    version='0.1',
    packages=['log_config_package'],
    install_requires=[
        # List any dependencies your package requires
        'logging',
        'pyyaml'
    ],
    url='https://github.com/Celebrinborn/log_config',
    license='',
    author='Celebrinborn',
    author_email='na',
    description='A package for configuring logging'
)
