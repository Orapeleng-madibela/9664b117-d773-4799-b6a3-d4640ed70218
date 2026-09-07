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
    Calculates classification statistics.

    Parameters:
        results_dic (dict): Dictionary containing classification results.

    Returns:
        dict: Dictionary containing calculated statistics.
    """

    results_stats_dic = {}

    # Initialize counters
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Process every image
    for key in results_dic:

        # Count whether the image is actually a dog
        if results_dic[key][3] == 1:

            results_stats_dic['n_dogs_img'] += 1

            # Check if classifier correctly identifies it as a dog
            if results_dic[key][4] == 1:

                results_stats_dic['n_correct_dogs'] += 1

                # Check whether the breed was correctly identified
                if results_dic[key][2] == 1:
                    results_stats_dic['n_correct_breed'] += 1

        else:

            results_stats_dic['n_notdogs_img'] += 1

            # Check if classifier correctly identifies it as NOT a dog
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

        # Check whether labels match
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

    # Percentage of correctly matched labels
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (
            results_stats_dic['n_match'] /
            results_stats_dic['n_images']
        ) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0

    # Percentage of correctly classified dogs
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (
            results_stats_dic['n_correct_dogs'] /
            results_stats_dic['n_dogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0

    # Percentage of correctly classified dog breeds
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (
            results_stats_dic['n_correct_breed'] /
            results_stats_dic['n_dogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    # Percentage of correctly classified non-dogs
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (
            results_stats_dic['n_correct_notdogs'] /
            results_stats_dic['n_notdogs_img']
        ) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic

