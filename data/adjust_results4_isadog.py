#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: ORAPELENG TIMOTHY MADIBELA
# DATE CREATED: 30 AUGUST 2026
# REVISED DATE: 31 AUGUST 2026
# PURPOSE: Adjusts the results dictionary to indicate whether the pet image
#          and classifier labels represent a dog.

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images 'as a dog' or 'not a dog'.

    Parameters:
      results_dic - Dictionary with image filename as key and a list as value:
                    index 0 = pet image label
                    index 1 = classifier label
                    index 2 = labels match (1) or do not match (0)

      dogfile - Text file containing all dog names.

    Returns:
      None - results_dic is a mutable data type and is adjusted directly.
    """

    # Create an empty dictionary for dog names
    dognames_dic = {}

    # Open the dog names file and read each dog name
    with open(dogfile, "r") as infile:

        for line in infile:

            # Remove the newline character and whitespace
            dog_name = line.rstrip()

            # Add dog name to dictionary if it does not already exist
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(
                    "** Warning: Duplicate dog name found in dognames.txt:",
                    dog_name
                )

    # Process every image in the results dictionary
    for key in results_dic:

        # Get pet image label and classifier label
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Determine whether the pet image label is a dog
        if pet_label in dognames_dic:
            pet_is_dog = 1
        else:
            pet_is_dog = 0

        # Classifier labels may contain multiple names separated by commas.
        # Example:
        # "dalmatian, coach dog, carriage dog"
        classifier_names = classifier_label.split(",")

        # Assume classifier label is not a dog initially
        classifier_is_dog = 0

        # Check every name returned by the classifier
        for name in classifier_names:

            # Remove spaces around each name
            name = name.strip()

            # If any classifier name is a dog breed, classify as a dog
            if name in dognames_dic:
                classifier_is_dog = 1
                break

        # Add the dog classification results to indexes 3 and 4
        results_dic[key].extend([
            pet_is_dog,
            classifier_is_dog
        ])
