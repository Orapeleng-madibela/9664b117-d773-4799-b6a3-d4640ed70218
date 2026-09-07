#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED: ORAPELENG TIMOTHY MADIBELA                                
# REVISED DATE: 30 AUGUST 2026
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 

def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images and compares classifier labels with
    the true pet labels.

    Parameters:
        images_dir (str): Directory containing pet images.
        results_dic (dict): Dictionary containing pet image labels.
        model (str): CNN architecture to use.

    Returns:
        None
    """

    for key in results_dic:

        # Create the complete path to the image
        image_path = os.path.join(images_dir, key)

        # Classify the image
        model_label = classifier(image_path, model)

        # Normalize classifier label
        model_label = model_label.lower().strip()

        # Compare the true pet label with the classifier label
        if results_dic[key][0] == model_label:
            match = 1
        else:
            match = 0

        # Add classifier label and match result
        results_dic[key].extend([model_label, match])

