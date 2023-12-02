import nltk
from nltk.tokenize import word_tokenize
import os

# Download necessary datasets (Punkt tokenizer is used here)
nltk.download('punkt')

# Specify the directory where the cleaned text file is located
cleaned_text_directory = 'outputs'

# Specify the filename (cleaned_text.txt)
cleaned_text_filename = 'cleaned_text.txt'

# Create the full path to the cleaned text file
cleaned_text_file_path = os.path.join(cleaned_text_directory, cleaned_text_filename)

# Read the cleaned text from the file
with open(cleaned_text_file_path, "r", encoding="utf-8") as file:
    cleaned_text = file.read()

# Tokenize the words in the text
words = word_tokenize(cleaned_text)


# Specify the directory where you want to save the output
output_directory = 'outputs'

# Specify the filename for the output file
output_filename = 'Tokenize.txt'

# Create the full path to the output file
output_file_path = os.path.join(output_directory, output_filename)

# Save the tokenized words to the output file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for word in words:
        output_file.write(word + "\n")

print("Successfully saved the tokenized words to:", output_file_path)
