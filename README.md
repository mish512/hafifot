The project looks really good! Since there is no strict convention on how to structure a fastapi project, I would recommend looking up "fastapi project structure example" on google to take some inspiration (for example, fastapi official documentation: [Bigger Applications Documentation](https://fastapi.tiangolo.com/tutorial/bigger-applications/#include-an-apirouter-in-another), good structured github project: [Real World Project Example](https://github.com/nsidnev/fastapi-realworld-example-app/tree/master/app/))

Some points to consider:

1. `Routers` & `App` Relationship: Its good practice to create separate router objects, and then include them in the main app.
For example:

```python
# EXAMPLE: src/routers/files_router.py

from fastapi import APIRouter

router = APIRouter(prefix="/files")

@router.get("/")
async def get_file():
    ...
```

```python
# EXAMPLE: src/main.py

from fastapi import FastAPI
from src.routers.file_router import router as file_router

app = FastAPI()

app.include_router(file_router)
```

2. Inside `services.py`:
    * Would be nice to have the buffer size as a parameter with default value in the `download_file` method
    * It's cleaner to emit the `return None` statements when the return value is `Optional`

3. Inside `routers.py`:
    * In the `download_file` function, why you don't return the `content` variable or save it locally as a file ?
    
