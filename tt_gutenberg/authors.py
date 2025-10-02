# tt_gutenberg/authors.py
import pandas as pd
from .data_loader import load_authors, load_languages, load_metadata

def list_authors(by_languages: bool = True, alias: bool = True):
    """
    Return a list of author aliases ordered by number of unique translations (languages).
    The first alias will have the most translations; the last will have the fewest.
    """

    # Load data
    authors = load_authors()
    languages = load_languages()
    metadata = load_metadata()

    # 1️⃣ Join languages → metadata on gutenberg_id
    lang_meta = pd.merge(
        languages,
        metadata[["gutenberg_id", "gutenberg_author_id"]],
        on="gutenberg_id",
        how="left"
    )

    # 2️⃣ Count unique languages per gutenberg_author_id
    lang_counts = (
        lang_meta.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="language_count")
    )

    # 3️⃣ Merge with authors
    merged = pd.merge(
        authors,
        lang_counts,
        on="gutenberg_author_id",
        how="left"
    )
    merged["language_count"] = merged["language_count"].fillna(0).astype(int)

    # 4️⃣ Choose grouping column (alias preferred)
    group_col = "alias" if alias and "alias" in merged.columns else "author"

    # 5️⃣ Aggregate & sort
    result = (
        merged.groupby(group_col)["language_count"]
        .sum()
        .sort_values(ascending=False)
        .index
        .tolist()
    )

    return result
