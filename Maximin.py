import Kmeans
import matplotlib.pyplot as plt
import random
import math


class Maximin(object):
    pointsX = []
    pointsY = []
    clusters = []
    numPnt: int
    numCls: int

    def __init__(self, numObj):
        for i in range(numObj):
            self.pointsX.append(random.uniform(0, 10))
            self.pointsY.append(random.uniform(0, 10))
        self.numPnt = numObj
        cluster = Cluster()
        cluster.X = self.pointsX[0]
        cluster.Y = self.pointsY[0]
        self.clusters.append(cluster)
        self.numCls = 1
        maximum = math.sqrt((cluster.X - self.pointsX[1]) * (cluster.X - self.pointsX[1]) + (cluster.Y - self.pointsY[1]) * (cluster.Y - self.pointsY[1]))
        num = 1
        for i in range (2, numObj):
            tmp = math.sqrt((cluster.X - self.pointsX[i])*(cluster.X - self.pointsX[i]) + (cluster.Y - self.pointsY[i])*(cluster.Y - self.pointsY[i]))
            if tmp > maximum:
                maximum = tmp
                num = i
        cluster = Cluster()
        cluster.X = self.pointsX[num]
        cluster.Y = self.pointsY[num]
        self.clusters.append(cluster)
        self.numCls += 1
        self.Bind()

    def Bind(self):
        cltrs = self.clusters
        size = self.numPnt
        pntsX = self.pointsX
        pntsY = self.pointsY
        numb = self.numCls
        for i in range(numb):
            cltrs[i].pointsX = []
            cltrs[i].pointsY = []
        firstX = cltrs[0].X
        firstY = cltrs[0].Y
        for i in range(size):
            minimum = math.sqrt(
                (firstX - pntsX[i])*(firstX - pntsX[i]) + (firstY - pntsY[i])*(firstY - pntsY[i]))
            num = 0
            for j in range(1, numb):
                secondX = cltrs[j].X
                secondY = cltrs[j].Y
                tmp = math.sqrt(
                    (secondX - pntsX[i])*(secondX - pntsX[i]) + (secondY - pntsY[i])*(secondY- pntsY[i]))
                if minimum > tmp:
                    minimum = tmp
                    num = j
            cltrs[num].pointsX.append(pntsX[i])
            cltrs[num].pointsY.append(pntsY[i])
        Draw(self)

    def DoTask(self):
        flag = True
        count = 0
        k = self.numCls
        while flag:
            self.Bind()
            max = 0
            newX = 0
            newY = 0
            clusters = self.clusters
            for i in range(k):
                posX = clusters[i].X
                posY = clusters[i].Y
                pntsX = clusters[i].pointsX
                pntsY = clusters[i].pointsY
                for j in range(len(clusters[i].pointsX)):
                    tmp = math.sqrt(
                        (posX - pntsX[j]) * (posX - pntsX[j]) + (posY - pntsY[j]) * (posY - pntsY[j]))
                    if tmp > max:
                        max = tmp
                        newX = pntsX[j]
                        newY = pntsY[j]
            midDist = 0
            for i in range(k):
                posX = clusters[i].X
                posY = clusters[i].Y
                midDist += math.sqrt(
                        (posX - newX) * (posX - newX) + (posY - newY) * (posY - newY))
            midDist /= k*2
            if max > midDist:
                cluster = Cluster()
                cluster.X = newX
                cluster.Y = newY
                self.clusters.append(cluster)
                self.numCls += 1
            else:
                flag = False
            count += 1
            print("Iteration:" + str(count))


class Cluster(object):
    pointsX = []
    pointsY = []
    X: float
    Y: float


def Draw(task):
    fig, ax = plt.subplots()
    colors = ['#ff0000', '#bf00ff', '#0000ff', '#40ff00', '#00ffbf', '#00ffff', '#00bfff', '#0080ff', '#ffff00',
              '#8000ff',
              '#ffbf00', '#ff00bf', '#808080', '#ff99ff', '#660033', '#999966', '#cc3300', '#ccffcc', '#ff99cc',
              '#99ccff']
    ax.set_title('Maximin')
    for i in range(task.numCls):
        x = []
        y = []
        for j in range(len(task.clusters[i].pointsX)):
            x.append(task.clusters[i].pointsX[j])
            y.append(task.clusters[i].pointsY[j])
        ax.scatter(x, y, c=colors[i])
        ax.scatter(task.clusters[i].X, task.clusters[i].Y, s=200, c='white', linewidths = 2,
                   edgecolors = 'black')
    ax.set_facecolor('black')
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.show()



