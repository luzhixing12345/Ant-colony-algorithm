# Ant Colony algorithm

## Introduction:
This is the python implementation of ant colony algorithm.

The code references [excellent Github code in python](https://github.com/ppoffice/ant-colony-tsp) about some function arguments and names and values, especailly thanks for his contribution, offers me great help.

From realizing the ant colony algorithm by myself, I also learn better about it.Actually it's a nice idea, and it could be used in many similar problems.

But it still confuse me that it seems not easy to convergent as I know.

### About ant colony:
- [introduction video](https://www.bilibili.com/video/BV17V411a7yf?from=search&seid=12790218810323775687&spm_id_from=333.337.0.0)
- [introduction video in matlab realization without code](https://www.bilibili.com/video/BV1ZA411v7pC?from=search&seid=12790218810323775687&spm_id_from=333.337.0.0)


## Requirements:
- python
- matplotlib

## Examples:

![](https://raw.githubusercontent.com/learner-lu/picbed/master/0R7F0VSP4%606C4YPJKDOTHGV.png)

![](https://raw.githubusercontent.com/learner-lu/picbed/master/123.png)




## Use:
- each run will create a random location for each country
  ```python
  python main.py
  ```
- use examples in `./data/example-x.txt` as\
  change x into number 1~5
  ```python
  python main.py --test x
  ```
- change arguments of ant colont algorithm
  - `ant`: the number of ants
  - `points`: the number of points
  - `generation`:the number of iteration
  - `alpha`:relative importance of pheromone
  - `beta`:relative importance of heuristic information
  - `rho`:pheromone residual coefficient
  - `q`:pheromone intensity
  - `strategy`:pheromone update strategy. 0 - ant-cycle, 1 - ant-quality, 2 - ant-density
  - `min_x`,`max_x`,`min_y`,`max_y` the range of values of points(x,y)
  ```python
  python main.py -ant 20 -points 50 -rho 0.2 -max_x 1000 -max_y 1000
  ```
  **pay attention that changing the arguments may imporve the algorithm in some cases, or behave worse**

-  each run will create a record file `./temp.txt`, if you want to use the data again by different strategies,\
  you should move it to `./data/` and rename it as `./data/example-x.txt` and then use `--test x`.
