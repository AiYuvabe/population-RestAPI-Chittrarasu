import pandas as pd
# from backend.population_pandas import get_continents, get_continent_data
from backend.logger import logger

import os

# file_path = os.path.join(os.path.dirname(__file__), "../../data/world_population.csv")
file_path = os.path.join(os.path.dirname(__file__), "../data/world_population.csv")
# file_path = os.path.abspath(file_path)  # Convert to absolute path

file_path = os.path.abspath(file_path)  # Convert to absolute path
try:
    df = pd.read_csv(file_path)
    logger.info(f"CSV file loaded successfully from: {file_path}")
except Exception as e:
    logger.error(f"Error loading CSV file from {file_path}: {e}")
    df = None  # Prevent NameError if file loading fails

if df is not None:
    # Perform the aggregations only if df is successfully loaded
    continent_stats = df.groupby("Continent").agg(
        Total_Countries=('Country', 'count'),
        Total_Population=('Population', 'sum'),
        Average_Population=('Population', 'mean'),
        Total_Area=('Area', 'sum'),
        max_population=('Population', 'max'),
        min_population=('Population', 'min'),
        Country_Max_Population=('Population', lambda x: df.loc[x.idxmax(), 'Country']),
        Country_Min_Population=('Population', lambda x: df.loc[x.idxmin(), 'Country'])
    ).reset_index()

    # Compute Population Density
    continent_stats["Population_Density"] = (
        continent_stats["Total_Population"] / continent_stats["Total_Area"]
    )

    logger.info("Data processing completed.")

def get_continents():
    """Returns a list of all continents."""
    logger.info("Fetching all continents.")
    return continent_stats["Continent"].tolist()

def get_continent_data(continent):
    """Returns statistics for a specific continent."""
    logger.info(f"Fetching data for continent: {continent}")
    result = continent_stats[continent_stats["Continent"] == continent].squeeze()

    if result.empty:
        logger.warning(f"No data found for continent: {continent}")
        return {}

    return result.to_dict()


