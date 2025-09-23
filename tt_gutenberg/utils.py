import pandas as pd

def clean_aliases(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter out messy values and keep only rows with valid aliases.
    """
    df = df[df["alias"].notna()]
    df = df[df["alias"].str.strip() != ""]
    return df

def count_translations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Count translations by alias.
    """
    counts = (
        df.groupby("alias")
        .size()
        .reset_index(name="translation_count")
        .sort_values("translation_count", ascending=False)
    )
    return counts