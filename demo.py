#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : demo.py
@Time    : 28 1月,2023 11:12
@Author  : Shinruey Wann
"""
from gen import *
class Demo(TMA):
	def __init__(self, filename: str, DIM=1024):
		super().__init__(filename, DIM)

	def RD(self, i: int, j: int, DIM: int):
		return 255 * math.cos(math.atan2(j - 512, i - 512) / 2) ** 2

	def GR(self, i: int, j: int, DIM: int):
		return 255 * math.cos(math.atan2(j - 512, i - 512) / 2 - 2 * math.acos(-1) / 3) ** 2

	def BL(self, i: int, j: int, DIM: int):
		return 255 * math.cos(math.atan2(j - 512, i - 512) / 2 + 2 * math.acos(-1) / 3) ** 2


if __name__ == '__main__':
	demo = Demo(r'demo.png')
	demo.Gen()
