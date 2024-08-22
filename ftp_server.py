from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from utils import utility_functions

config = utility_functions.load_config()

logger = utility_functions.create_logger()


def start_ftp_server() -> None:
    authorizer = DummyAuthorizer()
    authorizer.add_user(config['USER'], config['PASSWORD'], config['BASE_DIR'], perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    ftp_server = FTPServer(("0.0.0.0", 21), handler)
    logger.info("Starting FTP server...")
    ftp_server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()
