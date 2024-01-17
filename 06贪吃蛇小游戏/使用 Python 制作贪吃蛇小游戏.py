""""""
"""
贪吃蛇游戏是一款经典的益智游戏，既简单又耐玩。回味童年经典，今天我们来一同学习贪吃蛇游戏的制作。

课题：《使用 Python 制作贪吃蛇小游戏》
课程时间：20:00-22:00
讲师：正心老师

开发环境：
    1. 解释器： Python 3.6.5 | Anaconda, Inc.
    2. 编辑器： pycharm 社区版

课程收获：Python游戏开发的核心知识点，程序员需要掌握的核心技能
    1. Python开发游戏的流程
    2. 如何用编程思维设计游戏
    3. PyGame 游戏模块的使用

有不懂的随时在讨论区问出来

做一个项目流程是什么？
    + 需求文档
    + 开发文档
pip install pygame
"""
import pygame
import random
import copy

# 初始化蛇移动的位置
move_up = False
move_down = True
move_left = False
move_right = False

# 1.1 游戏初始化
pygame.init()
clock = pygame.time.Clock()  # 设置游戏时钟，帧率 fps
pygame.display.set_caption('贪吃蛇小游戏')
screen = pygame.display.set_mode((500, 500))  # 设置窗口大小
# 随机生成一个整数
x = random.randint(10, 490)
y = random.randint(10, 490)
food_point = [x, y]

# 蛇 有很多个点
snake_list = [
    [10, 10]
]

# 1.2 启动游戏
running = True  # 死循环的开关
while running:
    # 1.3 设置帧率
    clock.tick(20)  # 一秒钟刷新20次

    # 1.4 设置窗口的背景
    screen.fill([255, 255, 255])  # 三原色

    food_rect = pygame.draw.circle(screen, [255, 0, 0], food_point, 15, 0)

    snake_rect = []  # 蛇的身子在页面的图像
    for pos in snake_list:  # 遍历蛇的每一个点
        snake_rect.append(pygame.draw.circle(screen, [255, 0, 0], pos, 5, 0))

        # 只要蛇碰到了食物就吃掉食物，并且重新生成新的食物
        if food_rect.collidepoint(pos):
            snake_list.append(food_point)
            # 重新生成食物
            food_point = [random.randint(10, 490), random.randint(10, 490)]
            food_rect = pygame.draw.circle(screen, [255, 0, 0], food_point, 15, 0)
            break
    # 移动蛇的位置

    # 先把身子走一下
    pos = len(snake_list) - 1
    while pos > 0:
        snake_list[pos] = copy.deepcopy(snake_list[pos - 1])
        pos -= 1
    # pos = 0  # 获取蛇的头部位置

    if move_right:
        # x += 10 就可以不断往右走
        snake_list[pos][0] += 10
        if snake_list[pos][0] > 500:
            snake_list[pos][0] = 0

    if move_left:
        # x += 10 就可以不断往右走
        snake_list[pos][0] -= 10
        if snake_list[pos][0] < 0:
            snake_list[pos][0] = 500

    if move_up:
        snake_list[pos][1] -= 10
        if snake_list[pos][1] < 0:
            snake_list[pos][1] = 500

    if move_down:
        snake_list[pos][1] += 10
        if snake_list[pos][1] > 500:
            snake_list[pos][1] = 0

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.KEYDOWN:
            # 判断上下左右的按键
            if event.key == pygame.K_UP:
                print('上')
                move_up = True
                move_down = False
                move_left = False
                move_right = False
            if event.key == pygame.K_DOWN:
                print('下')
                move_up = False
                move_down = True
                move_left = False
                move_right = False
            if event.key == pygame.K_LEFT:
                print('左')
                move_up = False
                move_down = False
                move_left = True
                move_right = False
            if event.key == pygame.K_RIGHT:
                print('右')
                move_up = False
                move_down = False
                move_left = False
                move_right = True

            # 你们平时敲的代码多吗

    # 蛇吃掉自己，结束游戏
    # 如果蛇吃掉了自己，就结束游戏
    head_rect = snake_rect[0]
    count = len(snake_rect)
    while count > 1:
        if head_rect.colliderect(snake_rect[count - 1]):
            running = False
        count -= 1

    # 将内容显示到界面
    pygame.display.update()
"""
爬虫 爬虫开发工程师
    自己开发app 没有数据 360脱裤bilibili
全栈、后端  全栈开发工程师
    
数据分析 数据分析开发工程师
    
量化、自动化
人工智能
    纯数

我自学出去找工作，学了两年
原有有很多
第一点：没有方向，学的不怎么系统，一定要做项目
第二点：没有以就业的目的进行学习，学习的强度很低
以就业的目的进行学习并不是只学习了之后是就业的，以就业的高目标高要求进行学习

就业的目的进行学习  会的东西很多才能做出东西

报名之后完成每天的上课、作业、案例、项目并且有不懂的随时找老师沟通
经过六个月的学习之后，才能找到工作
    
    牛顿：如果我看的比别人更远些，那是因为我站在巨人的肩膀上。
    
    上课时间： 一周三节 周135/246 一周六个小时  会有大量的案例以及作业
        学知识-写案例-写作业  答疑
        QQ 微信 远程协助
        
        最重要的：有人带，有不懂的随时问老师
    上班时间：
        下午一点到晚上十一点 
    
    学习：学历最好是高中以上 
    找工作：最好有个大专文凭
    

爬虫开发工程师 + 全栈开发工程师  5680
    + 5680 - 360 分期12期  443

花呗、京东白条、腾讯课堂教育分期
    腾讯课堂教育分期 腾讯课堂与百度合作的教育分期 只能用于学习
        最高支持24期分期  每月：221


公司不需要新人
    公司招人是来干活
    计算行业看技术
    

穷人认知
    
    你们知道为什么有些人一直很穷吗？
    
    作为一个穷人 一辈子只有一次投资自己的机会 甚至一次都没有
    所以在这个机会与风险如果高的情况下，你就会养成一下这些坏习惯
    
    + 怂 懒 拖延 患得患失
    
    + 怂 风险太大了 万一失败了岂不是万劫不复 所以恐惧
    + 懒 符合本能 
    + 拖延 因为怂 所以拖 因为恐惧 所以不敢投资 所以会把机会给浪费掉
分期










"""
