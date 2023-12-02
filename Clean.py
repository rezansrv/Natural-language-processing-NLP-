import nltk
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import re
import os

nltk.download('punkt')

# Define the input directory path
input_directory = 'inputs'

# Ensure the 'inputs' directory exists
os.makedirs(input_directory, exist_ok=True)

# Get the input file name from the user
input_file_name = input("Enter the input file name (e.g., Eng.txt): ")

# Construct the full input file path by joining the input directory and file name
input_file_path = os.path.join(input_directory, input_file_name)

# Check if the input file exists
if not os.path.exists(input_file_path):
    print(f"Input file '{input_file_name}' not found in the '{input_directory}' directory.")
else:
    # Read the HTML text from the file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()

    # Remove tags and convert to plain text
    text = BeautifulSoup(html_text, 'html.parser').get_text()

    # Tokenize the text into words
    words = word_tokenize(text)

    # Join the cleaned words into a string
    cleaned_text = ' '.join(words)

    # Define the output directory path
    output_directory = 'outputs'

    # Ensure the 'outputs' directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Define the output file path
    output_file_path = os.path.join(output_directory, 'cleaned_text.txt')

    # Save the cleaned text to the output file in the 'outputs' directory
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

    print(f"Cleaned text has been saved to 'cleaned_text.txt' in the '{output_directory}' directory.")
