from setuptools import setup, find_packages

setup(
    name='custom_bucket_objects',
    version='0.1.0',
    author='David Cannan',
    author_email='Cdaprod@Cdaprod.dev',
    description='A LangChain-powered tool for transforming Python and Markdown files into structured, clean data objects, enhancing data handling and analysis efficiency.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Cdaprod/custom_bucket_objects',
    project_urls={
        'Bug Tracker': 'https://github.com/Cdaprod/custom_bucket_objects/issues',
    },
    license='LICENSE.txt',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'langchain',
        'pydantic',
        'pandas',
        'PyYAML',
        'markdown2',
        'unittest',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)