from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Temporary database
users = []


# Home route - Serves UI
@app.get("/")
def home():
    return FileResponse("index.html")


# CREATE - POST
@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return {
        "message": "User created successfully",
        "data": user
    }


# READ - GET
@app.get("/users")
def get_users():
    return {
        "users": users
    }


# UPDATE - PUT
@app.put("/users/{id}")
def update_user(id: int, user: dict):
    if id >= len(users):
        return {
            "message": "User not found"
        }

    users[id] = user

    return {
        "message": "User updated successfully",
        "data": user
    }


# DELETE - DELETE
@app.delete("/users/{id}")
def delete_user(id: int):
    if id >= len(users):
        return {
            "message": "User not found"
        }

    deleted_user = users.pop(id)

    return {
        "message": "User deleted successfully",
        "data": deleted_user
    }