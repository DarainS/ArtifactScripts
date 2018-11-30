#!/usr/bin/env python
# coding:utf-8

import random
import time

default_win_rate = 0.5

total_cal_num = 10 ** 6

rand = random.Random()
rand.seed(time.time())


class VirtualDraft(object):
	cost = 1
	value_dict = {
		1: 0,
		0: 0,
		2: 0,
		3: 1,
		4: 3,
		5: 5
	}


class RealDraft(object):
	cost = 2
	value_dict = {
		1: 0,
		0: 0,
		2: 0,
		3: 4,
		4: 6,
		5: 8
	}


def random_win_result(win_rate=default_win_rate):
	defeat_num = 0
	win_num = 0
	while win_num < 5 and defeat_num < 2:
		win = rand.random() <= win_rate
		if win:
			win_num += 1
		else:
			defeat_num += 1
	return win_num, defeat_num


def show_win_count_rate(win_rate=default_win_rate, draft=VirtualDraft()):
	total_cost = draft.cost * total_cal_num
	to_deal_num = total_cal_num
	win_num_statics = [0] * 6
	print('胜率: {}'.format(win_rate))
	cur_i = 0
	while cur_i < to_deal_num:
		win_num, defeat_num = random_win_result(win_rate)
		win_num_statics[win_num] += 1
		if defeat_num == 0:
			to_deal_num += 1
		cur_i += 1
	for i in range(6):
		print('{}胜概率： {}'.format(i, win_num_statics[i] / to_deal_num))
	total_value = .0
	for i in range(3, 6):
		total_value += draft.value_dict[i] * win_num_statics[i]
	print('三胜以下概率为{}'.format((win_num_statics[0] + win_num_statics[1] + win_num_statics[2]) / to_deal_num))

	print('胜率 {} 时平均每轮期望收益为{}'.format(win_rate, (total_value-total_cost) / total_cal_num ))


if __name__ == '__main__':
	show_win_count_rate(0.60, draft=VirtualDraft())
