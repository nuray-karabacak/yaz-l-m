# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:45:56 2024

@author: nuray
"""

import math

# Noktaların Tanımlanması
points = [(2, 3), (1, 0), (2, 0), (2, 3)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
x=len(distances)

for k  in range (0,x-1):
    
    for l in range (0,(x-i-1)):
        if (distances[k]<distances[l]):
           min_distances=distances[k]
        else:
            min_distances=distances[l]
            
print("Minimum Hesaplama: ", min_distances)

