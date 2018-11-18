#!/usr/bin/env python
#coding:utf-8
import random

default_win_rate = 0.6

total_cal_num = 10**6

rand = random.Random()

value_dict = {
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    4: 3,
    5: 5
}

def random_win_result(win_rate=default_win_rate):
    defeat_num = 0
    win_num = 0
    while win_num<5 and defeat_num<2:
        win = rand.random()<=win_rate
        if win:
            win_num+=1
        else:
            defeat_num+=1
    return win_num, defeat_num


def show_win_count_rate(win_rate=default_win_rate):
    win_num_statics = [0] * 6
    print('胜率: {}'.format(win_rate))
    for i in range(total_cal_num):
        win_num, _ = random_win_result(win_rate)
        win_num_statics[win_num] += 1
    for i in range(6):
        print('{}胜概率： {}'.format(i,win_num_statics[i]/total_cal_num))
    expect_value = .0
    for i in range(3, 6):
        expect_value+=value_dict[i]*win_num_statics[i]
    print('三胜以下概率为{}'.format((win_num_statics[0]+win_num_statics[1]+win_num_statics[2])/total_cal_num))

    print('胜率 {} 时平均每轮期望收益为{}'.format(win_rate,expect_value/total_cal_num))

if __name__ == '__main__':
    show_win_count_rate()