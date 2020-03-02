from imgSc import *
# открой изображение, любое

im = readIMG('python.png')

# выведи на экран

x = np.array(im).mean(2)

# plotIMG(x)
# print(x)
# plotIMG(x)
N=20    
xx = np.copy(x)
for i in range(x.shape[0]-N//2):
    for j in range(x.shape[1]-N//2):
        xx[i,j] = detAVG(x,i,j,N)
plotIMG(xx)

# for i in range(50,53):
#     for j in range(50,53):
#         xx[i,j] = detAVG(x,i,j,5)
#         print (xx[i][j])
# print(im[1332][1999])


#посмотри структуру изображения
