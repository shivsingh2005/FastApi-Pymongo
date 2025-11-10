from fastapi import APIRouter
from models.todo import Todo
from database import todo_collection
from Schema.schema import list_serial
from bson import ObjectId

router = APIRouter()

# GET all todos
@router.get("/")
async def get_todo():
    todos = list_serial(todo_collection.find())
    return todos

# POST a new todo
@router.post("/")
async def post_todo(todo: Todo):
    todo_dict = dict(todo)
    result = todo_collection.insert_one(todo_dict)
    # Return the inserted todo with its MongoDB _id
    return {"id": str(result.inserted_id), "message": "Todo added successfully"}

