#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : main.py
@Time    : 28 1月,2023 10:33
@Author  : Shinruey Wann
"""
# 参考 https://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art


import matplotlib.pyplot as plt
import math
from PIL import Image
import numpy as np
import random
from tqdm import tqdm
from abc import abstractclassmethod, abstractmethod, abstractproperty, ABC
import sys
sys.setrecursionlimit(8192)

class TMA(ABC):

	def __init__(self, filename: str, DIM=1024):
		self.filename = filename
		self.DIM = DIM
		self.data = []
		plt.figure()

	def Gen(self):
		pbar=tqdm(range(self.DIM))
		for i in pbar:
			row = []
			for j in range(self.DIM):
				#print(i, j)
				r = self.RD(i, j, DIM=self.DIM) % 256
				g = self.GR(i, j, DIM=self.DIM) % 256
				b = self.BL(i, j, DIM=self.DIM) % 256
				c = (r, g, b)
				#print(c)
				row.append(c)
			#pbar.set_description(f"Now Calculating {str(i).rjust(4)},{str(j).rjust(4)} ")
			self.data.append(row)
		# del(row)
		self._pixel_write()
		plt.close()

	@abstractmethod
	def RD(self, i, j, DIM: int):
		pass

	@abstractmethod
	def GR(self, i, j, DIM: int):
		pass

	@abstractmethod
	def BL(self, i, j, DIM: int):
		pass

	def _pixel_write(self):
		data = np.array(self.data)
		data = np.asarray(data, np.uint8)
		# print(data)
		pic = Image.fromarray(data)
		pic.save(self.filename)


def main():
	print("正在绘图")


if __name__ == "__main__":
	main()
