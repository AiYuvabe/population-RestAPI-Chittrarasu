from fastapi import APIRouter, HTTPException
from backend.population_pandas import get_continents, get_continent_data
from backend.models.population_models import ContinentResponse, ContinentsListResponse, StatResponse
from backend.logger import logger  # Import the logger

router = APIRouter()

@router.get("/continents/", response_model=ContinentsListResponse)
def get_all_continents():
    """Fetch the list of all continents."""
    logger.info("Fetching all continents")
    return {"continents": get_continents()}

@router.get("/continents/{continent}/", response_model=ContinentResponse | StatResponse)
def get_continent_stats(continent: str, stat: str = None):
    """Fetch statistics for a specific continent."""
    logger.info(f"Fetching statistics for continent: {continent}, stat: {stat}")

    continent_data = get_continent_data(continent)

    if not continent_data:
        logger.error(f"Continent not found: {continent}")
        raise HTTPException(status_code=404, detail="Continent not found")

    if stat:
        if stat in continent_data:
            logger.info(f"Returning stat {stat} for {continent}")
            return {"stat": stat, "value": continent_data[stat]}
        else:
            logger.warning(f"Invalid stat requested: {stat}")
            raise HTTPException(status_code=400, detail="Invalid statistic requested")

    logger.info(f"Successfully fetched data for {continent}")
    return {"continent": continent, "statistics": continent_data}
