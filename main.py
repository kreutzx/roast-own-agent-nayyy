import os

# Roast Your Own Agent — one line, tight and specific.
# The sting is earned by a real failing: summarising without reading, billed as confidence.
ENTRY_TEXT = "My agent summarised a 412-page report into one line — 'looks fine' — then billed me for the confidence."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
