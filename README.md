# PO File Translation Script

This script uses the OpenAI GPT-3.5 API to translate PO files. It takes three arguments: the source file, the target file, and the target language.

## Usage

To use the script, run the following command:

```bash
python3 translate.py <source_file> <target_file> <target_language>
```

Replace `<source_file>` with the path to the PO file you want to translate, `<target_file>` with the path where you want to save the translated file, and `<target_language>` with the language you want to translate the text into (e.g. `cs`).

The script will iterate over all entries in the PO file and translate the ones that are either untranslated or marked as fuzzy. It will print the string it is currently translating and any errors that occur during translation.

## Requirements

To run the script, you need to have the openai and polib Python libraries installed. You also need to have a valid [OpenAI API key](https://platform.openai.com), which should be set as the `OPENAI_API_KEY` environment variable (e.g. in `~/.bashrc`).

