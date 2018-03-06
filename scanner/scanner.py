'''
Author:joe
Description: scanner of InterNet servers
1、模块 argparse
2、获取命令行输入的目标地址和端口 ：Host，Port
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






