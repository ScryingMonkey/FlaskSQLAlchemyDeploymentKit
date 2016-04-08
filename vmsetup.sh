#!/bin/sh

echo "...updating apt-get"
apt-get update  # To get the latest package lists
echo "...installing python2.7"
apt-get install python2.7 -y
echo "...installing pip, dev, and build essential"
apt-get install python-pip python-dev build-essential -y
echo "...installing git"
apt-get install git -y

echo "...upgrading pip "
pip install --upgrade pip
echo "...upgrading virtualenv"
pip install --upgrade virtualenv

echo "...testing installs"
python -V
git --version
pip -V
virtualenv --version

echo "...creating virtualenv"
virtualenv venv --always-copy
echo "...activating virtualenv"
source venv/bin/activate


