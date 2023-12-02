import os
import spacy

# Define the directory where the output file is located
output_directory = 'outputs'

# Define the input file path (assuming it's in the 'outputs' directory)
input_file_path = os.path.join(output_directory, 'cleaned_text.txt')  # Assuming Persian (Farsi) text

# Read the cleaned text from the file
with open(input_file_path, "r", encoding="utf-8") as file:
    cleaned_text = file.read()

# Load the spaCy language model for Persian (Farsi)
nlp_fa = spacy.load('xx_ent_wiki_sm')  # Load the Persian model

# Add the sentencizer component to the pipeline
nlp_fa.add_pipe('sentencizer')

# Parse the text with spaCy
doc_fa = nlp_fa(cleaned_text)

# Define the output file path for parsed sentences
output_parsed_sentences_path = os.path.join(output_directory, 'parsed_sentences_fa.txt')

# Save the parsed sentences to the output file
with open(output_parsed_sentences_path, "w", encoding="utf-8") as parsed_sentences_file:
    for sentence in doc_fa.sents:
        parsed_sentences_file.write(sentence.text + "\n")

print(f"Parsed Persian (Farsi) sentences have been saved to '{output_parsed_sentences_path}' successfully.")
