# Ant Colony algorithm

## Introduction

This is the python implementation of ant colony algorithm.

Dynamic graphs are used to show the dynamic change when running the algorithm

The code references [excellent Github code in python](https://github.com/ppoffice/ant-colony-tsp) about some function arguments and names and values, especailly thanks for his contribution, offers me great help.

### About ant colony

- [introduction video](https://www.bilibili.com/video/BV17V411a7yf?from=search&seid=12790218810323775687&spm_id_from=333.337.0.0)
- [introduction video in matlab realization without code](https://www.bilibili.com/video/BV1ZA411v7pC?from=search&seid=12790218810323775687&spm_id_from=333.337.0.0)
- [professional blog](https://www.cnblogs.com/bokeyuancj/p/11798635.html)

## Requirements

```bash
pip install -r requirements.txt
```

## Examples

![result](https://raw.githubusercontent.com/learner-lu/picbed/master/result.png)

![dynamic](https://raw.githubusercontent.com/learner-lu/picbed/master/asdqw.gif)

## Use

- easy run

  ```python
  python main.py
  ```

- use your own data

  If you want to test your own data, please create a new example file(for example `data.txt`) and use

  ```python
  python main.py --test {FILENAME}
  # python main.py --test data.txt
  ```

  **Pay attention that** your data should be two-dimensional {X,Y} like below

  ```bash
  28 16
  5 34
  28 3
  19 48
  17 30
  23 1
  ...
  ```

  You could also use some text files in [data](data)

## Arguments

There are many related parameters in this algorithm, you could run with default arguments or change it as you like. **But changing the arguments may imporve the algorithm in some cases, or behave worse**

change arguments of ant colont algorithm

- `ant`: the number of ants
- `points`: the number of points
- `generation`:the number of iteration
- `alpha`:relative importance of pheromone
- `beta`:relative importance of heuristic information
- `rho`:pheromone residual coefficient
- `q`:pheromone intensity
- `strategy`:pheromone update strategy.

  see more details in code annotation

  - 0 - ant-cycle
  - 1 - ant-quality
  - 2 - ant-density

- `min_x`,`max_x`,`min_y`,`max_y` the range of values of points(x,y)

  ```python
  python main.py --ant 20 --points 50 --rho 0.2 --max_x 1000 --max_y 1000
  ```

## Attention

each run will create a record file `./temp.txt`, if you want to use the data again, you should move it to `./data/` and rename it as `./data/example-x.txt` and then use --test to load this file.

The result will be saved as `./result.png` for each run.

**If the final picture seems mad or has more than one line, that means it does not converge to a local optimal solution at the end of the iteration. So you need to change your arguments choice, such as increase `rho` or decrease `q` and so on**

As the [blog](https://www.cnblogs.com/bokeyuancj/p/11798635.html) said, ant colony algorithm is barely useful in solving small-scale TSP problems, and the optimal solution can be found in a little time. However, if the problem scale is large, the performance of ant colony algorithm will be very low or even stuck. So it can be improved, such as elite ant system.

**This code is just a simple realization of ant colony algorithm, when I run the code myself I also find some inappropriate simulation results and strange simulations.**

If you find any bug or suggestions to improve, please leave your advice in issue.
