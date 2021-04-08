from setuptools import setup
import pypandoc


setup(name='apikey',
      version='0.2.2',
      description='save and load API keys from a file',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/apikey',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['apikey'],
      install_requires=[
          'setuptools>=40.0.0'],
      python_requires='>=3.6',
      zip_safe=True)
