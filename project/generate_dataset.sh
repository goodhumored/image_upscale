#!/bin/bash

# создаем папки
mkdir -p original_images_resized
mkdir -p compressed_images

# Проходим по оригинальным изображениям
for image in original_images/*; do
    # Берём название файла
    filename=$(basename -- "$image")
    filename_no_ext="${filename%.*}"
    
    # Меняем размер кладём в папку original_images_resized
    ffmpeg -i "$image" -vf "scale=512:512" -q:v 2 "original_images_resized/${filename_no_ext}.jpg"
    
    # Меняем размер, сжимаем и кладём в "compressed_images"
    ffmpeg -i "$image" -vf "scale=512:512" -q:v 10 "compressed_images/${filename_no_ext}_compressed_10.jpg"
    ffmpeg -i "$image" -vf "scale=512:512" -q:v 20 "compressed_images/${filename_no_ext}_compressed_20.jpg"
    ffmpeg -i "$image" -vf "scale=512:512" -q:v 30 "compressed_images/${filename_no_ext}_compressed_30.jpg"
done

echo "Успешно"
