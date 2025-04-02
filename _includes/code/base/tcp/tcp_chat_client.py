import socket
import threading

class TcpClient:
    def __init__(self, message, ip, port):
        self.message = message
        self.ip = ip
        self.port = port
        self.client = None
        self.running = False
        self.reconnect_attempts = 3
        self.lock = threading.Lock()
        self.initialize_connection()

    def initialize_connection(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) 
            self.client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) 
            self.client.connect((self.ip, self.port))
            self.client.send(self.message.encode())
            print("连接成功")
        except Exception as e:
            print(f"初始化失败: {e}")
            self.auto_reconnect()

    def auto_reconnect(self):
        for attempt in range(self.reconnect_attempts):
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.ip, self.port))
                print("重连成功")
                return True
            except Exception as e:
                print(f"第{attempt+1}次重连失败: {e}")
        self.running = False
        return False

    def receive(self):
        self.running = True
        while self.running:
            try:
                data = self.client.recv(4096)
                if not data: 
                    print("连接已关闭")
                    break
                msg = data.decode()
                print()
                print(f"收到消息: {msg}")
                if "服务器关闭" in msg:
                    self.graceful_shutdown()
            except (ConnectionResetError, socket.timeout) as e:
                print(f"接收异常: {e}")
                if not self.auto_reconnect():
                    break

    def send_to(self):
        while self.running:
            try:
                message = input("输入消息 (exit退出): ")
                if message.lower() == "exit":
                    self.graceful_shutdown()
                    break
                with self.lock:
                    self.client.send(message.encode())
            except (BrokenPipeError, OSError) as e:
                print(f"发送失败: {e}")
                self.auto_reconnect()

    def graceful_shutdown(self):
        print("正在安全关闭...")
        self.running = False
        with self.lock:
            if self.client:
                self.client.send("客户端关闭".encode())
                self.client.close()
        print("连接已关闭")


if __name__ == "__main__":
    ip = input("IP地址: ")
    port = int(input("端口号: "))
    client = TcpClient("Hello Server", ip, port)
    send_thread = threading.Thread(target=client.send_to)
    recv_thread = threading.Thread(target=client.receive)
    send_thread.start()
    recv_thread.start()
    send_thread.join()
    recv_thread.join()
