#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : demo.py
@Time    : 28 1月,2023 11:12
@Author  : Shinruey Wann
"""
import random
import threading

import numpy

from gen import *
from decimal import *

getcontext().prec = 12


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
		a = 0;
		b = 0;
		c = 0;
		d = 0;
		n = 0
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
		a = 0;
		b = 0;
		c = 0;
		d = 0;
		n = 0
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
		a = 0;
		b = 0;
		c = 0;
		d = 0;
		n = 0
		while True:
			c = a * a
			d = b * b
			n += 1
			b = 2 * a * b + j * 8e-9 - .645411
			a = c - d + i * 8e-9 + .356888
			if not (c + d < 4 and n < 880):
				break
		return 255 * math.pow((n - 80) / 800, 0.5)


r = lambda n: random.randint(0, n+1)
c1 = numpy.ones((1024, 1024))*-1
c2 = numpy.ones((1024, 1024))*-1
c3 = numpy.ones((1024, 1024))*-1

class Random1(TMA):
	def RD(self, i, j, DIM: int):
		global c1
		if c1[i][j] < 0:
			if (not r(299)) or i>=DIM or j>=DIM:
				c1[i][j] = r(256)
			else:
				c1[i][j] = self.RD((i + r(8) +1020) % 1024, (j + r(8) +1020) % 1024, DIM)
		return c1[i][j]

	def GR(self, i, j, DIM: int):
		global c2
		if c2[i][j] < 0:
			if (not r(299)) or i>=DIM or j>=DIM:
				c2[i][j] = r(256)
			else:
				c2[i][j] = self.GR((i + r(8) +1020) % 1024, (j + r(8) +1020) % 1024, DIM)
		return c2[i][j]

	def BL(self, i, j, DIM: int):
		global c3
		if c3[i][j] < 0:
			if (not r(299)) or i>=DIM or j>=DIM:
				c3[i][j] = r(256)
			else:
				c3[i][j] = self.BL((i + r(8) +1020) % 1024, (j + r(8) +1020) % 1024, DIM)
		return c3[i][j]


class Random2(TMA):
	def RD(self, i, j, DIM: int):
		global c1
		if c1[i][j] < 0:
			if (not r(499)) or i>=DIM or j>=DIM:
				c1[i][j] = r(256)
			else:
				c1[i][j] = self.RD((i + r(5)) % 1024, (j + r(5)) % 1024, DIM)
		return c1[i][j]

	def GR(self, i, j, DIM: int):
		global c2
		if c2[i][j] < 0:
			if (not r(499)) or i>=DIM or j>=DIM:
				c2[i][j] = r(256)
			else:
				c2[i][j] = self.GR((i + r(5)) % 1024, (j + r(5)) % 1024, DIM)
		return c2[i][j]

	def BL(self, i, j, DIM: int):
		global c3
		if c3[i][j] < 0:
			if (not r(499)) or i>=DIM or j>=DIM:
				c3[i][j] = r(256)
			else:
				c3[i][j] = self.BL((i + r(5)) % 1024, (j + r(5)) % 1024, DIM)
		return c3[i][j]


class Random3(TMA):
	def RD(self, i, j, DIM: int):
		global c1
		if c1[i][j] < 0:
			if (not r(499)) or i>=DIM or j>=DIM:
				c1[i][j] = r(256)
			else:
				c1[i][j] = self.RD((i + r(1)) % 1024, (j + r(1)) % 1024, DIM)
		return c1[i][j]

	def GR(self, i, j, DIM: int):
		global c2
		if c2[i][j] < 0:
			if (not r(499)) or i>=DIM or j>=DIM:
				c2[i][j] = r(256)
			else:
				c2[i][j] = self.GR((i + r(1)) % 1024, (j + r(1)) % 1024, DIM)
		return c2[i][j]

	def BL(self, i, j, DIM: int):
		global c3
		if c3[i][j] < 0:
			if (not r(499)) or i>=DIM or j>=DIM:
				c3[i][j] = r(256)
			else:
				c3[i][j] = self.BL((i + r(1)) % 1024, (j + r(1)) % 1024, DIM)
		return c3[i][j]


if __name__ == '__main__':
	# demo=Demo(r'demo.png')
	# demo.Gen()
	# test1 = Test1(r'test1.png')
	# test1.Gen()
	random1 = Random1(r'random1.png')
	random1.Gen()
	# random2 = Random2(r'random2.png')
	# random2.Gen()
	# random3 = Random3(r'random3.png')
	# random3.Gen()
# mandelbrot = Mandelbrot(r'mandelbrot_1024.png')
# mandelbrot.Gen()
