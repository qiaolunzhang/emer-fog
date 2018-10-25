'''
this scenario is the original type
virtual start: 0
people: 1, 2, 3
task: 4, 5, 6, 7, 8, 9, 10, 11, 12
virtual end 100
'''
import random
from ortools.graph import pywrapgraph

'''
start_nodes = [0, 0, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12]
end_nodes = [1, 2, 3, 4, 100, 100, 100, 100, 100, 100, 100, 100]
capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
'''
def generate():
    start_nodes = []
    end_nodes = []
    capacity = []

    # generate available people: 0<=num<=3
    num_capable_people = random.randint(0, 3)
    # list of capable_people: people number: 1, 2, 3
    capable_people = random.sample(range(1, 4), num_capable_people)
    for i in range(num_capable_people):
        start_nodes.append(0)
        capacity.append(1)
    end_nodes.extend(capable_people)

    # generate emergency: 0<=num_emergency<=9
    num_emergency = random.randint(0, 9)
    # list of emergency to deal with: emergency number: 4, 5,..., 12
    emergency = random.sample(range(4, 13), num_emergency)

    # generate capable task
    for i in capable_people:
        if num_emergency > 3:
            num_capable_task = random.randint(0, 3)
        else:
            num_capable_task = random.randint(0, num_emergency)
        capable_emergency = random.sample(emergency, num_capable_task)
        for j in range(num_capable_task):
            start_nodes.append(i)
            capacity.append(1)
        # the number of capable is equal to num_capable_task
        end_nodes.extend(capable_emergency)

    # link emergency to virtual end node
    start_nodes.extend(emergency)
    for i in emergency:
        end_nodes.append(20)
        capacity.append(1)

    print("************************************************")
    print(start_nodes)
    print(len(start_nodes))
    print(end_nodes)
    print(len(end_nodes))
    print(capacity)
    print(len(capacity))
    print("************************************************")
    return emergency, start_nodes, end_nodes, capacity

def main():
    emergency, start_nodes, end_nodes, capacities = generate()
    # Instantiate a SimpleMaxFlow solver.
    max_flow = pywrapgraph.SimpleMaxFlow()
    # Add each arc.
    for i in range(0, len(start_nodes)):
        max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

    # Find the maximum flow between node 0 and node 4.
    if max_flow.Solve(0, 20) == max_flow.OPTIMAL:
        print('Max flow:', max_flow.OptimalFlow())
        print('')
        print('  Arc    Flow / Capacity')
        for i in range(max_flow.NumArcs()):
            print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))
        print('Source side min-cut:', max_flow.GetSourceSideMinCut())
        print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
    else:
        print('There was an issue with the max flow input.')

if __name__ == '__main__':
    main()
