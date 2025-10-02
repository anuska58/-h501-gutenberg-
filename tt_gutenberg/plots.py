# tt_gutenberg/plots.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .data_loader import load_authors, load_languages, load_metadata

def plot_translations(over: str = "birth_century"):
    """
    Plot a barplot showing average number of translations per author by birth century.
    """

    authors = load_authors()
    languages = load_languages()
    metadata = load_metadata()

    # Join and count translations
    lang_meta = pd.merge(
        languages,
        metadata[["gutenberg_id", "gutenberg_author_id"]],
        on="gutenberg_id",
        how="left"
    )
    lang_counts = (
        lang_meta.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="language_count")
    )
    merged = pd.merge(authors, lang_counts, on="gutenberg_author_id", how="left")
    merged["language_count"] = merged["language_count"].fillna(0).astype(int)

    # Create birth century column
    merged["birth_century"] = (merged["birthdate"] // 100 * 100).astype("Int64")

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=merged,
        x=over,
        y="language_count",
        ci=95
    )
    plt.title("Average Number of Translations by Birth Century")
    plt.xlabel("Birth Century")
    plt.ylabel("Average Translation Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
