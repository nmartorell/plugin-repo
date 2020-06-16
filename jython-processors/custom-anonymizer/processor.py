def process(row):
    
    # List of words to anonymize (assumes all lowercase)
    words_to_anonymize = ["tags", "doll", "marker"] 
    
    # Retrieve the user-defined input column
    text_column = params["input_column"]

    # anonymize words from list
    text_list = " ".split(row[text_column].lower())
    text_list_anon = [w if w not in words_to_anonymize else "****" for w in text_list]
    
    return text_list_anon.join(" ")
