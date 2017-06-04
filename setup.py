from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='Estimating time complexity of an algorithm',
      url='https://github.com/AGHPythonCourse2017/zad2-mateusz-olczyk/tree/production',
      author='Mateusz Olczyk',
      author_email='matik60@gmail.com',
      packages=['estimation', 'task'],
      install_requires=[
          'numpy',
          'matplotlib',
      ],
      zip_safe=False)
