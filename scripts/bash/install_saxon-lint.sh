#!/bin/bash

# install saxon-lint
git clone https://github.com/sputnick-dev/saxon-lint.git
cd saxon-lint*
chmod +x saxon-lint.pl

# add saxon-lint.pl to PATH variable
echo "PATH=$PATH:~/scripts/bash/saxon-lint" >> ~/.bashrc

# make an alias
echo "alias saxon-lint='saxon-lint.pl'" >> ~/.bashrc

source ~/.bashrc
