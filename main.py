import os 
import shutil
import random

def make_slideshow(pics_source_dir, infographics_source_dir, destination_dir, infographics_interval = 5):
    # Ensure the destination directory exists 
    os.makedirs(destination_dir, exist_ok=True)

    pics_list = os.listdir(pics_source_dir)
    infographics_list = os.listdir(infographics_source_dir)

    #Randomise order of pics 
    random.shuffle(pics_list)

    infographic_index = 0
    output_index=0

    for pic_index, pic_filename in enumerate(pics_list):
        pic_source_path = os.path.join(pics_source_dir, pic_filename)
        if os.path.isfile(pic_source_path):
            # Create new filename with 0 padded index
            new_info_filename = f"{output_index:04}_image{pic_index}{os.path.splitext(pic_filename)[1]}"
            info_destination_path = os.path.join(destination_dir, new_info_filename)

            shutil.copy2(pic_source_path, info_destination_path)
            output_index += 1
            print(f"Copied {pic_source_path} to {info_destination_path}")
        
        # Insert infographic image after a specified number of images
        if ((pic_index+1) % infographics_interval == 0):
            info_filename = infographics_list[infographic_index]
            info_source_path = os.path.join(infographics_source_dir, info_filename)
            new_info_filename = f"{output_index:04}_info{infographic_index}{os.path.splitext(info_filename)[1]}"
            info_destination_path = os.path.join(destination_dir, new_info_filename)
            shutil.copy2(info_source_path, info_destination_path)
            print(f"Copied {info_source_path} to {info_destination_path}")
            infographic_index += 1
            # Set infographic_index to modulo of length to loop back around
            infographic_index = infographic_index % len(infographics_list)
            output_index += 1
        

# Replace as needed
picsSourceDir = "REPLACE_ME"
infographicsDir = "REPLACE_ME"
destinationDir = "REPLACE_ME"

make_slideshow(picsSourceDir, infographicsDir, destinationDir)