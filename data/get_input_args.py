```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
get_input_args.py

Retrieves command-line arguments for the pet image classifier project.

Arguments:
    --dir       Directory containing pet images.
    --arch      CNN architecture: vgg, alexnet, or resnet.
    --dogfile   Text file containing dog names.
"""

import argparse


def get_input_args():
    """
    Retrieves and parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Classify pet images using a pretrained CNN."
    )

    parser.add_argument(
        '--dir',
        type=str,
        default='pet_images/',
        help='path to the folder containing pet images'
    )

    parser.add_argument(
        '--arch',
        type=str,
        default='vgg',
        choices=['vgg', 'alexnet', 'resnet'],
        help='CNN model architecture to use'
    )

    parser.add_argument(
        '--dogfile',
        type=str,
        default='dognames.txt',
        help='text file containing dog names'
    )

    return parser.parse_args()
```
