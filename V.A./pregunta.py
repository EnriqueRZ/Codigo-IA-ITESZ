import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.spatial import distance_matrix

lis = []

def sobelOperator(img):
    container = np.copy(img)
    size = np.size(container, 0), np.size(container, 1)
    cont = 0
    for i in range(1, size[0]-1):
        for j in range(1, size[1]-1):
            gx = (-img[i-1][j-1]-2*img[i][j-1]-img[i+1][j-1])+(img[i-1][j+1]+2*img[i][j+1]+img[i+1][j+1])
            #print(str(gx))
            #print(str(-img[i-1][j-1])+' '+str(-2*img[i][j-1])+' '+str(-img[i+1][j-1]))
            #print(str(img[i-1][j+1])+' '+str(2*img[i][j+1])+' '+str(img[i+1][j+1]))
            #print(' ')
            gy = (-img[i-1][j-1]-2*img[i-1][j]-img[i-1][j+1])+(img[i+1][j-1]+2*img[i+1][j]+img[i+1][j+1])
            if 30 < np.sqrt(gx**2 + gy**2) < 230: 
                container[i][j] = 255
                cont += 1
            else:
                container[i][j] = 0

            if gx > 10 and gy > 10:
                lis.append([i,j]) 
    return lis

def kmeans(data, k):
    x = np.size(data, 0)
    y = np.size(data, 1)

    initial_centroids = np.random.choice(x, k, replace=False)
    centroids = data[initial_centroids]

    centroids_old = np.zeros((k, y))
    cluster_assignments = np.zeros(x)

    while (centroids_old != centroids).any():
        print('si')
        print(str(centroids))
        centroids_old = centroids.copy()

        dist_matrix = distance_matrix(data, centroids, p=2)

        for i in np.arange(x):
            d = dist_matrix[i]
            closest_centroid = (np.where(d == np.min(d)))[0][0]

            cluster_assignments[i] = closest_centroid

        for j in np.arange(k):
            Xj = data[cluster_assignments == j]
            centroids[j] = np.apply_along_axis(np.mean, axis=0, arr=Xj)

    return (centroids, cluster_assignments)
   

img = cv2.cvtColor(cv2.imread('/home/rocker/Documents/I.A./V.A./uno.png'), cv2.COLOR_BGR2GRAY)
img = sobelOperator(img)
#print( str( np.size(img, 0)) )
data = np.copy(img)
k_means_result = kmeans(data, 1)
centroids = k_means_result[0]

cent = (k_means_result[1]).tolist()

xData = data[:,0]
yData = data[:,1]

xData = np.array(xData)
yData = np.array(yData)

xC = centroids[:,0]
yC = centroids[:,1]
print(type(xC))
print('xC = '+str(centroids[:,0]))
#plt.imshow(img2)

cluster_assignments = (k_means_result[1]).tolist()

colors = ['r', 'g', 'b']
f = lambda x: colors[int(x)]
cluster_assignments = list(map(f, cluster_assignments))

my_dpi = 96
tam = np.size(img, 0), np.size(img, 1)
#plt.figure(figsize=(400, 400), dpi=my_dpi)

plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.title('K-means clustering\n', fontsize=12)

plt.scatter(data[:,0], data[:,1], color=cluster_assignments, s=20)
plt.plot(264, 193, color='blue')
plt.xticks(np.arange(0, 21, 5), fontsize=12)
plt.yticks(np.arange(-5, 21, 5), fontsize=12)

plt.show()


radio = 0
bandera = False

for y in range(xC.shape[0]):
    
    for j in xData:
        if j == xC[y]:
            bandera = True
            radio += 1

    if bandera == True:
        print('per= '+str(radio))
        radio = 0
        bandera = False
            
plt.plot(xData, yData, 'ro')


#print('si'+str(data[5]))
print(type(data))

"""
for i in data:
    if str(i) == '[264 193]':
        print(str(i))
"""


"""
i = 0
while True:
    print(str(data[xC[0],yC[i]]))
    try:
        for i in data:
            if str(i) == '[264 193]':
                print(str(data[xC[0]],[yC[i]]))
        if data[xC[0],yC[i]] in data:
            print('si')
    except:
        print('ya = '+str(i))
        break
    i += 1
"""

