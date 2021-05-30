from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.model import PostSchema, UserSchema, UserLoginSchema, ReceiptSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer


posts = []  # DB 대신 쓰는 배열
users = []  # DB 대신 쓰는 배열
receipts = []  # DB 대신 쓰는 배열

app = FastAPI()

origins = ["*", "210.91.148.210", "localhost:3000",
           "localhost:8000", "localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "WORKING !!!"}


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)  # 여기서는 데이터를 그저 배열에 저장할뿐 나중에 DB에 해쉬 해서 저장할것
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Login Failed"
    }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())  # 여기서는 데이터를 그저 배열에 저장할뿐 나중에 DB에 해쉬 해서 저장할것
    return {
        "data": "post added."
    }


@app.post("/receipt", dependencies=[Depends(JWTBearer())], tags=["receipt"])
async def add_receipt(myreceipt: ReceiptSchema = Body(...)) -> dict:
    # 여기서는 데이터를 그저 배열에 저장할뿐 나중에 DB에 해쉬 해서 저장할것
    receipts.append(myreceipt.dict())
    return {
        "data": "receipt added."
    }


@app.get("/receipt", dependencies=[Depends(JWTBearer())], tags=["receipt"])
async def get_receipt() -> dict:
    return {
        "data": receipts
    }


@app.get("/receipt/{orderID}", dependencies=[Depends(JWTBearer())], tags=["receipt"])
async def get_single_receipt(orderID: int) -> dict:
    for receipt in receipts:
        if receipt["orderID"] == orderID:
            return {
                "data": receipt
            }
    return {
        "data": "there is no recipt has \"orderID\" like that"
    }
