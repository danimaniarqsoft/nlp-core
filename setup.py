from setuptools import setup, find_packages

setup(
    name='nlp_core',
    version='0.0.1',
    author='Daniel Pichardo',
    author_email='calmecad.dev@gmail.com',
    description='A simple Python library for basic data analysis with pandas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/data-science-adventure/nlp-core',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        # Add other dependencies here if any
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Data Analysis',
    ],
    python_requires='>=3.8',
)