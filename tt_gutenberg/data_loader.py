import pandas as pd
def data_loader():
    url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv'
    df=pd.read_csv(url)
    return df