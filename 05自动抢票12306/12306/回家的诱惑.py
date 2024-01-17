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

selenium 模拟人的行为去操作浏览器 人怎么去通过12306买票? 怎么就用代码去写

想学好python 想跟着老师学的 扣 1

如果你想要去就业, 跟着系统课程: 自动化办公课程
    1. 核心编程 + 高级开发 + 爬虫 + (数据分析) 可以找爬虫工程师工作 100-1000左右比较多
    2. 核心编程 + 高级开发 + 数据分析 + 人工智能 可以找数据分析师工作 100-1000左右比较多
    3. 核心编程 + 高级开发 + 全栈开发 (前端 + 后端) 可以找开发工程师工作 1000+以上

开发经验 是你用python开发项目案例所积累的经验  要求你可以直接做东西
工作经验 是你从事相关工作的经验 要求你又可以直接做项目, 做东西, 又熟悉业务流程


网站开发外包价格最高, 你可能接一个外包学费就回来了
爬虫 数据分析 开发工作, 都可以从事, 薪资待遇也相对而言也会高一些

全部学完 7 个月时间  并不是一天24小时都在学习  可以直接找工作 8-15K左右
三个月可以接外包赚钱 月收入 1000-3000左右

全套课程学费 7880 可以直接在腾讯课堂支付, 也可以通过分期免息学习 你可以加清风老师微信: pythonmiss
分18期免息 每个月 400出头学费

VIP授课方式, 服务.....
    - 在线直播授课 每周三节课 每周135或者246 晚上20:00-22:00 直播授课
    - 课后高清录播回放 源码资料 课件 都会提供并且永久观看权限
    - 老师解答辅导 文字 语音 远程操作 解答辅导

16年从事在线教育行业
"""
import time
from selenium import webdriver
from password import account, Password
from selenium.webdriver.common.keys import Keys


def get_train(num, from_station, to_station, date):
    # 如果你驱动放在你python环境安装目录里面 可以不用指定路径
    # driver = webdriver.Chrome(executable_path='驱动路径')
    driver = webdriver.Chrome()
    # 绕过selenium检测
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})

    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    driver.find_element_by_css_selector('#J-userName').send_keys(account)  # 输入账号
    driver.find_element_by_css_selector('#J-password').send_keys(Password)  # 输入密码
    driver.find_element_by_css_selector('#J-login').click()  # 点击登陆
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('.modal-ft .btn ').click()
    driver.find_element_by_css_selector('#link_for_ticket').click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('#fromStationText').clear()
    driver.find_element_by_css_selector('#fromStationText').click()
    driver.find_element_by_css_selector('#fromStationText').send_keys(from_station)
    driver.find_element_by_css_selector('#fromStationText').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('#toStationText').clear()
    driver.find_element_by_css_selector('#toStationText').click()
    driver.find_element_by_css_selector('#toStationText').send_keys(to_station)
    driver.find_element_by_css_selector('#toStationText').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_css_selector('#train_date').clear()
    driver.find_element_by_css_selector('#train_date').click()
    driver.find_element_by_css_selector('#train_date').send_keys(date)
    driver.find_element_by_css_selector('#train_date').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('#query_ticket').click()
    if num%2 == 0:
        driver.find_element_by_css_selector(f'#queryLeftTable tr:nth-child({num+1}) .btn72').click()
    else:
        driver.find_element_by_css_selector(f'#queryLeftTable tr:nth-child({num}) .btn72').click()
    driver.find_element_by_css_selector('#normalPassenger_0').click()
    driver.find_element_by_css_selector('#submitOrder_id').click()
    driver.find_element_by_css_selector('#erdeng1 > ul:nth-child(4) li:nth-child(2) a').click()
