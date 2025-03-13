import socket
import threading


def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))
    server.listen()
    print("[TCP 服务器] 等待连接...")
    client, addr = server.accept()
    print(f"[TCP服务器] 已连接:{addr}")
    message = "Hello Client"
    print("[TCP服务器] 正在发送消息")
    client.send(message.encode())
    client.close()
    server.close()


def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))
    data = client.recv(1024)
    print(f"[TCP客户端] 收到消息:{data.decode()}")
    client.close()


def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 12345))
    print("[UDP服务器] 等待数据")
    data, addr = server.recvfrom(1024)
    print(f"[UDP服务器] 已收到{addr}的数据")
    num = int.from_bytes(data, byteorder='big')
    response = (num + 1).to_bytes(4, byteorder='big')
    print("[UDP服务器] 正在响应")
    server.sendto(response, addr)
    server.close()


def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = int(input("[UDP客户端] 请输入一个整数:"))
    client.sendto(data.to_bytes(4, byteorder='big'), ("127.0.0.1", 12345))
    response, _ = client.recvfrom(1024)
    print(f"[UDP客户端] 收到响应:{int.from_bytes(response, 'big')}")
    client.close()


if __name__ == "__main__":
    for _ in range(2):
        choice = int(input("选择协议(TCP(连接):1,UDP(加一):2):"))
        if choice == 1:
            server_thread = threading.Thread(target=tcp_server)
            server_thread.start()
            threading.Event().wait(0.5)
            client_thread = threading.Thread(target=tcp_client)
            client_thread.start()
            server_thread.join()
            client_thread.join()
        elif choice == 2:
            server_thread = threading.Thread(target=udp_server)
            server_thread.start()
            threading.Event().wait(0.5)
            udp_client()
            server_thread.join()
