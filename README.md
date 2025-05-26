A quick converter of Vocably-export files into my own Anki format (extremely hard-coded).  For example, it converts a Vocably-exported file (with the default settings) into a text file with the following format:

```
ei lupe <i>(noun)</i>: magnifying glass <i>(noun)</i>
et fleip <i>(noun)</i>: joke <i>(noun)</i>
jeg spår <i>(verb)</i>: I predict <i>(verb)</i>
et gjetord <i>(noun)</i>: impressive rumor, high repute <i>(noun)</i>
```

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