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
    * It's cleaner to omit the `return None` statements when the return value is `Optional`
    * The variable `DOWNLOAD_PATH` is hard coded, making the class less flexible in the future. Think about receiving it in the constructor like the `base_dir`, or as a param of the method
    * When you use try/except, put inside it only the sepcific parts of the function which might raise an error -> you can move the `os.path.join()` before the try except

3. Inside `routers.py`:
    * In the `download_file` function, you save the return value in a `content` variable, even though it returns a `file_path`. Also, if you dont use the variable, dont save it
    * You should use the status.py module for status codes (`from fastapi import status`, status.HTTP_200_OK)
    * In the `upload_file` function, you read of all of the file to a `content` variable, so you cannot upload it in chunks (problematic if it is a huge file)
  
5. Inside `config.py`:
   * Put inside it the config of the ftp server & fastapi
     
6. rename `services/services.py` and `routers/routers.py` to be more specific, for example: `services/file_service.py`
