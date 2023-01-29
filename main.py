#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : demo.py
@Time    : 28 1月,2023 11:12
@Author  : Shinruey Wann
"""
from gen import *
from decimal import *

getcontext().prec=12

class Demo(TMA):
	def __init__(self, filename: str, DIM=1024):
		super().__init__(filename, DIM)

	def RD(self, i: int, j: int, DIM: int):
		return 255 * math.cos(math.atan2(j - 512, i - 512) / 2) ** 2

	def GR(self, i: int, j: int, DIM: int):
		return 255 * math.cos(math.atan2(j - 512, i - 512) / 2 - 2 * math.acos(-1) / 3) ** 2

	def BL(self, i: int, j: int, DIM: int):
		return 255 * math.cos(math.atan2(j - 512, i - 512) / 2 + 2 * math.acos(-1) / 3) ** 2


class Test1(TMA):
	def __init__(self, filename: str, DIM=1024):
		super().__init__(filename, DIM)

	def RD(self, i: int, j: int, DIM: int):
		return i / 4

	def GR(self, i: int, j: int, DIM: int):
		return j / 4

	def BL(self, i: int, j: int, DIM: int):
		return (i + j) / 4


class Mandelbrot(TMA):
	def __init__(self, filename: str, DIM=1024):
		super().__init__(filename, DIM)

	def RD(self, i: int, j: int, DIM: int):
		a = 0;b = 0;c = 0;d = 0;n = 0
		while True:
			c = a * a
			d = b * b
			n += 1
			b = 2 * a * b + j * 8e-9 - .645411
			a = c - d + i * 8e-9 + .356888
			if not (c + d < 4 and n < 880):
				break
		return 255 * math.pow((n - 80) / 800, 3)

	def GR(self, i: int, j: int, DIM: int):
		a = 0;b = 0;c = 0;d = 0;n = 0
		while True:
			c = a * a
			d = b * b
			n += 1
			b = 2 * a * b + j * 8e-9 - .645411
			a = c - d + i * 8e-9 + .356888
			if not (c + d < 4 and n < 880):
				break
		return 255 * math.pow((n - 80) / 800, 0.7)

	def BL(self, i: int, j: int, DIM: int):
		a = 0;b = 0;c = 0;d = 0;n = 0
		while True:
			c = a * a
			d = b * b
			n += 1
			b = 2 * a * b + j * 8e-9 - .645411
			a = c - d + i * 8e-9 + .356888
			if not (c + d < 4 and n < 880):
				break
		return 255 * math.pow((n - 80) / 800, 0.5)


if __name__ == '__main__':
	# demo=Demo(r'demo.png')
	# demo.Gen()
	# test1 = Test1(r'test1.png')
	# test1.Gen()
	mandelbrot = Mandelbrot(r'mandelbrot_1024.png')
	mandelbrot.Gen()
	mandelbrot.DIM=2048; mandelbrot.filename=r'mandelbrot_2048'
	mandelbrot.Gen()
