import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
import random
import math
import matplotlib.cm as cm

class KMeans(object):
    pointsX = []
    pointsY = []
    clusters = []
    numPnt: int
    numCls: int

    def __init__(self, numObj, numClass, max = None):
        if max is None:
            for i in range(numObj):
                self.pointsX.append(random.uniform(0, 10))
                self.pointsY.append(random.uniform(0, 10))
            for i in range(numClass):
                self.clusters.append(Cluster())
            self.numPnt = numObj
            self.numCls = numClass
            step = int(numObj / numClass)
            point = 0
            for i in range(numClass):
                self.clusters[i].curX = self.pointsX[int(point)]
                self.clusters[i].curY = self.pointsY[int(point)]
                point += step
        else:
            self.pointsX = max.pointsX
            self.pointsY = max.pointsY
            self.numPnt = numObj
            self.numCls = numClass
            for i in range(numClass):
                self.clusters.append(Cluster())
                self.clusters[i].curX = max.clusters[i].X
                self.clusters[i].curY = max.clusters[i].Y
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
        firstX = cltrs[0].curX
        firstY = cltrs[0].curY
        for i in range(size):
            minimum = math.sqrt(
                (firstX - pntsX[i])*(firstX- pntsX[i]) + (firstY - pntsY[i])*(firstY - pntsY[i]))
            num = 0
            for j in range(1, numb):
                secondX = cltrs[j].curX
                secondY = cltrs[j].curY
                tmp = math.sqrt(
                    (secondX - pntsX[i])*(secondX - pntsX[i]) + (secondY - pntsY[i])*(secondY- pntsY[i]))
                if minimum > tmp:
                    minimum = tmp
                    num = j
            cltrs[num].pointsX.append(pntsX[i])
            cltrs[num].pointsY.append(pntsY[i])

    def DoTask(self):
        flag = True
        count = 0
        numCls = self.numCls
        while flag:
            chk = 0
            self.Bind()
            for i in range(numCls):
                self.clusters[i].FindCenter()
            for j in range(numCls):
                if ((self.clusters[j].curX == self.clusters[j].prevX) and (
                        self.clusters[j].curY == self.clusters[j].prevY)):
                    chk += 1
                if chk == numCls:
                    flag = False
            count += 1
            print("Iteration:" + str(count))


class Cluster(object):
    pointsX = []
    pointsY = []
    curX: float
    curY: float
    prevX: float
    prevY: float

    def FindCenter(self):
        sumX = 0
        sumY = 0
        length = len(self.pointsX)
        for i in range(length):
            sumX += self.pointsX[i]
            sumY += self.pointsY[i]
        self.prevX = self.curX
        self.prevY = self.curY
        self.curX = sumX / length
        self.curY = sumY / length


def Draw(task):
    fig, ax = plt.subplots()
    colors = ['#ff0000', '#bf00ff', '#0000ff', '#40ff00', '#00ffbf', '#00ffff', '#00bfff', '#0080ff', '#ffff00',
              '#8000ff',
              '#ffbf00', '#ff00bf', '#808080', '#ff99ff', '#660033', '#999966', '#cc3300', '#ccffcc', '#ff99cc',
              '#99ccff']
    ax.set_title('K-means')
    for i in range(task.numCls):
        x = []
        y = []
        for j in range(len(task.clusters[i].pointsX)):
            x.append(task.clusters[i].pointsX[j])
            y.append(task.clusters[i].pointsY[j])
        ax.scatter(x, y, c=colors[i])
        ax.scatter(task.clusters[i].curX, task.clusters[i].curY, s=200, c='white' , linewidths = 2,
                   edgecolors = 'black')
    ax.set_facecolor('black')
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.show()


