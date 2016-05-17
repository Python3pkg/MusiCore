from distutils.core import setup

setup(
  name='musicore',
  packages=['musicore'],  # this must be the same as the name above
  version='0.5',
  description='A audio analysis application',
  author='Aurelien BETTINI',
  author_email='gerox@minet.net',
  url='https://github.com/gerosix/MusiCore',
  download_url='https://github.com/gerosix/MusiCore',  # I'll explain this in a second
  # keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers=[],
  install_requires=[
    'samplerate',
    'numpy',
    'scipy',
    'librosa'
  ]
)
