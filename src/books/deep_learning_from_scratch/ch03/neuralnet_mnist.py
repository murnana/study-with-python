# coding: utf-8
import sys, os
dirname = os.path.dirname(os.path.abspath(__file__))
# 親ディレクトリを追加
sys.path.append(
    os.path.abspath(
        os.path.join(dirname,'..')
    )
)

import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    """MNISTの読み込み
    
    :return: テストデータだけ
    :rtype: numpy.ndarray((10000, 784)), numpy.ndarray((10000,))
    """
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


'''
sample_weight.pkl から学習済みの重みデータを読み込む
'''
def init_network():
    with open(os.path.join(dirname, 'sample_weight.pkl'), 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    """分類する
    
    :param network: 学習済み重みデータ
    :type network: {'W1': numpy.ndarray((784, 50)), 'W2': numpy.ndarray((50, 100)), 'W3': numpy.ndarray((100, 10)), 'b1': numpy.ndarray((50, )), 'b2': numpy.ndarray((100, )), 'b3': numpy.ndarray((10, ))}
    :param x: テストデータ
    :type x: numpy.ndarray((784, ))
    :return: 結果
    :rtype: numpy.ndarray((10, ))
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


if __name__ == "__main__":
    x, t = get_data()
    network = init_network()
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p= np.argmax(y) # 最も確率の高い要素のインデックスを取得
        if p == t[i]:
            accuracy_cnt += 1

    print(f"Accuracy: {str(float(accuracy_cnt) / len(x))}")
