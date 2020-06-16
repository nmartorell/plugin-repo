# Note: this processor anonymizes in a caseless manner.

def process(row):
    
    # List of words to anonymize (ensure caseless)
    words_to_anonymize = ["tags", "doll", "marker", "heart", "colour"] 
    words_to_anonymize = [w.casefold() for w in words_to_anonymize]
    
    # Retrieve the user-defined input column
    text_column = params["input_column"]

    # Anonymize words from list
    text_list = row[text_column].split(" ")
    text_list_anon = [w if w.casefold() not in words_to_anonymize else "****" for w in text_list]
    
    return " ".join(text_list_anon)