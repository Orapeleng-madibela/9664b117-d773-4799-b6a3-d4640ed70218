#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: ORAPELENG TIMOTHY MADIBELA
# DATE CREATED: 30 AUGUST 2026
# REVISED DATE: 31 AUGUST 2026
# PURPOSE: Prints the results statistics from the results statistics dictionary.
#          Optionally prints incorrectly classified dogs and incorrectly
#          classified dog breeds.

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dog images and incorrectly classified dog breeds if requested.

    Parameters:
      results_dic - Dictionary containing image classification results.
      results_stats_dic - Dictionary containing result statistics.
      model - CNN model architecture: resnet, alexnet, or vgg.
      print_incorrect_dogs - True to print incorrectly classified dogs.
      print_incorrect_breed - True to print incorrectly classified breeds.

    Returns:
      None
    """

    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(),
          "***")

    print("{:20}: {:3d}".format(
        'N Images',
        results_stats_dic['n_images']
    ))

    print("{:20}: {:3d}".format(
        'N Dog Images',
        results_stats_dic['n_dogs_img']
    ))

    # TODO 6a:
    # Print the number of images that are NOT dogs.
    print("{:20}: {:3d}".format(
        'N Not-Dog Images',
        results_stats_dic['n_notdogs_img']
    ))

    # Prints summary statistics (percentages) on Model Run
    print(" ")

    # TODO 6b:
    # Print all percentage statistics.
    for key in results_stats_dic:
        if key.startswith('p'):
            print("{:20}: {:.2f}".format(
                key,
                results_stats_dic[key]
            ))

    # IF print_incorrect_dogs == True AND there were images incorrectly
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and
        ((results_stats_dic['n_correct_dogs'] +
          results_stats_dic['n_correct_notdogs'])
         != results_stats_dic['n_images'])):

        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # Process through results dictionary
        for key in results_dic:

            # TODO 6c:
            # Print images where:
            # 1. The actual image is a dog but classifier says NOT a dog
            # OR
            # 2. The actual image is NOT a dog but classifier says dog

            if ((results_dic[key][3] == 1 and results_dic[key][4] == 0) or
                (results_dic[key][3] == 0 and results_dic[key][4] == 1)):

                print("Real: {:>26}   Classifier: {:>30}".format(
                    results_dic[key][0],
                    results_dic[key][1]
                ))

    # IF print_incorrect_breed == True AND there were dogs whose breeds
    # were incorrectly classified - print out these cases
    if (print_incorrect_breed and
        (results_stats_dic['n_correct_dogs'] !=
         results_stats_dic['n_correct_breed'])):

        print("\nINCORRECT Dog Breed Assignment:")

        # Process through results dictionary
        for key in results_dic:

            # Pet Image Label is-a-Dog, classified as-a-dog
            # but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0):

                print("Real: {:>26}   Classifier: {:>30}".format(
                    results_dic[key][0],
                    results_dic[key][1]
                ))
