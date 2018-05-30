import numpy
import matplotlib.pylab as plt
import step_and_sigmoid


"""
恒常関数
値をそのまま返す関数のこと
:param numpy.array: x
"""
def identity_function(x):
    return x



"""
ネットワークの構築
 重みとバイアスの初期化をします
 …本当は学習結果で分かった重みを突っ込む気がする
"""
def init_network():
    network = {}
    # 1層目の重みとバイアス
    network['W1'] = numpy.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = numpy.array([0.1, 0.2, 0.3])

    # 2層目の重みとバイアス
    network['W2'] = numpy.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = numpy.array([0.1, 0.2])

    # 3層目の重みとバイアス
    network['W3'] = numpy.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = numpy.array([0.1, 0.2])

    return network


"""
入力からニューラルネットワークを通じて出力する
"""
def forward(network, x):
    # 1層目のニューロンを計算する
    a1 = numpy.dot(x, network['W1']) + network['b1']
    z1 = step_and_sigmoid.sigmoid(a1)

    # 2層目のニューロンを計算する
    a2 = numpy.dot(z1, network['W2']) + network['b2']
    z2 = step_and_sigmoid.sigmoid(a2)

    # 3層目のニューロンを計算する
    a3 = numpy.dot(z2, network['W3']) + network['b3']
    y = identity_function(a3)

    return y


if __name__ == "__main__":
    network = init_network()
    print(f'network is {network}')

    x = numpy.array([1.0, 0.5])
    print(f'x = {x}')

    y = forward(network, x)
    print(f'y = {y}')
