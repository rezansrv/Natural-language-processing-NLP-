import nltk
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import re
import os

nltk.download('punkt')

# Define the directory where the output file is located
output_directory = 'outputs'

# Define the input file path (assuming it's in the 'outputs' directory)
input_file_path = os.path.join(output_directory, 'cleaned_text.txt')  # Assuming English text

with open(input_file_path, "r", encoding="utf-8") as file:
    html_text = file.read()

# Remove tags and convert to plain text
text = BeautifulSoup(html_text, 'html.parser').get_text()

# Tokenize the text into words
words = word_tokenize(text)

# Define English stopwords
english_stop_words = set(nltk.corpus.stopwords.words('english'))

# Remove English stopwords from tokens
filtered_tokens = [word for word in words if word.lower() not in english_stop_words]

# Join the cleaned words into a string
filtered_text = ' '.join(filtered_tokens)

# Define the output file path
output_file_path = os.path.join(output_directory, 'filtered_english.txt')

# Save the cleaned text to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(filtered_text)

print("Cleaned English text has been saved to 'filtered_english.txt' in the 'outputs' directory.")
