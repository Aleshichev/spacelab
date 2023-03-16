from tortoise import fields, models
from tortoise.contrib.pydantic import (pydantic_model_creator,
                                       pydantic_queryset_creator)


class User(models.Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(50)
    email = fields.CharField(max_length=100, unique=True)
    gender = fields.CharField(50)
    status = fields.CharField(max_length=100)
    posts = fields.ReverseRelation['Post']


class Post(models.Model):

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='posts')
    title = fields.CharField(max_length=250)
    body = fields.TextField()


User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
User_Pydantic_List = pydantic_queryset_creator(User)

Post_Pydantic = pydantic_model_creator(Post, name='Post')
