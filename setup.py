from distutils.core import setup
setup(
  name = 'SFM4300_readout',
  packages = ['SFM4300_readout'],
  version = '0.1',
  license='MIT',
  description = 'simple wrapper class to read flow data from the SFM4300-20 flow sensor',
  author = 'Oscar Weissenbach',
  author_email = 'oscar.weissenbach@tu-berlin.de',
  url = 'https://github.com/oscarisolin/SFM4300_readout',
  keywords = ['i2c',"read", 'SFM4300', 'flow sensor'],
  install_requires=[
        'smbus2>=0.4',
        'numpy>=1.21.5'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',    
  ],
)