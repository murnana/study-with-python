import numpy
import matplotlib.pylab as plt

"""
ステップ関数
:param numpy.array: x
"""
def step_function(x):
    y = x > 0   # 配列Xの各要素を比較した結果の配列をYに入れる
    return y.astype(numpy.int)  # Yの各要素booleanをintがたに変換



"""
シグモイド関数
:param numpy.array: x
"""
def sigmoid(x):
    return 1 / (1 + numpy.exp(-x))  # exp = 指数関数のこと


if __name__ == "__main__":
    x = numpy.arange(-5.0, 5.0, 0.1)    # 0.1刻みで、-5.0 ~ 5.0の配列
    y1 = step_function(x)
    y2 = sigmoid(x)
    plt.plot(x, y1, linestyle = '--', label = 'step')
    plt.plot(x, y2, label = 'sigmoid')
    plt.ylim(-0.1, 1.1) # y軸の範囲
    plt.show()
