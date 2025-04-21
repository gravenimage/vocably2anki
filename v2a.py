from pathlib import Path
import arguably
import sys


@arguably.command
def convert(
    input: Path, output: str, vocably_separator: str = "\t", anki_separator: str = ": "
):
    """
    converts a Vocably export file to Anki deck

    Args:
        input: the input Vocably file
        output: the output Anki file (use "-" for stdout).  File is overwritten.
        vocably_separator: the characters separating the vocably columns
        anki_separator: the characters separating two sides of the deck card
    """

    if output == "-":
        out = sys.stdout
    else:
        out = open(output, encoding="utf-8", mode="w")

    try:
        with open(input, encoding="utf-8") as f:
            first = True
            for line in f.readlines():
                if first:
                    first = False
                    continue
                line = line.strip()
                # some usage colums contain newlines with *-delimited bullet points.  Just skip for now, we're not exporting them at all
                if line.startswith("*"):
                    continue

                parts = line.split(vocably_separator)

                word = parts[0]
                translation = parts[1]
                part_of_speech = parts[2]

                print(f"{word} <i>({part_of_speech})</i>{anki_separator}{translation} <i>({part_of_speech})</i>", file=out)
    finally:
        out.close()


if __name__ == "__main__":
    arguably.run()
