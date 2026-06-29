import select
import socket
from collections.abc import Generator


def nb_socket(host: str, port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)

    try:
        sock.connect((host, port))
    except BlockingIOError:
        pass  # connect in progress — check with nb_is_connected()
    except OSError as e:
        if e.winerror == 10035 or e.errno in (115, 114):  # in progress
            pass
        else:
            raise
    
    return sock


def nb_is_connected(sock: socket.socket) -> bool:
    _, writable, errors = select.select([], [sock], [sock], 0)
    if errors:
        err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
        raise OSError(err, "connect failed")
    if not writable:
        return False

    err = sock.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
    if err != 0:
        raise OSError(err, "connect failed")

    return True


def nb_connect(host: str, port: int) -> Generator[None, None, socket.socket]:
    sock = nb_socket(host, port)
    while not nb_is_connected(sock):
        yield None
    return sock


def nb_send(
    sock: socket.socket,
    data: bytes
) -> Generator[None, None, None]:
    sent: int = 0
    while sent < len(data):
        try:
            sent += sock.send(data[sent:])
        except BlockingIOError:
            yield None
        except OSError as e:
            if e.winerror == 10035 or e.errno in (115, 114):  # in progress
                yield None
            raise


def nb_recv(
    sock: socket.socket
) -> Generator[None, None, bytes]:
    buffer = b""
    bufsize = 4096

    while True: 
        try:
            chunk = sock.recv(bufsize)
            if not chunk:
                return buffer
            buffer += chunk
        except BlockingIOError:
            yield None
        except OSError as e:
            if e.winerror == 10035 or e.errno in (115, 114):  # in progress
                yield None
            raise

