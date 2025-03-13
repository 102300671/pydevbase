import socket
import threading
class Tcp_server():
    def __init__(self,message):
        self.message = message
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0",8023))
        self.server.listen()
        print("[TCP 服务器] 等待连接...")
        self.client, addr = self.server.accept()
        print(f"[TCP服务器] 已连接:{addr}")
        self.client.send(self.message.encode())
    def  send_to(self):
        while True:
            message = input("[TCP服务器] 请输入消息:")
            if message == "exit":
                self.client.send("TCP服务器即将关闭".encode())
                self.server.close()
                print("[TCP服务器] 服务器已关闭")
                break
            else:
                print("[TCP服务器] 正在发送消息")
                self.client.send(message.encode())
    def receive(self):
        while True:
            data = self.client.recv(1024)
            message = data.decode()
            print(f"[TCP客户端] 收到消息:{message}")
            if message == "TCP客户端即将关闭":
                print("[TCP服务器] 挂起，等待客户端重新连接...")
                self.client.close()
                self.client, addr = self.server.accept()
                print(f"[TCP服务器] 已重新连接:{addr}")

tcp  = Tcp_server("Hello Client")
send_thread = threading.Thread(target=tcp.send_to)
receive_thread = threading.Thread(target=tcp.receive)
send_thread.start()
receive_thread.start()
send_thread.join()
receive_thread.join()