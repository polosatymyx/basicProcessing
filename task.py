from imgSc import *
# открой изображение, любое

im = readIMG('python.png')

# выведи на экран

# plotIMG(im)
# print(type(im))
# x = im.split()
# print(len(x))
# im2 = np.array(im)
x = []
z = []
# for i in range (1333):
#     for b in range (2000):   
#         z.append(sum(im[i][b]) / 3)
#     x.append(z)
#     z=[]
x = np.array(im).mean(2)
# plotIMG(x)
print(x)
plotIMG(x)
# print(im[1332][1999])


#посмотри структуру изображения
