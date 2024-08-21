from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from config import BASE_DIR, USER, PASSWORD


def start_ftp_server() -> None:
    authorizer = DummyAuthorizer()
    authorizer.add_user(USER, PASSWORD, BASE_DIR, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    ftp_server = FTPServer(("0.0.0.0", 21), handler)
    print("Starting FTP server...")
    ftp_server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()
