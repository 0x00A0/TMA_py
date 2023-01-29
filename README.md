# TMA_py

---

The python version of [Tweetable Mathematical Art](https://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art)

Usage: 
1. import `gen.py`
2. inherit class `TMA`
3. implements `RD(i, j, DIM)`, `GR(i, j, DIM)`, `BL(i, j, DIM)`, to specify the RGB value of the generated image at position `(i, j)`, the size of the image is `DIM*DIM`
4. instantiate then call `Gen()`, the generated image would be saved to `filename`

---

[Tweetable Mathematical Art](https://codegolf.stackexchange.com/questions/35569/tweetable-mathematical-art) 的Python实现

用法:

1. 导入`gen.py`
2. 继承`TMA`类
3. 实现`RD(i, j, DIM)`, `GR(i, j, DIM)`, `BL(i, j, DIM)`三个抽象方法, 用于指定生成图在`(i, j)`位置的RGB值, 生成图的尺寸是`DIM*DIM`
4. 实例化并调用`Gen()`方法, 生成的图像会被保存到`filename`指定的位置

Example/示例:
```python
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
```
The generated image of codes above would be:
![Demo image](demo.png)