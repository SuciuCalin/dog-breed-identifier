#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Eugen-Calin Suciu
# DATE CREATED: 29.04.2020                                 
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
from os import listdir, path

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve the filenames from image_dir
    filename_list = listdir(image_dir)
    
    # Create the results_dic
    results_dic = dict()
    
    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. 
    # This dictionary's value is a List that contains only one item - the pet image label
    for idx in range(len(filename_list)):
        if not filename_list[idx].startswith('.'):
            if filename_list[idx] not in results_dic:
                filename_no_ext = path.splitext(filename_list[idx])[0].lower()
                result = ''.join([i for i in filename_no_ext if i.isalpha() or i == '_'])
                pet_label = result.replace('_', ' ').strip()               
                results_dic[filename_list[idx]] = [pet_label]
            else:
                print("** Warning: Key=", filenames[idx], 
                      "already exists in results_dic with value =", 
                      results_dic[filenames[idx]])

    # The results_dic dictionary that we created with this function
    return results_dic
