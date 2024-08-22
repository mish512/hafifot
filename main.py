import uvicorn
from utils import utility_functions

config = utility_functions.load_config()

if __name__ == "__main__":
    uvicorn.run("main:app", host=config['HOST'], port=config['PORT'], reload=True)
