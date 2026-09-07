#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/test_classifier.py
#                                                                             
# PROGRAMMER: ORAPELENG TIMOTHY MADIBELA                                                   
# DATE CREATED: 06 SEPTEMBER 2026                              
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. See the example
#          usage below.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Imports classifier function for using pretrained CNN to classify images 
from classifier import classifier

# Test image
test_image = "pet_images/Collie_03797.jpg"

# CNN architecture
model = "vgg"

# Classify image
image_classification = classifier(
    test_image,
    model
)

# Print result
print(
    "\nResults from test_classifier.py"
)

print(
    "Image:",
    test_image
)

print(
    "Using model:",
    model
)

print(
    "Classified as:",
    image_classification
)
