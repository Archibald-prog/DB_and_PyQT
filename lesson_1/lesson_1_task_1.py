import subprocess
import ipaddress
import platform


def ping_ip(ip):
    if platform.system().lower() == 'windows':
        cmd = ['ping', '-n', '1', ip]
    else:
        cmd = ['ping', '-c', '1', ip]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        encoding='utf-8'
    )
    if result.returncode == 0:
        return True
    else:
        return False


def host_ping(orig_lst):
    ip_lst = [str(ipaddress.ip_address(ip)) for ip in orig_lst]
    for ip in ip_lst:
        status = ping_ip(ip)
        if status:
            print(f'Узел {ip} доступен')
        else:
            print(f'Узел {ip} не доступен')


if __name__ == '__main__':
    orig_lst = ['8.8.8.8', '192.168.1.5', '192.168.0.251', '10.1.1.1']
    host_ping(orig_lst)
