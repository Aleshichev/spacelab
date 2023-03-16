import httpx
from models import Post, User
from tortoise import Tortoise, run_async


async def download(data):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://gorest.co.in/public/v2/'

    async with httpx.AsyncClient() as client:

        response = await client.get(url=f"{url}{data}?page=1&per_page=100", headers=headers)
        
        if response.status_code == 200:
            data_list = response.json()
            if data == 'posts':
                await create_post(data_list)
            else:
                await create_user(data_list)
     
            return data_list
        else:
            print(response.status_code)


async def connect_db():
    
    await Tortoise.init(
      db_url='sqlite://sql_app.db',
      modules={'models': ['models']},)

    await Tortoise.generate_schemas()


async def create_post(data_list):
    
    await connect_db()

    for post in data_list:
        try: 
            await Post.create(id=post['id'], user_id=post['user_id'], title=post['title'], body=post['body'])
        except Exception as e:
            print(f'ошибка id {e}')


async def create_user(data_list):

    await connect_db()
    
    for user in data_list:
        await User.create(id=user['id'], name=user['name'], email=user['email'], gender=user['gender'], status=user['status']) 


if __name__ == '__main__':

    run_async(download(data='users'))
    run_async(download(data='posts'))
