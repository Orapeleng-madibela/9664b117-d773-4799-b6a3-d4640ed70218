#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py

# PROGRAMMER: ORAPELENG TIMOTHY MADIBELA
# DATE CREATED: 30 AUGUST 2026
# REVISED DATE:
#
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the program run using the classifier's
#          model architecture to classify the images.

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using the
    classifier's model architecture to classify pet images.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a list:
                    idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 where 1 = match between pet and classifier
                            labels and 0 = no match
                    idx 3 = 1/0 where 1 = pet image is a dog and
                            0 = pet image is NOT a dog
                    idx 4 = 1/0 where 1 = classifier classifies image
                            as a dog and 0 = classifier classifies image
                            as NOT a dog

    Returns:
      results_stats_dic - Dictionary containing the results statistics.
    """

    # Create the results statistics dictionary
    results_stats_dic = dict()

    # Initialize counters
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Iterate through the results dictionary
    for key in results_dic:

        # Check if the pet image is a dog
        if results_dic[key][3] == 1:

            # Count dog images
            results_stats_dic['n_dogs_img'] += 1

            # Check if classifier correctly identifies image as a dog
            if results_dic[key][4] == 1:

                # Count correctly classified dog images
                results_stats_dic['n_correct_dogs'] += 1

                # Check if the breed was correctly classified
                if results_dic[key][2] == 1:
                    results_stats_dic['n_correct_breed'] += 1

        else:
            # Count non-dog images
            results_stats_dic['n_notdogs_img'] += 1

            # Check if classifier correctly identifies image as NOT a dog
            if results_dic[key][4] == 0:

                # Count correctly classified non-dog images
                results_stats_dic['n_correct_notdogs'] += 1

        # Check if pet label and classifier label match
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

    # Calculate percentage of correct matches
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (
            results_stats_dic['n_match'] /
            results_stats_dic['n_images']
        ) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0

    # Calculate percentage of correctly classified dogs
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (
            results_stats_dic['n_correct_dogs'] /
            results_stats_dic['n_dogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0

    # Calculate percentage of correctly classified dog breeds
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (
            results_stats_dic['n_correct_breed'] /
            results_stats_dic['n_dogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    # Calculate percentage of correctly classified non-dogs
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (
            results_stats_dic['n_correct_notdogs'] /
            results_stats_dic['n_notdogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    # Return the results statistics dictionary
    return results_stats_dic
