from pydantic import BaseModel, Field, EmailStr
from typing import List


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "TEST post title",
                "content": "TEST post content"
            }
        }


class UserSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    fullname: str = Field(...)
    address1: str = Field(...)
    address2: str = Field(...)
    phoneNumber: str = Field(...)
    userCat: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "mmyu2090@gmail.com",
                "password": "SuperPowerfulPW",
                "fullname": "wooseok jang",
                "address1": "경북 구미시 대학로 17-9",
                "address2": "프라임 탑 201호",
                "phoneNumber": "010-0000-0000",
                "userCat": "점주"

            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "mmyu2090@gmail.com",
                "password": "SuperPowerfulPW"
            }
        }


class OrderMenuSchema(BaseModel):
    menuId: int = Field(...)
    menuName: str = Field(...)
    quantity: int = Field(...)
    price: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "menuId": 1,
                "menuName": "생수",
                "quantity": 4,
                "price": 4000
            }
        }


class ReceiptSchema(BaseModel):
    orderDate: str = Field(...)
    orderID: int = Field(...)
    seller: str = Field(...)
    sellerID: str = Field(...)
    sellerHP: str = Field(...)
    orderItem: List[OrderMenuSchema]

    class Config:
        schema_extra = {
            "example": {
                "orderDate": "21/04/23",
                "orderID": 1472583691,
                "seller": "주단태",
                "sellerID": "SELLERID",
                "sellerHP": "010-0000-0000",
                "orderItem": [
                    {
                        "menuId": 1,
                        "menuName": "생수",
                        "quantity": 4,
                        "price": 4000
                    },
                    {
                        "menuId": 2,
                        "menuName": "주단태빌리지 피규어",
                        "quantity": 1,
                        "price": 150000
                    }
                ]
            }
        }
