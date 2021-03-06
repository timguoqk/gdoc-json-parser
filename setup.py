from setuptools import setup

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

# TODO: documentations
setup(name='gdoc-json-parser',
      version='1.0.0.dev3',
      description='Convert Google spreadsheet to clean json.',
      long_description=README_TEXT,
      author='Tim Guo',
      author_email='qikun.guo@engineering.ucla.edu',
      url='https://github.com/timguoqk/gdoc-json-parser',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Topic :: Utilities',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4'],
      keywords='json google spreadsheet parser',
      license='MIT',
      py_modules=[],
      )
