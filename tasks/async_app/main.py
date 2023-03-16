# from data import download
from typing import List

from fastapi import FastAPI, HTTPException
from database.models import Post, User, User_Pydantic, UserIn_Pydantic
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(

    title="Message App"
)


class Status(BaseModel):
    message: str


@app.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


@app.get(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@app.get(
    "/user/posts/{user_id}", responses={404: {"model": HTTPNotFoundError}}
)
async def get_user_posts(user_id: int):
    
    user = await User.get(id=user_id)
    posts = await Post.filter(user=user)
    if posts == []:
        return {"message": f"У пользователя {user.name} нет постов"}
    
    return {
            "User_name": user.name,
            "posts": posts,
            }


# @app.get(
#     "/user/posts/{user_id}", response_model=User_Pydantic_List, responses={404: {"model": HTTPNotFoundError}}
# )
# async def get_user_post(user_id: int):

#     user = await User.get(id=user_id)
#     return await User_Pydantic_List.from_queryset(user.posts.all())


@app.post("/users", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@app.put(
    "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@app.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")


register_tortoise(
    app,
    db_url='sqlite://sql_app.db',
    modules={'models': ['database.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
