import MetaTrader5 as mt5
from Setting import symbol

def Buy(magic: int, price: float, sl: float, tp: float):
    """
    :param magic: 交易 ID (幻数)
    :param price: 价格
    :param sl: 订单止损价位点位
    :param tp: 订单盈利价位点位
    :return:
    """
    try:
        # 获取净值
        account_info_dict = mt5.account_info()._asdict()
        equity = account_info_dict['equity']
        lot_eq = round(equity / 100000, 2)
        lot_res = lot_eq if lot_eq > 0.01 else 0.01

        lot = lot_res                                  # 交易量
        # point = mt5.symbol_info(symbol).point       # 小数位数
        # price = mt5.symbol_info_tick(symbol).ask    # 价格
        deviation = 136                             # 允许价格偏差
        # print("point", point, "price", price)
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": magic,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        # 发送交易请求
        result = mt5.order_send(request)
        """
        # 显示有关程序端设置和状态的信息
        terminal_info_dict = mt5.terminal_info()._asdict()
        # 将词典转换为DataFrame和print
        # df_terminal_info = pd.DataFrame(list(terminal_info_dict.items()), columns=['property', 'value'])
        print("***程序端状态:")
        print(terminal_info_dict)
        # 发送交易请求
        result = mt5.order_send(request)
        # 检查执行结果
        print("---1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("！！！！2. order_send failed, retcode={}".format(result.retcode))
            # 请求词典结果并逐个元素显示
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
        else:
            print("---2. order_send done, ", result)
            print("   opened position with POSITION_TICKET={}".format(result.order))
        """
    except Exception as e:
        print(e)