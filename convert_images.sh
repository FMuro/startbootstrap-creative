#!/bin/zsh

# run this script in the project's root directory

find src/assets/img/ -name '*.jpg' -execdir mogrify -format webp {} +