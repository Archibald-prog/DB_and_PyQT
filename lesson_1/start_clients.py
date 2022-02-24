import os
import subprocess

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(CURRENT_DIR, '../messenger', 'client.py')


def listen_clients(port, ip, clients_num):
    args = ['python', filepath, '-p', port, '-a', ip]
    for client in range(clients_num):
        subprocess.run(args, stdout=subprocess.PIPE, shell=True)


if __name__ == '__main__':
    clients_number = int(input('Enter the number of clients: '))
    listen_clients('8888', '127.0.0.1', clients_number)
