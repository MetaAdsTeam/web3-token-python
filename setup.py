from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='web3-token',
    packages=['web3_token'],
    version='1.0.0',
    license='MIT',
    description='Web3 Token implementation for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alex Dudko',
    author_email='duke@simfik.ru',
    url='https://github.com/MetaAdsTeam/web3-token-python',
    download_url='https://github.com/MetaAdsTeam/web3-token-python/archive/v_1_0_3.tar.gz',
    keywords=['web', 'web3', 'web3-token', 'etherium', 'crypto', 'blockchain'],
    install_requires=[
        'web3',
        'eth_account',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
