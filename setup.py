from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='English to IPA',
    version='0.2.1',
    description='take English text and convert it to IPA',
    author=['mphilli', 'Mitchellpkt', 'CanadianCommander', 'timvancann'],
    long_description=long_description,
    include_package_data=True,
    packages=['eng_to_ipa'],
)
