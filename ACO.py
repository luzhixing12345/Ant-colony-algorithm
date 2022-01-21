

from utils import draw_picture, get_next_pos, init_pos,save_best_result
import matplotlib.pyplot as plt
import numpy as np


class ACO(object):
    def __init__(self, ant_count: int, generations: int, alpha: float, beta: float, rho: float, q: int,
                 strategy: int,distance,points):
        """
        :param ant_count:
        :param generations:
        :param alpha: relative importance of pheromone
        :param beta: relative importance of heuristic information
        :param rho: pheromone residual coefficient
        :param q: pheromone intensity
        :param strategy: pheromone update strategy. 0 - ant-cycle, 1 - ant-quality, 2 - ant-density
        :param distance: distance between each points
        """
        self.Q = q
        self.rho = rho
        self.beta = beta
        self.alpha = alpha
        self.ant_count = ant_count
        self.generations = generations
        self.update_strategy = strategy
        self.points = points
        self.distance = distance
        self.rank = len(distance)   
        self.eta = [[0 if i == j else 1 / distance[i][j] for j in range(self.rank)] for i in
                    range(self.rank)]

        self.pheromone_content = [[1 for _ in range(self.rank)] for _ in range(self.rank)]    
        # for i in range(self.rank):
        #     self.pheromone_content[i][i]=0

    def initialization(self):
        # memory vector is used to record the total path of each ant
        self.memory_vector = []
        for _ in range(self.ant_count):
            # random initialize each ant first
            self.memory_vector.append([init_pos(self.rank)])
        

    def roulette(self,id,pos):
        # classical roulette method 
        possibility = []
        for i in range(self.rank):
            if i in self.memory_vector[id]:
                # if the ant has been to the point, pass it
                possibility.append(0)
            else:
                possibility.append(self.pheromone_content[pos][i]**self.alpha*(self.eta[pos][i]**self.beta))

        next_pos = get_next_pos(possibility)
        return next_pos

    def update_pheromone_delta(self,ant_path):
        # we must update the pheromone content in the same time, instead of one by one, otherwise it may 
        # affect the possibility of other ants
        if self.update_strategy == 0:
            for i in range(self.ant_count):
                self.pheromone_content[ant_path[i][0]][ant_path[i][1]]+=self.Q
                self.pheromone_content[ant_path[i][1]][ant_path[i][0]]+=self.Q
                if len(self.memory_vector[0])==self.rank:
                    self.pheromone_content[self.memory_vector[i][-1]][self.memory_vector[i][0]]+=self.Q
                    self.pheromone_content[self.memory_vector[i][0]][self.memory_vector[i][-1]]+=self.Q
        elif self.update_strategy == 1:
            for i in range(self.ant_count):
                self.pheromone_content[ant_path[i][0]][ant_path[i][1]]+=(self.Q/self.distance[ant_path[i][0]][ant_path[i][1]])
                self.pheromone_content[ant_path[i][1]][ant_path[i][0]]+=(self.Q/self.distance[ant_path[i][0]][ant_path[i][1]])
                if len(self.memory_vector[0])==self.rank:
                    self.pheromone_content[self.memory_vector[i][-1]][self.memory_vector[i][0]]+=self.Q/self.distance[self.memory_vector[i][0]][self.memory_vector[i][-1]]
                    self.pheromone_content[self.memory_vector[i][0]][self.memory_vector[i][-1]]+=self.Q/self.distance[self.memory_vector[i][0]][self.memory_vector[i][-1]]
        elif self.update_strategy == 2:
            if len(self.memory_vector[0]) == self.rank:
                total_cost = []
                for i in range(self.ant_count):
                    cost = 0
                    for j in range(1,self.rank):
                        cost+=self.distance[self.memory_vector[i][j-1]][self.memory_vector[i][j]]
                    cost+=self.distance[self.memory_vector[i][0]][self.memory_vector[i][-1]]
                    total_cost.append(cost)
                for i in range(self.ant_count):
                    delta = self.Q/total_cost[i]
                    for j in range(1,self.rank):
                        self.pheromone_content[self.memory_vector[i][j-1]][self.memory_vector[i][j]]+=delta
                        self.pheromone_content[self.memory_vector[i][j]][self.memory_vector[i][j-1]]+=delta
                    self.pheromone_content[self.memory_vector[i][0]][self.memory_vector[i][-1]]+=delta
                    self.pheromone_content[self.memory_vector[i][-1]][self.memory_vector[i][0]]+=delta
            else:
                # have not finished one cycle
                pass
        else:
            raise KeyError
    def update_pheromone(self):
        for i in range(self.rank):
            for j in range(self.rank):
                self.pheromone_content[i][j]=self.pheromone_content[i][j]*(1-self.rho)

    def update_memory_vector(self,ant_path):
        for i in range(self.ant_count):
            self.memory_vector[i].append(ant_path[i][1])

    def run(self):
        plt.ion()
        for iteration in range(self.generations):
            print(f'-----start iteration {iteration+1} of ACO-----')
            self.initialization()
            for steps in range(self.rank-1):
                # in a new iteration, each ant choose a path, from pos to next_pos
                ant_path = []
                for i in range(self.ant_count):
                    pos = self.memory_vector[i][-1]
                    next_pos = self.roulette(i,pos)
                    ant_path.append([pos,next_pos])
                self.update_memory_vector(ant_path)
                self.update_pheromone_delta(ant_path)
            self.update_pheromone()
            plt.cla()
            plt.title("ant colony algorithm")
            cost,path = draw_picture(self.points,self.distance,self.memory_vector,iteration)
            #print(f'best path cost = {best_cost}')
            plt.pause(0.01)

        save_best_result(cost,path,self.points)
        plt.ioff()
        plt.show()
        

        
        
        
        

        

        



    
