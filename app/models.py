from pydantic import BaseModel

class PriceSimInput(BaseModel):
    percent_increase: float
