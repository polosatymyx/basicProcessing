import numpy as np, matplotlib.pyplot as plt
def readIMG(x): return plt.imread(x).tolist()

def plotIMG(x):
    plt.imshow(np.asarray(x),cmap='Greys')
    plt.show()    

def getMask(X,i,j,N):
    ind = np.arange(N)-N//2
    return X[ind+i].transpose()[ind+j]

def detAVG(X,i,j,N):
    return getMask(X,i,j,N).mean()