#!/bin/bash

# intall in lib folder
mkdir -p ~/lib  && cd ~/lib

# install quarto
git clone https://github.com/quarto-dev/quarto-cli
cd quarto-cli
./configure.sh

# tex 4 quarto
quarto install tinytex

# go to home
cd ~/
