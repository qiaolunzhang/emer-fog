'''
this scenario is the type with scheduling and fog computing
virtual start: 0
people: 1, 2, 3
task: 4, 5, 6, 7, 8, 9, 10, 11, 12
virtual end 100
'''
import random
from ortools.graph import pywrapgraph

def generate():
    start_nodes = [0, 0, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    end_nodes = [1, 2, 3, 4, 100, 100, 100, 100, 100, 100, 100, 100]
    capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(1, 4):
        num_capable_task = random.randint(0, 3)
        capable_task = random.sample(range(4, 12), num_capable_task)
        for j in range(num_capable_task):
            start_nodes.append(i)
            capacity.append(1)
        end_nodes.extend(capable_task)
    '''
    print(start_nodes)
    print(len(start_nodes))
    print(end_nodes)
    print(len(end_nodes))
    print(capacity)
    print(len(capacity))
    '''

def main():


if __name__ == '__main__':
    main()
