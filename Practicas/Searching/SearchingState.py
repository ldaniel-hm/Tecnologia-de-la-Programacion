from TDA_Stack.StackList import Stack
from TDA_Queue.QueueList import Queue


class State_Node:
    __slots__ = '_state', '_parent', '_cost', '_heuristic'

    def __init__(self, state, parent, cost=0.0, heuristic=0.0):
        self._state = state
        self._parent = parent
        self._cost = cost
        self._heuristic = heuristic

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent

    @property
    def cost(self):
        return self._cost

    @property
    def heuristic(self):
        return self._heuristic

    def __lt__(self, other_node):
        return (self.cost + self.heuristic) < (other_node.cost + other_node.heuristic)

    def path_from_root(self):
        path = list()
        node = self
        while node is not None:
            path.append(node.state)
            node = node.parent
        path.reverse()
        return path


def dfs(initial, goal_test, successors):
    frontier = Stack()
    frontier.push(State_Node(initial, None))
    explored: set = set()
    explored.add(initial)
    while not frontier.is_empty():
        current_node: State_Node = frontier.pop()
        current_state = current_node.state
        print(f" - - - - - - Estudiando {current_state}")
        if goal_test(current_state):
            return current_node.path_from_root()
        succ = successors(current_state)
        for child in succ:
            print(f"Hijo de {current_state} es {child}")
            if child in explored:
                print(f"{child} se añadió en algún momento a la frontera")
                continue
            print(f"Añadiendo {child} al conjunto frontera")
            explored.add(child)
            print(f"Añadiendo nodo con {child} y padre {current_state} a la pila")
            frontier.push(State_Node(child, current_node))
    return None


def bfs(initial, goal_test, successors):
    frontier = Queue()
    frontier.push(State_Node(initial, None))
    explored: set = set(initial)
    while not frontier.is_empty():
        current_node: State_Node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node.path_from_root()
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(State_Node(child, current_node))
    return None
