
import argparse
from ACO import ACO

from utils import random_init,calculate_distance,load_example

def default_argument_parser():
    parser = argparse.ArgumentParser(description="Ant Colony Algorithm")
    parser.add_argument("--test",nargs="?")
    parser.add_argument('--ant', default=3)
    parser.add_argument('--points', default=5)
    parser.add_argument('--generation', default=100) #[]
    parser.add_argument('--alpha', default=2.0)     #[1,4]
    parser.add_argument('--beta', default=5.0)     #[0,5]
    parser.add_argument('--rho', default=0.5)       #[0.2,0.5]
    parser.add_argument('--q', default=10)
    parser.add_argument('--strategy', default=2) 
    parser.add_argument('--min_x', default=0) 
    parser.add_argument('--max_x', default=10) 
    parser.add_argument('--min_y', default=0) 
    parser.add_argument('--max_y', default=10)    
    '''
    0:  ant-quality system
        In the ant density model, when each ant passes through the cities i and j, 
        it is on the side E_ij The pheromone increment contributed by {ij} is constant, and each unit length is Q
    
    1:  ant-density
        In the ant quantity model, an ant K passes through the edge e between cities I and J_ {ij},
        the pheromone increment contributed to the edge is a variable, that is, Q / D per unit length_ {ij}, 
        the path length d between it and cities I, J_ {ij} related, specifically

    2:  ant-cycle system
        The above two models are applied to the edge e between two cities_ 
        The increment of pheromone contribution on {ij} is completed at the same time that 
        ant K passes through edge, while the ant week model is opposite to edge E_ 
        The increment of {ij} pheromone is updated and adjusted at the end of this cycle. 
        An ant is passing the city I, J opposite E_ The increment of contribution on {ij} is Q / L per unit length_ {k}，
        L_ {k} Is the length of the path the ant walks out of this cycle
    '''
    return parser

def main():
    args = default_argument_parser().parse_args()

    if args.test!=None:
        points,distance = load_example(args.test)
    else:
        points = random_init(args.points,args.min_x,args.max_x,args.min_y,args.max_y)
        distance = calculate_distance(points)
    aco = ACO(
        ant_count=args.ant,
        generations=args.generation,
        alpha=args.alpha,
        beta=args.beta,
        rho=args.rho,
        q=args.q,
        strategy=args.strategy,
        points=points,
        distance=distance,
    )
    aco.run()

if __name__ == '__main__':
    main()