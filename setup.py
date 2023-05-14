from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

# Setup script
setup(
    name='dragon-curve',
    version='1.0.0',
    author="Pedro Mayorga, PhD",
    author_email="ppmayorga80@gmail.com",
    description='Dragon curve',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ppmayorga80/dragon-curve",
    packages=find_namespace_packages(exclude=['tests', 'tests.*']),
    install_requires=list(open('requirements.txt')),
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'dragon = dragon_curve.dragon:main',
        ]
    }
)
