'''
Author:joe
Description: scanner of InterNet servers
1、模块 argparse(Generic Operation System Services)
2、获取命令行输入的目标地址和端口 ：Host，Port
3、-H host -p port
'''

import argparse

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


ADDRESS = get_tgthostandport()
print(ADDRESS)

'''def port_scan():
    
    get the tgt_host_ip tgt_host_name
    Paramters: None
    Returns:
    
    

def conn_scan():
    pass

'''