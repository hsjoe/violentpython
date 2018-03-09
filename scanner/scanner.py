# coding=utf-8

'''
Author:joe
Description: scanner of InterNet servers
1、模块 argparse(Generic Operation System Services)
2、获取命令行输入的目标地址和端口 ：Host，Port
3、-H host -p port
'''

import argparse
import socket

def get_tgthostandport():
    '''
    获取命令行输入的目标地址和端口

    Parameters:
        None
    Returns:
        (host, port)
    '''
    parser = argparse.ArgumentParser(description="Get Target Host and Port")
    parser.add_argument('-H', dest='Host', help='input host')
    parser.add_argument('-p', dest='Port', nargs='+', type=int, help='input port')
    # print(parser.parse_args())
    address = parser.parse_args()
    host = address.Host
    port = address.Port
    print(type(host))
    print(type(port))
    return [host, port]


def conn_scan(tg_host, tg_port):
    try:
        conn_stk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_stk.connect(tg_host, tg_port)
        conn_stk.send("volient python\r\n")
        reslut = conn_stk.recv(1000)
        print('[+]%d is open', tg_port)
        print('[+]' + str(reslut))
    except:
        print('[-]%d closed', tg_port)


    


'''
ADDRESS = get_tgthostandport()
print(ADDRESS)
'''

def port_scan():
    '''
    get the tgt_host_ip tgt_host_name
    Paramters: None
    Returns:
    '''
    tg_host = get_tgthostandport()[0]
    tg_port = get_tgthostandport()[1]

    try:
        tg_ip = socket.gethostbyname(tg_host)
    except:
        print('Can not get target ip by %s', tg_host)
        return
    
    print('scan reslut for %s', tg_ip)
    socket.setdefaulttimeout(1)

    for tgport in tg_port:
        print('sanning port %d:', tgport)
        conn_scan(tg_host, tgport)
    

port_scan()




