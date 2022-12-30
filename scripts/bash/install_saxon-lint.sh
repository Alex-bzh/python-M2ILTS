#!/bin/bash

# create lib folder
mkdir -p ~/lib && cd ~/lib

# install saxon-lint
git clone https://github.com/sputnick-dev/saxon-lint.git
cd saxon-lint*
chmod +x saxon-lint.pl

# add saxon-lint.pl to PATH variable
echo "PATH=$PATH:~/lib/saxon-lint" >> ~/.bashrc

# make an alias
echo "alias saxon-lint='saxon-lint.pl'" >> ~/.bashrc

# validation
source ~/.bashrc

# go to home
cd ~/
