#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: ORAPELENG TIMOTHY MADIBELA
# DATE CREATED: 30 AUGUST 2026                               
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

from time import time

from print_functions_for_lab_checks import *

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    """Runs the complete pet image classification program."""

    # Start timer
    start_time = time()

    # Get command-line arguments
    in_arg = get_input_args()

    # Check command-line arguments
    check_command_line_arguments(in_arg)

    # Create pet labels
    results = get_pet_labels(in_arg.dir)

    # Check pet image labels
    check_creating_pet_image_labels(results)

    # Classify images
    classify_images(
        in_arg.dir,
        results,
        in_arg.arch
    )

    # Check classifier results
    check_classifying_images(results)

    # Determine dog/not-dog classifications
    adjust_results4_isadog(
        results,
        in_arg.dogfile
    )

    # Check dog classifications
    check_classifying_labels_as_dogs(results)

    # Calculate statistics
    results_stats = calculates_results_stats(results)

    # Check calculated statistics
    check_calculating_results(
        results,
        results_stats
    )

    # Print final results
    print_results(
        results,
        results_stats,
        in_arg.arch,
        True,
        True
    )

    # Stop timer
    end_time = time()

    # Calculate elapsed time
    tot_time = end_time - start_time

    hours = int(tot_time / 3600)
    minutes = int((tot_time % 3600) / 60)
    seconds = int((tot_time % 3600) % 60)

    print(
        "\n** Total Elapsed Runtime:",
        f"{hours}:{minutes}:{seconds}"
    )


if __name__ == "__main__":
    main()

