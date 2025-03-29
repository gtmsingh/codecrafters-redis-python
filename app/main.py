import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    try:
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    except ValueError:
        # If the reuse port is not supported
        server_socket = socket.create_server(("localhost", 6379))

    conn, _ = server_socket.accept()  # wait for client

    conn.sendall(b"+PONG\r\n")  # send a PONG response


if __name__ == "__main__":
    main()
