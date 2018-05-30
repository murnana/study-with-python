'''
MNIST を使用した実践
元のソース: https://github.com/oreilly-japan/deep-learning-from-scratch
'''
import sys, os
dirname = os.path.dirname(os.path.abspath(__file__))
# 親ディレクトリを追加
sys.path.append(
    os.path.abspath(
        os.path.join(dirname,'..')
    )
)

import numpy
from dataset.mnist import load_mnist
from PIL import Image   # Python3ではpilが使えないので、pillowを使用している

'''
イメージを開く
他のプログラムを通して開きます
:param numpy.array: img 画像データの入った二次元行列
'''
def img_show(img):
    pil_img = Image.fromarray(numpy.uint8(img)) # numpy.arrayのデータをPILのデータオブジェクトに変換
    pil_img.show()

if __name__ == '__main__':
    # MNISTの読み込み
    # flatten=True で1次元配列にしている
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

    img = x_train[0]    # 訓練画像を1枚選択する
    label = t_train[0]  # ↑の訓練ラベルを引っ張り出す
    print(label)        # 「5」という画像であることを指す

    print(img.shape)            # (784,) 28 * 28の画像が一次元になっている
    img = img.reshape(28, 28)   # 形状を元の画像サイズに変形
    print(img.shape)            # (28, 28) 28 * 28の二次元になった

    img_show(img)
