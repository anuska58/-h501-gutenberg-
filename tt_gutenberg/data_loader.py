import pandas as pd

AUTHORS_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
LANGUAGES_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
METADATA_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"


def load_authors() -> pd.DataFrame:
    """Load the Gutenberg authors dataset."""
    return pd.read_csv(AUTHORS_URL)


def load_languages() -> pd.DataFrame:
    """Load the Gutenberg languages dataset."""
    return pd.read_csv(LANGUAGES_URL)


def load_metadata() -> pd.DataFrame:
    """Load the Gutenberg metadata dataset."""
    return pd.read_csv(METADATA_URL)
