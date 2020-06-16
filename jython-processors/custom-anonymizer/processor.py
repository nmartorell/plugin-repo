def process(row):
    
    # Retrieve the user-defined input column
    input_column = params["input_column"]

    # Retrieve the list of words to anonymize (defined as a plugin parameter)
    w = get_plugin_config()
    
    #print("here!")
    #print(w)
    
    #dataiku.customrecipe.get_plugin_config()["words_to_remove"]
    
    return input_column
