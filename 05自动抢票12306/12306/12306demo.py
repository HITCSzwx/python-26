"""
[课程内容]: Python实现12306查票以及自动抢票

[授课老师]: 青灯教育-自游  [上课时间]: 20:05

[环境使用]:
    Python 3.8
    Pycharm

[模块使用]:
    requests  >>> pip install requests
    prettytable  >>> pip install prettytable
    selenium
    json

课前素材:
    city.json 文件
    Chromedriver驱动安装文档
    selenium 使用教程

先听一下歌 等一下后面进来的同学, 20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加落落老师微信: xinlian_00
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找落落老师领取录播, 然后再写代码
    3. 不要进进出出, 早退不仅没有录播, 你还会思路中断
---------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：http://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：http://pypi.hustunique.com/
                山东理工大学：http://pypi.sdutlinux.org/
                豆瓣：http://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

        - 失败三: cmd里面显示已经安装过了, 或者安装成功了, 但是在pycharm里面还是无法导入
            解决方法: 可能安装了多个python版本 (anaconda 或者 python 安装一个即可) 卸载一个就好
                    或者你pycharm里面python解释器没有设置好
---------------------------------------------------------------------------------------------------
如何配置pycharm里面的python解释器?
    1. 选择file(文件) >>> setting(设置) >>> Project(项目) >>> python interpreter(python解释器)
    2. 点击齿轮, 选择add
    3. 添加python安装路径
---------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1. 选择file(文件) >>> setting(设置) >>> Plugins(插件)
    2. 点击 Marketplace  输入想要安装的插件名字 比如:翻译插件 输入 translation / 汉化插件 输入 Chinese
    3. 选择相应的插件点击 install(安装) 即可
    4. 安装成功之后 是会弹出 重启pycharm的选项 点击确定, 重启即可生效
---------------------------------------------------------------------------------------------------

零基础同学 0
有基础同学 1

查票: 使用爬虫相关的内容:

爬虫最基本思路流程:

一. 数据来源分析
    车票信息数据内容
    1. F12或者鼠标右键点击检查选择network  然后刷新一下网页数据, 让我们的数据包重新加载出来
    2. 通过搜索数据, 找到相应数据包, 然后查看请求url地址 请求方式, 以及请求头参数

二. 代码实现的过程
    1. 发送请求, 对于刚刚分析得到url地址发送请求
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取我们想要数据内容
    4. 格式化输出效果
"""
import requests  # 数据请求模块 第三方模块 需要安装 pip install requests
import prettytable as pt  # 表格格式的输出  第三方模块 需要安装 pip install prettytable
import json

# import 回家的诱惑

f = open("city.json", encoding="utf-8")
txt = f.read()
json_data = json.loads(txt)  # 转成字典数据类型
from_station = input("请输入你出发的城市: ")
to_station = input("请输入你目的城市: ")
# print(txt)
date = input("请输入你要出发的日期(格式: 2022-05-04):")
# print(json_data[from_station])
# print(json_data[to_station])
"""
发送请求, 对于刚刚分析得到url地址发送请求
    python爬虫发送请求: 模拟浏览器对于url地址发送请求
请求头: 伪装python代码, 让它伪装一个浏览器去发送请求
    字典的数据类型, 构建完整键值对形式
    User-Agent: 用户代理 浏览器基本身份标识
    Cookie: 用户信息, 常用于检测是否登陆账号
当你请求数据之后, 虽然返回 <Response [200]> 但是不一定得到你想要数据内容 得到的数据不是你想要, 说明你被反爬了
"""
url = f"https://kyfw.12306.cn/otn/leftTicket/queryE?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_station]}&leftTicketDTO.to_station={json_data[to_station]}&purpose_codes=ADULT"
headers = {
    "Cookie": "_uab_collina=170541395918089063870135; JSESSIONID=545158467B335BECECA555D7FF49DEFD; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=937951498.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=401080586.50210.0000; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u5CB3%u9633%2CYYQ; _jc_save_toDate=2024-01-16; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2024-01-30",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
# 通过requests数据请求模块里面get请求方法, 对于url地址发送请求, 并且携带上headers请求头伪装, 最后用response变量接收返回数据
response = requests.get(url=url, headers=headers)
# 2. 获取数据
# print(response.json())  #  <Response [200]>  请求成功 返回响应对象  不是完整json数据格式
# 3. 解析数据, 提取我们想要数据内容
tb = pt.PrettyTable()
tb.field_names = [
    "序号",
    "车次",
    "出发时间",
    "到达时间",
    "耗时",
    "特等座",
    "一等",
    "二等",
    "软卧",
    "硬卧",
    "硬座",
    "无座",
]
page = 1
for index in response.json()["data"]["result"]:  # 把列表里面元素 一个一个提取出来, 用for循环遍历
    # index.split('|') # 字符串分割, 以|进行分割, 返回列表
    info = index.split("|")
    num = info[3]  # 车次
    start_time = info[8]  # 出发时间
    end_time = info[9]  # 到达时间
    use_time = info[10]  # 耗时
    topGrade = info[32]  # 特等座
    first_class = info[31]  # 一等
    second_class = info[30]  # 二等
    soft_sleeper = info[23]  # 软卧
    hard_sleeper = info[28]  # 硬卧
    hard_seat = info[29]  # 硬座
    no_seat = info[26]  # 无座
    dit = {
        "车次": num,
        "出发时间": start_time,
        "到达时间": end_time,
        "耗时": use_time,
        "特等座": topGrade,
        "一等": first_class,
        "二等": second_class,
        "软卧": soft_sleeper,
        "硬卧": hard_sleeper,
        "硬座": hard_seat,
        "无座": no_seat,
    }
    tb.add_row(
        [
            page,
            num,
            start_time,
            end_time,
            use_time,
            topGrade,
            first_class,
            second_class,
            soft_sleeper,
            hard_sleeper,
            hard_seat,
            no_seat,
        ]
    )
    page += 1
print(tb)
word = input("请输入你想要购买车票: ")
# 回家的诱惑.get_train(int(word), from_station, to_station, date)
