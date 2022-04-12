
import random
import math
import matplotlib.pyplot as plt
import numpy as np

def random_init(points_num,min_x, max_x, min_y, max_y):
    points = []

    while len(points)!=points_num:
        x = random.randint(min_x,max_x)
        y = random.randint(min_y,max_y)
        if [x,y] in points:
            continue
        points.append([x,y])
    
    file = open("temp.txt","w")
    for i in range(len(points)):
        file.write(f'{points[i][0]} {points[i][1]}\n')
    file.close()
    return points

def dis(point1,point2):
    return math.sqrt((point1[0]-point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_distance(points):
    distance = []
    for i in range(len(points)):
        list = []
        for j in range(len(points)):
            list.append(dis(points[i],points[j]))
        distance.append(list)
    return distance
    
def get_next_pos(possibility):
    #print(possibility)
    n = sum(possibility)
    
    for i in range(len(possibility)):
        possibility[i]/=n
    
    n = sum(possibility)
    r = random.uniform(0,n)
    pos = 0
    while True:
        if possibility[pos]==0:
            pos+=1
        elif r-possibility[pos]<0:
            return pos
        else:
            r-=possibility[pos]
            pos=pos+1

def init_pos(rank):
    pos = random.randint(0,rank-1)
    return pos

def load_example(number):
    url = f'./data/example-{number}.txt'
    file = open(url,'r')
    content = file.readlines()
    points = []
    for data in content:
        x,y = data.split(" ")
        points.append([int(x),int(y)])
    distance = calculate_distance(points)
    
    return points,distance

def draw_picture(points,distance,path,iteration):
    rank = len(points)
    ant_number = len(path)
    x = []
    y = []
    for i in range(rank):
        x.append(points[i][0])
        y.append(points[i][1])
    plt.scatter(x,y)
    
    min_cost = np.inf
    for i in range(ant_number):
        temp_cost = 0
        for j in range(1,rank):
            temp_cost+=distance[path[i][j-1]][path[i][j]]
        temp_cost+=distance[path[i][0]][path[i][-1]]
        if temp_cost<min_cost:
            min_cost = temp_cost
            best_path = path[i]
        
    for i in range(ant_number):
        for j in range(rank):
            x[j] = points[path[i][j]][0]
            y[j] = points[path[i][j]][1]
        plt.plot(x,y)

    plt.text(0, 0, f'iteration:{iteration} min_cost = {round(min_cost,2)}', family='fantasy', fontsize=12,style='italic',color='mediumvioletred')
    return round(min_cost,2),best_path


def save_best_result(cost,path,points):
    for i in range(1,len(path)):
        x1 = points[path[i-1]][0]
        y1 = points[path[i-1]][1]
        x2 = points[path[i]][0]
        y2 = points[path[i]][1]
        plt.arrow(x1, y1, x2 - x1, y2 - y1, width = 0.05,color='r', length_includes_head=True)
    plt.arrow(x2,y2,points[path[0]][0]-x2,points[path[0]][1]-y2, width = 0.05,color='r', length_includes_head=True)
    #plt.text(0, 0, f'min_cost = {cost}')
    plt.savefig("result.png")
    plt.close()

    print(f'best path = {show_path(path)}')

def show_path(path):
    route = str(path[0])
    for i in range(1,len(path)):
        route = route+" -> "+str(path[i])
    route = route+"->"+str(path[0])
    return route