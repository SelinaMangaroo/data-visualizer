from setuptools import setup, find_packages

setup(
    name='xml_to_csv_lib',
    version='1.0.0',
    description='A library for converting XML files to CSV.',
    author='Selina Mangaroo',
    author_email='selinamangaroo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)