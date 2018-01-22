import numpy
from matplotlib import pyplot

# パーセプトロン
# 正確には、パーセプトロンのノード
class Perceptron:
    def __init__(self,count):
        self.__weight = numpy.zeros(count)

    # パーセプトロンの基本的な動き
    # 閾値を超えたら(発火したら)1を返し、そうでないときは0を返す
    def __step(self,num):
        if num > 0:
            return 1
        else:
            return 0

    # こいつ発火するのかい？を聞くための関数
    def output(self,num):
        return self.__step( numpy.dot( num, self.__weight ) )

    # 学習用関数
    def training(self, train_x, train_y, eta, epoch):
        for i in range(epoch):
            for x,y in zip(train_x,train_y):
                o = self.output(x)
                self.__weight += x * (y - o) * eta

    def get_weight(self):
        return self.__weight


# テスト
# ANDを学習させる
if __name__ == "__main__":
    # トレーニング内容を記述する
    # 2次元配列(X∩Y)での結果を学習させていくが、
    # 最後にバイアスを入れる必要がある
    # (バイアスによって閾値をいくらか調整できる)
    bias = 1
    train_x = numpy.array([[0,0,bias],[0,1,bias],[1,0,bias],[1,1,bias]])

    # 結果こうでなければならない！を入れる
    train_y = numpy.array([0,0,0,1])

    # 学習係数
    # 重みを更新するとき、どれくらい変化させるのか
    eta     = 0.1

    # パーセプトロン作成
    percept = Perceptron(3)

    # 100回学習させる
    epoch   = 100
    percept.training(train_x,train_y,eta,epoch)

    # グラフを描いてみる
    x1 = numpy.arange(start=0.0,stop=1.0,step=0.1)
    x1 = x1.reshape(len(x1),1)
    x2 = numpy.arange(start=0.0,stop=1.0,step=0.1)
    x2 = x2.reshape(len(x2),1)
    x = numpy.concatenate( [
        numpy.repeat(x1,len(x2),axis=0),
        numpy.repeat(x2,len(x1),axis=0).reshape(-1,x2.shape[1]),
        numpy.repeat(numpy.array([1]),len(x1),axis=0),reshape(len(x1),1)
    ],axis=1)
    y = percept.output(i)
    train_true = x[y == 1]
    train_false = x[y != 1]
    pyplot.plot(train_true[:,0], train_true[:,1], "o", color="#FF0000", label="true")
    pyplot.plot(train_false[:,0], train_false[:,1], "^", color="#FF7777", label="false")

    true_x = x[y==1]
    false_x = x[y!=1]
    pyplot.plot(true_x[:,0], true_x[:,1], "o", color="#00FF00", label="true")
    pyplot.plot(false_x[:,0], false_x[:,1], "^", color="#77FF77", label="false")

    pyplot.show()
    