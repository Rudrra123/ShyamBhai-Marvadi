from pydantic import BaseModel
from typing import List

class Row(BaseModel):
    item: str
    no: float
    length: float
    breadth: float
    quantity: float
    price: float
    total_price: float

class Header(BaseModel):
    name: str
    mobile: str
    address: str
    work_name: str

class FormRequest(BaseModel):
    header: Header
    rows: List[Row]
    total: float
