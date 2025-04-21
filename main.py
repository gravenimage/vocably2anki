from pathlib import Path
import arguably


@arguably.command
def convert(vocably: Path, vocably_separator: str = "|", anki_separator: str = ": "):
    """
    converts a Vocably export file to Anki deck

    Args:
        vocably: the input CSV file
        vocably_separator: the characters separating the vocably columns
        anki_separator: the characters separating two sides of the deck card
    """
    with open(vocably, encoding="utf-8") as f:
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
            print(f"{parts[0]}{anki_separator}{parts[1]}")


if __name__ == "__main__":
    arguably.run()
