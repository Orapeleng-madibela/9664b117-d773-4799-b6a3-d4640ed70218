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
                  print_incorrect_dogs=False,
                  print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if requested.

    Parameters:
      results_dic - Dictionary with image filename as key and a list as value:
                    index 0 = pet image label
                    index 1 = classifier label
                    index 2 = labels match
                    index 3 = pet image is a dog
                    index 4 = classifier classifies image as a dog

      results_stats_dic - Dictionary containing counts and percentages.

      model - CNN architecture used: resnet, alexnet, or vgg.

      print_incorrect_dogs - True prints incorrectly classified dog images.

      print_incorrect_breed - True prints incorrectly classified dog breeds.

    Returns:
      None
    """

    # Print the model architecture used
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")

    # Print the number of images
    print("\nNumber of Images:", results_stats_dic["n_images"])

    # Print all percentage statistics
    print("\nPercentage Results:")

    for key in results_stats_dic:

        if key.startswith("pct"):
            print("{:>30}: {:6.1f}%".format(
                key,
                results_stats_dic[key]
            ))

    # Print incorrectly classified dogs if requested
    if print_incorrect_dogs:

        print("\n\n*** Incorrectly Classified Dogs ***")

        incorrect_dogs_found = False

        for key in results_dic:

            # Pet image and classifier disagree about whether image is a dog
            if results_dic[key][3] != results_dic[key][4]:

                incorrect_dogs_found = True

                print(
                    "\nPet Image Label:",
                    results_dic[key][0],
                    "| Classifier Label:",
                    results_dic[key][1]
                )

        if not incorrect_dogs_found:
            print("None")

    # Print incorrectly classified dog breeds if requested
    if print_incorrect_breed:

        print("\n\n*** Incorrectly Classified Dog Breeds ***")

        incorrect_breeds_found = False

        for key in results_dic:

            # A breed is incorrectly classified when:
            # 1. The pet image is actually a dog
            # 2. The classifier correctly identifies it as a dog
            # 3. The breed labels do not match
            if (results_dic[key][3] == 1 and
                    results_dic[key][4] == 1 and
                    results_dic[key][2] == 0):

                incorrect_breeds_found = True

                print(
                    "\nPet Image Label:",
                    results_dic[key][0],
                    "| Classifier Label:",
                    results_dic[key][1]
                )

        if not incorrect_breeds_found:
            print("None")
