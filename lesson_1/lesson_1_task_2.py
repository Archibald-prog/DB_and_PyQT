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

orig_lst = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

def get_ip_list(ip_lst):
    res_list = []
    for ip in ip_lst:
        if '-' in ip:
            start_ip, stop_ip = ip.split('-')
            if '.' not in stop_ip:
                stop_ip = '.'.join(start_ip.split('.')[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                res_list.append(str(ipaddress.ip_address(ip)))
        else:
            res_list.append(str(ipaddress.ip_address(ip)))
    return res_list


def host_range_ping(ip_list):
    for ip in ip_list:
        status = ping_ip(ip)
        if status:
            print(f'Адрес {ip} пингуется')
        else:
            print(f'Адрес {ip} не пингуется')


if __name__ == '__main__':
    host_range_ping(get_ip_list(orig_lst))