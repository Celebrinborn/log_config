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
    url='https://github.com/your-username/my-logging-package',
    license='',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for configuring logging'
)
