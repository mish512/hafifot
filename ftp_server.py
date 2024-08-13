from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

BASE_DIR = "./files"


def start_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", BASE_DIR, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    ftp_server = FTPServer(("0.0.0.0", 21), handler)
    print("Starting FTP server...")
    ftp_server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()
