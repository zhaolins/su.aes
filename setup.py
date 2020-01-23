from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = "0.1.6"
NAME = "aes"
DESCRIPTION = "A simple encrypt/decrypt lib based on AES."
INSTALL_REQUIRES = [
    'pycrypto'
]

package_name = f"su.{NAME}"
entry_point = f"su-{NAME} = {package_name}:main"
here = path.abspath(path.dirname(__file__))
description_header = f'''
# su.{NAME}

{DESCRIPTION}

'''

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    md_description = description_header + f.read()
    try:
        import pypandoc
        long_description = pypandoc.convert_text(md_description, to='rst', format='md')
    except(IOError, ImportError) as e:
        long_description = md_description

setup(
    name=package_name,
    version=VERSION,
    description=DESCRIPTION,
    long_description='',
    url=f'https://github.com/zhaolins/{package_name}',
    author='Zhaolin Su',
    author_email='z@suho.me',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='development',
    namespace_packages=['su'],
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts':[
            entry_point
        ] if entry_point else '',
    },
)
