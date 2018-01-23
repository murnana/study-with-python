# 
# 二つの1次元配列からすべての組み合わせの2次元配列を作る
# https://funmatu.wordpress.com/2017/09/07/2%E3%81%A4%E3%81%AEnumpy-ndarray%E3%81%8B%E3%82%89%E7%9B%B4%E7%A9%8D%E3%81%AAnumpy-ndarray%E3%82%92%E4%BD%9C%E3%82%8B/
# を参考に。
import numpy

# 0.0~1.0を0.5刻みで作る
# a = [ 0.   0.5  1. ]
a = numpy.arange(start=0.0,stop=1.1,step=0.5)
b = numpy.arange(start=0.0,stop=1.1,step=0.5)

# 1次元配列を二次元配列に
# a = [[ 0. ] [ 0.5] [ 1. ]]
a = a.reshape(len(a),1)
b = b.reshape(len(b),1)

# ここからがちと難しい
# numpy.repeatによって1次元配列の中身が指定された回数繰り返される
# axis=0は、次元を指定せずそのままという意味
# b[None] = [[[ 0. ] [ 0.5] [ 1. ]]] つまり、1次元増やすという意味
# b.shape[1] = 1 つまり、bの配列の中の配列の長さ(ちなみに、b.shape[0] = 3)
# ～.reshape(-1, b.shape[1]) つまり、1次元減らすという意味
# numpy.concatenteは第一引数を直でつなげてくれる
# numpy.concatente(axis=1)は、配列の中の配列同士をくっつける
x = numpy.concatenate([
        numpy.repeat(a,len(b),axis=0),
        numpy.repeat(b[None],len(a),axis=0).reshape(-1, b.shape[1])
    ],axis=1)
print(x)