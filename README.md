# 2_python_prj_with_setupfile
Python Prj with DetailedSetup File and read environment files

contains Detailed Setup File
contains code to include python repository as python library
contains code to read environment files
  Different ways to provide environment variables
     1. As variables and secrets in github workflow file => implemented
     2. Pass environment_name , environment file path as environment variables in github workflow and use python-dotenv library to read the environment file => implemented
     3. Reading environment variables in setup.py file using python-dotenv library => not working as of now

