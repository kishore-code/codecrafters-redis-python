import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept() # wait for client
    connection, _ = server_socket.accept()
    ## Single PING
    # data = connection.recv(1024)  # receive data (this will be the PING command)
    # print(f"Received: {data.decode().strip()}")  # log received data (for debugging)
    # connection.sendall(b"+PONG\r\n")  # send response

    '''
    Simple strings - https://redis.io/docs/latest/develop/reference/protocol-spec/#simple-strings
    Simple strings are encoded as a plus (+) character, followed by a string.
    The string mustn't contain a CR (\r) or LF (\n) character and is terminated by CRLF (i.e., \r\n).
    Simple strings transmit short, non-binary strings with minimal overhead.
    For example, many Redis commands reply with just "OK" on success. The encoding of this Simple String is the following 5 bytes:
    +OK\r\n
    '''

    ## Respoinding to multiple PINGs
    while True:
        request: bytes = connection.recv(1024)
        data: str = request.decode()

        if "ping" in data.lower():
            print(f"Received: {data}")
            # Respond with PONG
            connection.send(b"+PONG\r\n")
        
        if not data:
            print("No data received, closing connection.")
            break


    connection.close()  # close the connection




if __name__ == "__main__":
    main()
