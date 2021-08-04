import setuptools

long_description = "just a test"


setuptools.setup(
     name='kruztw_py1',  
     version='0.1',
     scripts=['kruztw_py1'] ,
     author="kruztw",
     author_email="kruztw@gmail.com",
     description="a simple test",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/kruztw",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
