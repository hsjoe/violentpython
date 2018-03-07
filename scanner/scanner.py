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
        (Host, Port)
    '''
    parser = argparse.ArgumentParser(description="Get Target Host and Port")
    parser.add_argument('-H', dest='Host', help='get host')
    parser.add_argument('-p', dest='Port', type=int, help='get port')
    # print(parser.parse_args())
    address = parser.parse_args()
    host = address.Host
    port = address.Port
    return (host, port)


ADDRESS = get_tgthostandport()

print(ADDRESS)
