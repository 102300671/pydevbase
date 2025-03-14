import socket
import threading


class TcpServer:
    def __init__(self, message, port):
        self.message = message
        self.port = port
        self.server = None
        self.client = None
        self.addr = None
        self.lock = threading.Lock()
        self.running = False
        self.initialize_server()

    def initialize_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", self.port))
        self.server.listen()
        print("[TCP 服务器] 等待初始连接...")
        self.running = True
        self.accept_connection()

    def accept_connection(self):
        try:
            with self.lock:
                self.client, self.addr = self.server.accept()
            print(f"[TCP服务器] 已连接: {self.addr}")
            self.client.send(self.message.encode())
        except Exception as e:
            print(f"[TCP服务器] 接受连接时出错: {e}")
            self.running = False

    def send_to(self):
        while self.running:
            try:
                message = input("[TCP服务器] 请输入消息 (输入exit退出): ")
                if message.lower() == "exit":
                    print("[TCP服务器] 正在关闭连接...")
                    with self.lock:
                        self.client.send("TCP服务器即将关闭".encode())
                        self.shutdown()
                    break
                    
                with self.lock:
                    if self.client:
                        self.client.send(message.encode())
            except (EOFError, KeyboardInterrupt):
                break
            except Exception as e:
                print(f"[TCP服务器] 发送失败: {e}")
                self.reconnect_client()

    def receive(self):
        while self.running:
            try:
                with self.lock:
                    data = self.client.recv(1024) if self.client else None
                if not data:
                    print("[TCP服务器] 客户端断开连接")
                    self.reconnect_client()
                    continue
                    
                message = data.decode()
                print(f"[TCP客户端] 收到消息: {message}")
                if message == "TCP客户端即将关闭":
                    self.reconnect_client()

            except ConnectionResetError:
                print("[TCP服务器] 连接被客户端重置")
                self.reconnect_client()
            except Exception as e:
                print(f"[TCP服务器] 接收错误: {e}")
                self.running = False

    def reconnect_client(self):
        try:
            with self.lock:
                if self.client:
                    self.client.close()
                print("[TCP服务器] 等待客户端重新连接...")
                self.client, self.addr = self.server.accept()
                print(f"[TCP服务器] 重新连接成功: {self.addr}")
                self.client.send(self.message.encode())
        except Exception as e:
            print(f"[TCP服务器] 重新连接失败: {e}")
            self.running = False

    def shutdown(self):
        self.running = False
        with self.lock:
            if self.client:
                self.client.close()
            if self.server:
                self.server.close()
        print("[TCP服务器] 服务已完全关闭")


if __name__ == "__main__":
    port = int(input("请输入服务器端口: "))
    server = TcpServer("Hello Client", port)
    
    if not server.running:
        exit()

    sender = threading.Thread(target=server.send_to)
    receiver = threading.Thread(target=server.receive)

    sender.start()
    receiver.start()

    sender.join()
    receiver.join()
