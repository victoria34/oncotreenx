from setuptools import setup
setup(name='oncotreenx',
      version='0.2.0',
      description="thin networkx wrapper for oncotree",
      author="James Lindsay",
      author_email="jlindsay@jimmy.harvard.edu",
      url="https://github.com/jim-bo/oncotreenx",
      py_modules=['oncotreenx'],
      install_requires = ['networkx', 'nose'],
      )