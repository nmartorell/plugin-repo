def do(payload, config, plugin_config, inputs):
    
    print("here!")
    print(inputs)
    
    # Retrieve filter column
    filter_column = config["filter_column"]
    
    # Create list of unique values in filter column
    
    
    
    choices = [
        { "value" : "val1", "label" : "Value 1"},
        { "value" : "val2", "label" : "Value 2"}
    ]
    
    return {"choices": choices}