from distutils.core import setup

setup(name='scaws',
      version='0.1',
      license='BSD',
      description='Scrapy extensions for Amazon EC2',
      author='Scrapinghub',
      author_email='info@scrapinghub.com',
      url='http://github.com/scrapinghub/scaws',
      keywords="scrapy amazon aws ec2",
      packages=['scaws'],
      platforms = ['Any'],
      install_requires = ['Scrapy', 'boto'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'License :: OSI Approved :: BSD License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
