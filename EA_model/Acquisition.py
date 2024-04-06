import pandas as pd
import MetaTrader5 as mt5

def getdata(symblo: str, start_pos: int, count: int) -> pd.DataFrame:
    """
    获取数据
    :param symblo: 标的代码
    :param start_pos: 初始柱形图索引
    :param count: 要接收的柱形图数
    :return: numpy数据柱形图
    """
    rates = mt5.copy_rates_from_pos(symblo, mt5.TIMEFRAME_D1, start_pos, count)
    """
    # rates = getdata("Etc/UTC", symbol)
    rates = getdata(symbol, 0, 30)
    # 从所获得的数据创建DataFrame
    rates_frame = pd.DataFrame(rates)
    # 将时间（以秒为单位）转换为日期时间格式
    # rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
    # ATR 用于衡量价格波动性的指标
    rates_frame['ATR5'] = talib.ATR(rates_frame['high'], rates_frame['low'], rates_frame['close'], timeperiod=5)
    """
    return rates