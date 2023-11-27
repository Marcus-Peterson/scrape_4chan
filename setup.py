
from setuptools import setup, find_packages

setup(
    name='4chan-scraping-toolkit',
    version='0.1.0',
    packages=find_packages(),
    description='A toolkit for scraping data from 4chan, suitable for research purposes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-github-username/4chan-scraping-toolkit',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    install_requires=[
        'requests',
        'pandas',
        'beautifulsoup4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    keywords='4chan scraping, data collection, hate speech detection',
    python_requires='>=3.6',
)
