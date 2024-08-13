## Some comments:
1. add typing on parameters and return types
2. add exception handling when reading/writing/removing files in FileService (OSError might be thrown - though unlikely)
3. Why does the "download file" route does not return the file content (or download it localy) ?

## Some suggestions:
Since this project is small, its good that you kept it simple and concise!
If it was bigger project, it would be nice to add these:

1. Pydantic models for the Request Body and Request Response (its good for validation, and also for the swagger)
2. Dependency injection - in fastapi, its done by using "Depends" (from fastapi import Depends). This can help decoupling & testing
3. Async functions where async operations may be beneficial, like in file_upload & file_download
4. Handle cases where the file being downloaded / uploaded is very large (split to chunks)
5. Put the services into a services/ directory, put the routers into a routers/ directory
