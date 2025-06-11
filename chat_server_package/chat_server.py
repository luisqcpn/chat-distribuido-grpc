import grpc
from concurrent import futures
import threading
import time
import sys
import os

# Garante que o diretório 'proto' está no caminho de importação
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
proto_dir = os.path.join(parent_dir, 'proto')
sys.path.insert(0, proto_dir)

import chat_pb2
import chat_pb2_grpc



# Lista global para manter todos os streams conectados
clients = []
lock = threading.Lock()


class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def JoinChat(self, request, context):
        print(f"[INFO] Usuário entrou: {request.username}")
        return chat_pb2.JoinResponse(welcome_message=f"Bem-vindo, {request.username}!")

    def Chat(self, request_iterator, context):
        client_queue = []

        # Adiciona o cliente à lista global
        with lock:
            clients.append(client_queue)

        try:
            def receive_messages():
                for chat_msg in request_iterator:
                    print(f"[RECEBIDO] {chat_msg.username}: {chat_msg.message}")
                    # Distribui para todos os outros clientes
                    with lock:
                        for c in clients:
                            if c != client_queue:
                                c.append(chat_msg)

            threading.Thread(target=receive_messages, daemon=True).start()

            while True:
                if client_queue:
                    with lock:
                        msg = client_queue.pop(0)
                    yield msg
                else:
                    time.sleep(0.1)

        except Exception as e:
            print(f"[ERRO] Conexão com cliente encerrada: {e}")

        finally:
            with lock:
                if client_queue in clients:
                    clients.remove(client_queue)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("[INFO] Servidor gRPC de Chat iniciado na porta 50051.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
