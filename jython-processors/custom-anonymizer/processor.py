from dataiku.customrecipe import *

# This file is the actual code for the custom Jython step custom-anonymizer

def process(row):
    
    # Retrieve the user-defined input column
    input_column = params["input_column"]

    # Retrieve the list of words to anonymize (defined as a plugin parameter)
    #words_to_anonymize = params["words_to_remove"]
    
    dataiku.customrecipe.get_plugin_config()["words_to_remove"]
    
    return input_column
