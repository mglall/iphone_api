from model import Todo

# mongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://mglall:Mm0509329943@mg.m8axd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.TodoList
collection = database.iphone



async def fetch_one_iphone_by_model(model):
    iphones = []
    cursor = collection.find({"model":model})
    async for document in cursor:
        key, value = list(document)[5]
        if value not in iphones:
            iphones.append(value)
    return iphones


async def fetch_one_iphone(model, capacity, colors):
    document = await collection.find_one({"model":model,"capacity":capacity,"colors":colors})
    return document


async def fetch_all_iphones():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos 

async def create_iphone(iphone):
    document = iphone
    result = await collection.insert_one(document)
    return document

