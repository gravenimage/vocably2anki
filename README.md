A quick converter of Vocably-export files into my own Anki format.  Extremely hard-coded.

Usage:

First, install [uv](https://docs.astral.sh/uv/getting-started/installation/).  Then run `vocably2anki` as a uv tool:


```
❯ uvx vocably2anki -h
usage: vocably2anki [-h] input output [vocably-separator] [anki-separator]

Converts a Vocably export file to Anki deck

positional arguments:
  input              the input Vocably file (type: Path)
  output             the output Anki file (use "-" for stdout).  File is overwritten. (type: str)
  vocably-separator  the characters separating the vocably columns (type: str, default:      )
  anki-separator     the characters separating two sides of the deck card (type: str, default: ': ')

options:
  -h, --help         show this help message and exit
```

or run the python script directly (this example uses uv to manage the environment contained in `uv.lock`).

```
❯ uv run v2a.py -h
usage: vocably2anki [-h] input output [vocably-separator] [anki-separator]

Converts a Vocably export file to Anki deck

positional arguments:
  input              the input Vocably file (type: Path)
  output             the output Anki file (use "-" for stdout).  File is overwritten. (type: str)
  vocably-separator  the characters separating the vocably columns (type: str, default:      )
  anki-separator     the characters separating two sides of the deck card (type: str, default: ': ')

options:
  -h, --help         show this help message and exit
```