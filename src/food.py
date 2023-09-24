from fastapi.responses import JSONResponse
from pydantic import BaseModel

all_food = {
  1: 'pizza',
  2: 'cheese burger'
}

class Food(BaseModel):
  food: str

def get_food_v1(food_id):
  try:
    return {'food': all_food[int(food_id)]}
  except KeyError:
    return JSONResponse(status_code=400, content={"code": 400, "message": "Invalid ID supplied."})