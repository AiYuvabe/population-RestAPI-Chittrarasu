import pandas as pd
# from backend.population_pandas import get_continents, get_continent_data
from backend.logger import logger

# Load the dataset
try:
    df = pd.read_csv("data/world_population.csv")
    logger.info("CSV file loaded successfully.")
except Exception as e:
    logger.error(f"Error loading CSV file: {e}")

# Aggregate the data
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
