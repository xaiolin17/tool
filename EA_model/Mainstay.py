import pandas as pd
import MetaTrader5 as mt5
from Operate import Buy

def transaction(data: pd.DataFrame):
    """
    param: rates_frame: 含有指标的数据
    根据条件执行买卖操作
    :return:
    """
    # 订单数
    orders_total = mt5.positions_total()
    print("--->Buy orders_total", orders_total)
    # 买操作
    Buy()
    """是否请求成功 比对操作后的订单数是否变化"""
    # 查看buy后的订单数
    orders_total_current = mt5.positions_total()
    print("Buy--->orders_total_current", orders_total_current)
    # 直到买入成功(最多尝试12次)
    repeat = 0
    while orders_total == orders_total_current:
        if repeat > 12:
            print("---Buy失败---")
            break
        print("上一次失败，将重新Buy -> ", repeat)
        # 买操作
        Buy()
        orders_total_current = mt5.positions_total()
        print("--->Buy---> orders_total_current", orders_total_current)
        repeat += 1

    # 获取交易品种的订单列表
    positions_get = mt5.positions_get()
    df_positions_get = pd.DataFrame(list(positions_get), columns=positions_get[0]._asdict().keys())
    df_positions_get['time'] = pd.to_datetime(df_positions_get['time'], unit='s')
    df_positions_get.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    print('******当前订单列表******')
    print(df_positions_get)
