# coding=utf-8

'''
Author:joe
Description: scanner of InterNet servers
1、模块 argparse(Generic Operation System Services)
2、获取命令行输入的目标地址和端口 ：Host，Port
3、-H host -p port
4、多线程 加锁
'''

import argparse
import socket
import threading

SCREEN_LOCK = threading.Semaphore(value=1)

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
    #print(type(host))
    #print(type(port))
    return [host, port]



def conn_scan(tg_host, tg_port):
    '''
    connect host port
    Paremters:
        tg_host, tg_port
    Returns:
        None
    '''
    try:
        conn_stk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_stk.connect((tg_host, tg_port))
        conn_stk.send(b"hello/r/n")
        reslut = conn_stk.recv(100)
        SCREEN_LOCK.acquire()
        print('[+]%d tcp is open'%(tg_port))
        print('[+]' + str(reslut))
    except:
        SCREEN_LOCK.acquire()
        print('[-]%d tcp closed'%(tg_port))
    finally:
        SCREEN_LOCK.release()
        conn_stk.close()
   


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
        print('Can not get target ip by %s'%(tg_host))
        return

    try:
        tg_name = socket.gethostbyaddr(tg_ip)
        print(tg_name)
        print("\n scan reslut for:" + tg_name[0])    
    except:
        print('\n[+]scan reslut for: ' + tg_ip + ' : ' + tg_host)
    
    socket.setdefaulttimeout(10)

    for tgport in tg_port:
        print('sanning port :'+str(tgport))
        #conn_scan(tg_host, int(tgport))
        t = threading.Thread(target=conn_scan, args=(tg_host,int(tgport)))
        t.start()

# port_scan()

if __name__ == '__main__':
    port_scan()



