from setuptools import setup

setup(
    name='dynamicbinder',
    version='0.1',
    description="Programming challenge to build parser.",
    long_description="A parser of the basic instructions AND, OR, NOT, ==, <, >, if, else and in",
    classifiers=[
        'Programming Language :: Python :: 3.6.5',
        'Topic :: Compilers:: Parsing',
        ],
    author='Sreenidhin C C',
    author_email='sreenidhin@blueripples.com',
    install_requires=['ply',],
    )
