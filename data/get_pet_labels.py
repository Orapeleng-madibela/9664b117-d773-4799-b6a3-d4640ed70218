#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: ORAPELENG TIMOTHY MADIBELA
# DATE CREATED: 30 AUGUST 2026                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on image filenames.

    Parameters:
        image_dir (str): Directory containing pet images.

    Returns:
        dict: Dictionary where each key is an image filename and
              each value is a list containing the pet label.
    """

    filename_list = listdir(image_dir)

    results_dic = {}

    for filename in filename_list:

        # Ignore hidden files such as .DS_Store
        if filename.startswith('.'):
            continue

        # Convert filename to lowercase
        low_pet_image = filename.lower()

        # Split filename using underscores
        word_list_pet_image = low_pet_image.split('_')

        # Build the pet label
        pet_label = ""

        for word in word_list_pet_image:

            # Only include alphabetic words
            if word.isalpha():
                pet_label += word + " "

        # Remove leading/trailing whitespace
        pet_label = pet_label.strip()

        # Add image filename and pet label to dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(
                "** Warning: Duplicate files exist in directory:",
                filename
            )

    return results_dic

