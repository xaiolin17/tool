import pandas as pd
import MetaTrader5 as mt5
from Acquisition import getdata
from Mainstay import transaction
from GitFeature import creatFeature
from Setting import login, password, server, symbol, initialize_path

pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display

if __name__ == "__main__":
    """
    初始化
    """
    # 建立与MetaTrader 5程序端的连接
    if not mt5.initialize(path=initialize_path, login=login, password=password, server=server):
        print("initialize() failed, error code =", mt5.last_error())
        quit()

    # 准备买入请求结构
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        mt5.shutdown()
        quit()

    # 如果市场报价中没有此交易品种，请添加
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol, True):
            print("symbol_select({}}) failed, exit", symbol)
            mt5.shutdown()
            quit()

    """
    运行主体
    """
    while True:
        # 读取实时数据
        data = getdata(symbol, 0, 150)
        # 计算
        must = creatFeature(data)
        # 根据数据进行操作
        transaction(must)

    # 断开与MetaTrader 5程序端的连接
    mt5.shutdown()