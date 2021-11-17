from pydantic import BaseModel 

class Todo(BaseModel):
    brand: str
    model: str
    announced: str
    size_height_width_deth: str
    weight_g: str
    colors: str
    capacity: str 
    ram: str 
    approx_price_USD: str 
    img_url: str 
    stock: str 