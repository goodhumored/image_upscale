
#!/bin/bash

# Folders
compressed_images_folder="compressed_images"
sent_images_folder="result_images"
result_folder="result_images"

# Create directories if they don't exist
mkdir -p "$sent_images_folder"
mkdir -p "$result_folder"

# Number of images to process
num_images=5

# Pick random images from compressed_images_folder
images=($(ls "$compressed_images_folder" | sort -R | tail -n "$num_images"))

# Iterate over the selected images
for image in "${images[@]}"
do
    # Define paths
    input_image="$compressed_images_folder/$image"
    output_image="$result_folder/result_$image"
    sent_image="$sent_images_folder/sent_$image"

    # Send the image using curl and save the result
    curl -X POST http://localhost:5000/upscale \
         -F "image=@$input_image" \
         --output "$output_image"

    # Copy the sent image to the sent_images_folder
    cp "$input_image" "$sent_image"

    echo "Processed $image: result saved to $output_image, sent image saved to $sent_image"
done
