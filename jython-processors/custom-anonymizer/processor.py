def process(row):
    
    # List of words to anonymize (assumes all lowercase)
    words_to_anonymize = ["tags", "doll", "marker"] 
    
    # Retrieve the user-defined input column
    text_column = params["input_column"]

    # anonymize words from list
    text_list = row[text_column].lower().split(" ")
    text_list_anon = [w if w not in words_to_anonymize else "****" for w in text_list]
    
    #return " ".join(text_list_anon)
    return " ".split(row[text_column].lower())