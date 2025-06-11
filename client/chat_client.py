import grpc
import threading
import time
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
proto_dir = os.path.join(parent_dir, 'proto')
sys.path.insert(0, proto_dir)

import chat_pb2
import chat_pb2_grpc



def listen_for_messages(stream):
    try:
        for message in stream:
            print(f"\n[{message.username}]: {message.message}")
    except grpc.RpcError as e:
        print(f"[ERRO] Falha ao escutar mensagens: {e}")


def main():
    channel = grpc.insecure_channel('44.210.116.70:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    username = input("Digite seu nome de usuário: ")
    response = stub.JoinChat(chat_pb2.JoinRequest(username=username))
    print(response.welcome_message)

    def message_generator():
        while True:
            msg = input()
            if msg.lower() == 'sair':
                break
            yield chat_pb2.ChatMessage(username=username, message=msg)

    # Cria o stream bidirecional
    responses = stub.Chat(message_generator())

    # Thread para escutar mensagens recebidas
    thread = threading.Thread(target=listen_for_messages, args=(responses,), daemon=True)
    thread.start()

    # Aguarda a thread principal (de envio) encerrar
    while thread.is_alive():
        time.sleep(0.1)


if __name__ == '__main__':
    main()
