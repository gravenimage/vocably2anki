A quick converter of Vocably-export files into my own Anki format.  Extremely hard-coded.

Usage:

```
❯ uv run .\main.py -h
usage: main.py [-h] vocably [vocably-separator] [anki-separator]

converts a Vocably export file to Anki deck

positional arguments:
  vocably            the input CSV file (type: Path)
  vocably-separator  the characters separating the vocably columns (type: str, default: |)
  anki-separator     the characters separating two sides of the deck card (type: str, default: ': ')

options:
  -h, --help         show this help message and exit
```