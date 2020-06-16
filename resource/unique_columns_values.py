import dataiku

def do(payload, config, plugin_config, inputs):
    
    # Retrieve filter column
    filter_column = config["filter_column"]
    
    # Retrieve input dataset
    input_dataset = inputs[0]["fullName"]
    
    dataset = dataiku.Dataset(input_dataset)
    df = dataset.get_dataframe()
    
    unique_vals = df[filter_column].unique().tolist()
    
    print(unique_vals)
    
    choices = [
        { "value" : "val1", "label" : "Value 1"},
        { "value" : "val2", "label" : "Value 2"}
    ]
    
    return {"choices": choices}