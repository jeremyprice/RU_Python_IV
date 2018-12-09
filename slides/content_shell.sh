#!/bin/false
# Get a copy of the course materials
# optional step
sudo yum install git

# clone the repo
git clone https://github.com/jeremyprice/RU_Python_IV


# System Config
python --version
python3 --version

# Virtualenv
# virtualenv in Python 3
python3 -m venv directory_name

# virtualenv in Python 2
# CentOS 7
sudo yum install python-virtualenv
# Ubuntu
sudo apt install virtualenv
virtualenv directory_name

# use the virtualenv
source directory_name/bin/activate
# stop using the virtualenv
deactivate
