from pydantic import BaseModel

class Voo(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    airline: str
    aircraft_type: str
    available_seats: int