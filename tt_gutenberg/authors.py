from .data_loader import load_data
from .utils import clean_aliases, count_translations

def list_authors(by_languages=True, alias=True):
    """
    Return a list of author aliases ordered by translation count.
    """
    df = load_data()
    df = clean_aliases(df)

    if by_languages:
        counts = count_translations(df)
        return counts["alias"].tolist()
    else:
        return df["alias"].unique().tolist()
