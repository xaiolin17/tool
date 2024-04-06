import talib
import pandas as pd

def creatFeature(rates_frame: pd.DataFrame) -> pd.DataFrame:
    """
    计算方法
    param: rates_frame: DataFrame
    return: DataFrame
    """
    """
    指标计算
    """
    # ATR 用于衡量价格波动性的指标
    rates_frame['ATR5'] = talib.ATR(rates_frame['high'], rates_frame['low'], rates_frame['close'], timeperiod=5)
    rates_frame['ATR10'] = talib.ATR(rates_frame['high'], rates_frame['low'], rates_frame['close'], timeperiod=10)
    rates_frame['ATR14'] = talib.ATR(rates_frame['high'], rates_frame['low'], rates_frame['close'], timeperiod=14)

    # MACD = 快线 - 慢线
    # Signal = MACD的移动平均线
    # Hist = MACD - Signal
    rates_frame['MACD'], rates_frame['SIGNAL'], rates_frame['HIST'] = talib.MACD(rates_frame['close'], fastperiod=6,
                                                                                 slowperiod=13, signalperiod=5)

    # 简单移动平均线 SMA
    rates_frame['SMA8'] = talib.SMA(rates_frame['close'], timeperiod=8)
    rates_frame['SMA30'] = talib.SMA(rates_frame['close'], timeperiod=30)

    # STOCH  用于确定价格超买或超卖的指标 使用fastk_period参数设置快速K线周期为5，slowk_period参数设置慢速K线周期为3，slowd_period参数设置慢速D线周期为3
    rates_frame['SLOWK'], rates_frame['SLOWD'] = talib.STOCH(rates_frame['high'], rates_frame['low'],
                                                             rates_frame['close'], fastk_period=21, slowk_period=3,
                                                             slowd_period=3)

    """
    模式识别
    """
    # -100表示出现了较强的2Crows形态，0表示没有出现2Crows形态，100表示出现了较强的反向2Crows形态

    # CDL3STARSINSOUTH 南方三星 下跌趋势反转，股价上升
    # 开盘前3秒进入多单
    rates_frame["CDL3STARSINSOUTH"] = talib.CDL3STARSINSOUTH(rates_frame['open'], rates_frame['high'],
                                                             rates_frame['low'], rates_frame['close'])

    # CDLABANDONEDBABY 弃婴 三日K线模式 第二日价格跳空且收十字星，预示趋势反转，发生在顶部下跌，底部上涨
    # 开盘前3秒进入空单，挂空(h+l/2)-3.6
    rates_frame["CDLABANDONEDBABY"] = talib.CDLABANDONEDBABY(rates_frame['open'], rates_frame['high'],
                                                             rates_frame['low'], rates_frame['close'])

    # CDLCONCEALBABYSWALL 藏婴吞没 预示着底部反转
    # 开盘前3秒进入多单 挂多(h+l/2)+3.6
    rates_frame["CDLCONCEALBABYSWALL"] = talib.CDLCONCEALBABYSWALL(rates_frame['open'], rates_frame['high'],
                                                                   rates_frame['low'], rates_frame['close'])

    # CDLDRAGONFLYDOJI 蜻蜓十字/T形十字 开盘后价格一路走低，之后收复，收盘价与开盘价相同
    # 开盘前3秒进入多单
    rates_frame["CDLDRAGONFLYDOJI"] = talib.CDLDRAGONFLYDOJI(rates_frame['open'], rates_frame['high'],
                                                             rates_frame['low'], rates_frame['close'])

    # CDLGAPSIDESIDEWHITE 向上/下跳空并列阳线 上升趋势向上跳空，下跌趋势向下跳空,第一日与第二日有相同开盘价，实体长度差不多，则趋势持续
    # 挂多单(h+l/2)+3.6
    rates_frame["CDLGAPSIDESIDEWHITE"] = talib.CDLGAPSIDESIDEWHITE(rates_frame['open'], rates_frame['high'],
                                                                   rates_frame['low'], rates_frame['close'])

    # CDLGRAVESTONEDOJI 墓碑十字/倒T十字 开盘价与收盘价相同，上影线长，无下影线。
    # 挂空单(h+l/2)-3.6
    rates_frame["CDLGRAVESTONEDOJI"] = talib.CDLGRAVESTONEDOJI(rates_frame['open'], rates_frame['high'],
                                                               rates_frame['low'], rates_frame['close'])

    # CDLHAMMER  锤头 实体较短，无上影线，下影线大于实体长度两倍，处于下跌趋势底部，预示反转
    # 开盘进入多单 挂多单(h+l/2)+3.6
    rates_frame["CDLHAMMER"] = talib.CDLHAMMER(rates_frame['open'], rates_frame['high'], rates_frame['low'],
                                               rates_frame['close'])

    # CDLHANGINGMAN  上吊线  形状与锤子类似，处于上升趋势的顶部
    # 开盘进入空单 挂空单(h+l/2)-3.6
    rates_frame["CDLHANGINGMAN"] = talib.CDLHANGINGMAN(rates_frame['open'], rates_frame['high'], rates_frame['low'],
                                                       rates_frame['close'])

    # CDLHIGHWAVE  风高浪大线  三日K线模式，具有极长的上/下影线与短的实体，预示着趋势反转
    # 开盘进入多单 挂多单(h+l/2)+3.6
    rates_frame["CDLHIGHWAVE"] = talib.CDLHIGHWAVE(rates_frame['open'], rates_frame['high'], rates_frame['low'],
                                                   rates_frame['close'])

    # CDLINVERTEDHAMMER 倒锤头 一日K线模式，上影线较长，长度为实体2倍以上，无下影线
    # 开盘进入空单 挂空单(h+l/2)-3.6
    rates_frame["CDLINVERTEDHAMMER"] = talib.CDLINVERTEDHAMMER(rates_frame['open'], rates_frame['high'],
                                                               rates_frame['low'], rates_frame['close'])

    # CDLLADDERBOTTOM  梯底   五日K线模式，下跌趋势中，前三日阴线，开盘价与收盘价皆低于前一日开盘、收盘价，
    #                           第四日倒锤头，第五日开盘价高于前一日开盘价，阳线，收盘价高于前几日价格振幅，预示着底部反转
    # 开盘进入多单 挂多单(h+l/2)+3.6
    rates_frame["CDLLADDERBOTTOM"] = talib.CDLLADDERBOTTOM(rates_frame['open'], rates_frame['high'], rates_frame['low'],
                                                           rates_frame['close'])

    # CDLSHOOTINGSTAR  射击之星 一日K线模式，上影线至少为实体长度两倍，没有下影线，预示着下跌
    # 开盘进入空单 挂空单(h+l/2)-3.6
    rates_frame["CDLSHOOTINGSTAR"] = talib.CDLSHOOTINGSTAR(rates_frame['open'], rates_frame['high'], rates_frame['low'],
                                                           rates_frame['close'])

    # 剔除因为计算而造成的NULL
    rates_frame = rates_frame.dropna(axis=0)
    # 重置索引
    rates_frame = rates_frame.reset_index(drop=True)
    print("\n****计算最终shape: ", rates_frame.shape)
    return rates_frame

# """
# 价格转换
# """
# # AVGPRICE 平均价格函数
# rates_frame['AVGPRICE'] = talib.stream_AVGPRICE(rates_frame['open'], rates_frame['high'], rates_frame['low'], rates_frame['close'])
#
# # MEDPRICE 中位数价格
# rates_frame['MEDPRICE'] = talib.stream_MEDPRICE(rates_frame['high'], rates_frame['low'])
#
# # TYPPRICE 代表性价格
# rates_frame['TYPPRICE'] = talib.stream_TYPPRICE(rates_frame['high'], rates_frame['low'], rates_frame['close'])
#
# # WCLPRICE 代表性价格
# rates_frame['WCLPRICE'] = talib.stream_WCLPRICE(rates_frame['high'], rates_frame['low'], rates_frame['close'])
    """
    变化计算
    """

    """
    周期指标
    """

    """
    统计函数
    """
    """
    # CORREL 皮尔逊相关系数 度量两个变量X和Y之间的相关（线性相关）
    rates_frame["CORREL"] = talib.CORREL(rates_frame['high'], rates_frame['low'], timeperiod=30)

    # LINEARREG 确定两种或两种以上变量间相互依赖的定量关系的一种统计分析方法
    rates_frame["LINEARREG"] = talib.LINEARREG(rates_frame['close'], timeperiod=14)

    # LINEARREG_ANGLE 来确定价格的角度变化
    rates_frame["LINEARREG_ANGLE"] = talib.LINEARREG_ANGLE(rates_frame['close'], timeperiod=14)

    # LINEARREG_INTERCEPT 线性回归截距
    rates_frame["LINEARREG_INTERCEPT"] = talib.LINEARREG_INTERCEPT(rates_frame['close'], timeperiod=14)

    # LINEARREG_SLOPE 线性回归斜率指标
    rates_frame["LINEARREG_SLOPE"] = talib.LINEARREG_SLOPE(rates_frame['close'], timeperiod=14)

    # STDDEV 标准偏差 种量度数据分布的分散程度之标准，用以衡量数据值偏离算术平均值的程度
    rates_frame["STDDEV"] = talib.STDDEV(rates_frame['close'], timeperiod=5, nbdev=1)

    # TSF 时间序列预测 历史引伸预测法
    rates_frame["TSF"] = talib.TSF(rates_frame['close'], timeperiod=14)

    # VAR 方差
    rates_frame["VAR"] = talib.VAR(rates_frame['close'], timeperiod=5, nbdev=1)
    """