from setuptools import find_namespace_packages
from setuptools import setup

# Optional dependencies
extras_require = {'all': []}

# All dependencies
for key in extras_require:
    if key != 'all':
        extras_require['all'] += extras_require[key]

# Setup script
setup(
    name='fractal-logo',
    version='0.1.0',
    description='Fractal logo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_namespace_packages(exclude=['tests', 'tests.*']),
    install_requires=list(open('requirements.txt')),
    test_suite='tests',
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'dragon-curve = dragon_curve:main',
        ]
    }
)
