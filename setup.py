from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rl_transformer',
    version='0.0.1',
    description='RL experiments with transformers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abelriboulot/rl_transformer',
    author='Abel Riboulot',
    author_email='abel@kta.io',
    package_dir={'': 'rl_transformer'},
    packages=find_packages(where='rl_transformer'),  # Required
    python_requires='>=3.5, <4',
    install_requires=[
        "scipy",
        "numpy",
        "gym"
    ],
    extras_require={
        'dev': [],
        'test': [],
    },

    package_data={
        'sample': [],
    },

    entry_points={
    },

    project_urls={
        'Repo': 'https://github.com/abelriboulot/rl_transformer',
    },
)