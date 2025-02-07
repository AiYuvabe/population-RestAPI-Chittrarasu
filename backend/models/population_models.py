from pydantic import BaseModel, Field
from typing import List, Union

class ContinentBase(BaseModel):
    continent: str = Field(..., title="Continent Name", example="Asia")

class ContinentStats(BaseModel):
    Total_Countries: int = Field(..., title="Total Number of Countries", example=48)
    Total_Population: int = Field(..., title="Total Population", example=4600000000)
    Average_Population: float = Field(..., title="Average Population Per Country", example=96000000)
    Total_Area: int = Field(..., title="Total Land Area (sq km)", example=44679000)
    max_population: int = Field(..., title="Highest Country Population", example=1400000000)
    min_population: int = Field(..., title="Lowest Country Population", example=100000)
    Country_Max_Population: str = Field(..., title="Country with Highest Population", example="China")
    Country_Min_Population: str = Field(..., title="Country with Lowest Population", example="Maldives")
    Population_Density: float = Field(..., title="Population Density (people/sq km)", example=103)

class ContinentResponse(BaseModel):
    continent: str = Field(..., title="Continent Name", example="Asia")
    statistics: ContinentStats

class ContinentsListResponse(BaseModel):
    continents: List[str] = Field(..., title="List of Continents", example=["Asia", "Europe", "Africa"])

class StatResponse(BaseModel):
    stat: str = Field(..., title="Statistic Name", example="Total Population")
    value: Union[str, int, float] = Field(..., title="Statistic Value", example=4600000000)

