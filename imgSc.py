import numpy as np, matplotlib.pyplot as plt
def readIMG(x): return plt.imread(x).tolist()

def plotIMG(x):
    plt.imshow(np.asarray(x),cmap='Greys')
    plt.show()    

