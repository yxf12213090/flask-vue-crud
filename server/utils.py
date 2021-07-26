import baostock as bs
import pandas as pd

class baostockApi():
    def __init__(self):
        #### 登陆系统 ####
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

    # def __del__(self):
    #     # 登出系统
    #     bs.logout()


    def query_sz50_stocks(self):
        # 获取上证50成分股
        rs = bs.query_sz50_stocks()
        print('query_sz50 error_code:' + rs.error_code)
        print('query_sz50  error_msg:' + rs.error_msg)

        # 打印结果集
        sz50_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            sz50_stocks.append(rs.get_row_data())
        result = pd.DataFrame(sz50_stocks, columns=rs.fields)
        # 结果集输出到csv文件
        return result


    def query_hs300_stocks(self):
        # 获取沪深300成分股
        rs = bs.query_hs300_stocks()
        print('query_hs300 error_code:' + rs.error_code)
        print('query_hs300  error_msg:' + rs.error_msg)

        # 打印结果集
        hs300_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            hs300_stocks.append(rs.get_row_data())
        result = pd.DataFrame(hs300_stocks, columns=rs.fields)
        # 结果集输出到csv文件
        return result


    def query_zz500_stocks(self):
        # 获取中证500成分股
        rs = bs.query_zz500_stocks()
        print('query_zz500 error_code:' + rs.error_code)
        print('query_zz500  error_msg:' + rs.error_msg)

        # 打印结果集
        zz500_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            zz500_stocks.append(rs.get_row_data())
        result = pd.DataFrame(zz500_stocks, columns=rs.fields)
        # 结果集输出到csv文件
        return result

    def query_history_k_data_plus(self, code, start_date, end_date, frequency, fields):
        # http://finance.sina.com.cn/money/fund/fundzmt/2019-12-31/doc-iihnzahk1179182.shtml
        # 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
        # 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
        # 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
        # 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
        # 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
        # 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
        # 成长指数，例如：sz.399376 小盘成长 等；
        # 价值指数，例如：sh.000029 180价值 等；
        # 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；

        # 详细指标参数，参见“历史行情指标参数”章节；“周月线”参数与“日线”参数不同。
        # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
        rs = bs.query_history_k_data_plus(code=code, fields=fields, start_date=start_date, end_date=end_date,
                                          frequency=frequency, adjustflag="2")
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        # print(data_list[0])
        result = pd.DataFrame(data_list, columns=rs.fields)
        # 结果集输出到csv文件
        # print(result)
        return result


    def query_stock_basic(self, code):
        # 获取证券基本资料
        # rs = bs.query_stock_basic(code="sh.000300")
        rs = False
        if not code:
            rs = bs.query_stock_basic()
        else:
            rs = bs.query_stock_basic(code=code)  # 支持模糊查询
        print('query_stock_basic respond error_code:' + rs.error_code)
        print('query_stock_basic respond  error_msg:' + rs.error_msg)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        # 结果集输出到csv文件
        # print(result)
        return result


    def query_stock_k_data(self):
        rs = bs.query_stock_basic()
        code_list = []
        while (rs.error_code == '0') & rs.next():
            code_list.append(rs.get_row_data()[0])
        print(code_list)
        print(len(code_list))
        code_list = code_list[1000:1003]
        code_info = []
        for code in code_list:
            rs = bs.query_stock_basic(code=code)
            while (rs.error_code == '0') & rs.next():
                code_info.append(rs.get_row_data())
            print(code_info[0])
        c = code_info[1]

        data = self.query_history_k_data_plus(c[0], '1994-04-01', '1995-06-01', 'd', 'pctChg')
        print(data)



if __name__ == '__main__':
    b = baostockApi()
    b.query_stock_k_data()
    bs.logout()
    # fields = "date,code,open,high,low,close,preclose,volume,amount,pctChg"
    # code = "sh.000001"
    # start_date = '2017-01-01'
    # end_date = '2017-06-30'
    # b.query_history_k_data_plus(code, start_date, end_date, 'd', fields)
    # b.query_stock_basic()
