# main.py

from typing import Annotated

from app.models.users import UserModel
from app.schemas.users import UserCreateRequest, UserSearchRequest, UserUpdateRequest
from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

UserModel.create_dummy()  # API 테스트를 위한 더미를 생성하는 메서드 입니다.


@app.post("/users")
async def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return user.id


@app.get("/users")
async def get_all_user():
    # 일부러 매개변수 받아보자. 무슨일이 생기나 ->  422 error
    result = UserModel.all()
    if not result:
        raise HTTPException(status_code=404)
    return result


@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., description="유저정보 가져오기", gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    return {"id": user.id, "username": user.username, "age": user.age, "gender": user.gender}


@app.patch("/users/{user_id}")
async def update_user(data: UserUpdateRequest, user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    user.update(**data.model_dump())
    return {"id": user.id, "username": user.username, "age": user.age, "gender": user.gender}


@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(gt=0)):
    user = UserModel.get(id=user_id)
    if user is None:
        raise HTTPException(status_code=404)
    user.delete()
    return {"detail": f"User: {user_id}, Successfully Deleted."}


@app.get("/users/search")
async def search_users(query_params: Annotated[UserSearchRequest, Query()]):
    valid_query = {key: value for key, value in query_params.model_dump().items() if value is not None}
    filtered_users = UserModel.filter(**valid_query)
    if not filtered_users:
        raise HTTPException(status_code=404)
    return filtered_users


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
