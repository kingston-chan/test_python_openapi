from src.food import Food, get_food_v1
from fastapi import FastAPI
from pydantic import BaseModel

class Error(BaseModel):
  message: str
  code: int

tags_metadata = [
  {
    "name": "Food"
  }
]

APP = FastAPI(openapi_tags=tags_metadata)

@APP.get(
  "/food/",
  tags=["Food"],
  response_model=Food,
  responses={
    200: {
      "model": Food,
      "description": "Food requested by ID",
      "content": {
        "application/json": {
          "example": {
            "food": "pizza"
          }
        }
      },
    },
    400: {
      "model": Error,
      "description": "Invalid ID supplied",
      "content": {
        "application/json": {
          "example": {
            "code": 400,
            "message": "Invalid ID supplied"
          }
        }
      },
    },
  }
)
async def get_food(food_id: int):
    return get_food_v1(food_id)