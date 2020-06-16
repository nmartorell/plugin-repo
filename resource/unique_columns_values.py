import dataiku

def do(payload, config, plugin_config, inputs):
    
    # Retrieve filter column
    filter_column = config["filter_column"]
    
    # Retrieve input dataset as dataframe
    input_dataset_name = inputs[0]["fullName"]
    
    dataset = dataiku.Dataset(input_dataset_name)
    df = dataset.get_dataframe()
    
    # Generate list of dictionaries with unique values in column
    choices = [{"value" : x, "label" : x} for x in df[filter_column].unique().tolist()]
    
    return {"choices": choices}