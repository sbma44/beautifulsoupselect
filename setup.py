from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='beautifulsoupselect',
      version='0.1',
      description='',
      url='http://github.com/sbma44/beautifulsoupselect',
      author='Tom Lee',
      author_email='thomas.j.lee@gmail.com',
      license='MIT',
      packages=['beautifulsoupselect'],
      install_requires=[
          'BeautifulSoup', 
      ],      
      zip_safe=False)
