from setuptools import find_packages, setup


setup(
    name='pipinstallable',
    license='MIT',

    author='Satoshi SUZUKI',
    author_email='studio3104.com@gmail.com',
    maintainer='Satoshi SUZUKI',
    maintainer_email='studio3104.com@gmail.com',

    url='https://github.com/studio3104/pipinstallable',
    description='Test package for allowing to install package from git',
    python_requires='>=3.6',
    install_requires=[],

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    packages=find_packages(),
)
