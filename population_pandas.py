import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()
df = pd.read_csv("world_population.csv")

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


@app.get("/")
def home():
    return {"message": "Welcome to the home page"}

@app.get("/continents/")
def get_all_continents():
    continents = continent_stats["Continent"].tolist()
    return {"continents": continents}

@app.get("/continents/{continent}/")
def get_continent_stats(continent: str, stat: str = None):
    # Filter the dataframe for the given continent
    result = continent_stats[continent_stats["Continent"] == continent].squeeze()
    print(result)
    print(type(result))

    # Convert row to a dictionary
    result = result.to_dict()
    print(result)

    if stat:
        if stat in result:  # Check if the requested stat is valid
            return {stat: result[stat]}
        else:
            raise HTTPException(status_code=400, detail="Invalid statistic requested")

    return result  
