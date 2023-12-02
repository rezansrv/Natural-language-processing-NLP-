import os
import spacy

# Define the directory where the output file is located
output_directory = 'outputs'

# Define the input file path (assuming it's in the 'outputs' directory)
input_file_path = os.path.join(output_directory, 'cleaned_text.txt')  # Assuming English text

# Read the cleaned text from the file
with open(input_file_path, "r", encoding="utf-8") as file:
    cleaned_text = file.read()

# Load the spaCy language model for English
nlp_en = spacy.load('en_core_web_sm')  # Load the English model

# Parse the text with spaCy
doc_en = nlp_en(cleaned_text)

# Define the output file path for parsed sentences
output_parsed_sentences_path = os.path.join(output_directory, 'parsed_sentences_en.txt')

# Save the parsed sentences to the output file
with open(output_parsed_sentences_path, "w", encoding="utf-8") as parsed_sentences_file:
    for sentence in doc_en.sents:
        parsed_sentences_file.write(sentence.text + "\n")

print(f"Parsed English sentences have been saved to '{output_parsed_sentences_path}' successfully.")
