#!/bin/zsh

# run this script in the project's root directory

convert src/assets/img/bg-masthead.jpg  -write mpr:img +delete \
\( mpr:img -resize 576x +write src/assets/img/bg-masthead_576w.webp \) \
\( mpr:img -resize 768x +write src/assets/img/bg-masthead_768w.webp \) \
\( mpr:img -resize 992x +write src/assets/img/bg-masthead_992w.webp \) \
\( mpr:img -resize 1200x +write src/assets/img/bg-masthead_1200w.webp \) \
\( mpr:img -resize 1400x +write src/assets/img/bg-masthead_1400w.webp \) \
null:

find src/assets/img/ -name '*.jpg' -execdir mogrify -format webp {} +