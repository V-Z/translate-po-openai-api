"""
PO File Translation Script

This script uses the OpenAI GPT-3.5 API to translate PO files. It takes three arguments: 
the source file, the target file, and the target language. The script will iterate over 
all entries in the PO file and translate the ones that are either untranslated or marked 
as fuzzy. It will print the string it is currently translating and any errors that occur 
during translation.

Usage:
python translate.py <source_file> <target_file> <target_language>

Requirements:
To run the script, you need to have the `openai` and `polib` Python libraries installed. 
You also need to have a valid OpenAI API key, which should be set as the `OPENAI_API_KEY` 
environment variable.
"""

import os
import sys
import openai
import polib
from openai.api_resources import Completion

# Load the API key from the system environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Check if the necessary arguments were provided
if len(sys.argv) != 4:
    print("Usage: python translate.py <source_file> <target_file> <target_language>")
    sys.exit(1)

# Load the script arguments
source_file = sys.argv[1]
target_file = sys.argv[2]
target_language = sys.argv[3]

# Load the PO file
po = polib.pofile(source_file)

# Iterate over all entries in the PO file
for entry in po:
    # Check if the entry is untranslated or marked as fuzzy
    if entry.msgstr == '' or 'fuzzy' in entry.flags:
        print(f"Translating: {entry.msgid}")
        try:
            # Translate using GPT-3.5
            response = Completion.create(
              engine="text-davinci-003",
              prompt=f"Translate the following English text about openSUSE Linux to {target_language}:\n\n{entry.msgid}",
              temperature=0.5,
              max_tokens=60
            )
            
            # Set the translated text as the translation of the entry
            entry.msgstr = response.choices[0].text.strip()
            if 'fuzzy' in entry.flags:
                entry.flags.remove('fuzzy')
        except Exception as e:
            print(f"Error translating string: {entry.msgid}. Error: {e}")

# Save the translated PO file
po.save(target_file)

