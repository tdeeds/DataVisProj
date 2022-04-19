import pandas as pd


def institutions_data(mx):
    df = pd.read_csv('institutions.csv')
    df = df.head(mx)
    return df


def institutions_definitions(mx):
    df = pd.read_csv('institutions_definitions.csv')
    df = df.head(mx)
    return df
