def do(payload, config, plugin_config, inputs):
    
    print("Here!")
    print(config)
    
    choices = [
        { "value" : "val1", "label" : "Value 1"},
        { "value" : "val2", "label" : "Value 2"}
    ]
    
    return {"choices": choices}