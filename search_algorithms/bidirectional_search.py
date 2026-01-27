from collections import deque
from data_structures.non_directed_graph import *
def expand_frontier(graph, frontier, visit_this, visit_other):
    current = frontier.popleft()
    for neighbour in graph.neighbors(current):
        if neighbour not in visit_this:
            visit_this[neighbour]=current
            frontier.append(neighbour)
            if neighbour in visit_other:
                return neighbour
    return None

def build_path(meeting_node, visited_start, visited_goal):
    path_start=[]
    node = meeting_node
    while node is not None:
        path_start.append(node)
        node=visited_start[node]
    path_start.reverse()

    path_goal=[]
    node=visited_goal[meeting_node]
    while node is not None:
        path_goal.append(node)
        node=visited_goal[node]
    return path_start + path_goal

def bidirectional_search(graph, start, end):
    if start == end:
        return [start]
    frontier_start = (deque([start]))
    frontier_goal = (deque([end]))

    visited_start = {start: None}
    visited_goal = { end: None}

    while frontier_start and frontier_goal:
        result = expand_frontier(graph,frontier_start,visited_start, visited_goal)
        if result:
            return build_path(result, visited_start, visited_goal)
        result = expand_frontier(graph, frontier_goal, visited_goal, visited_start)
        if result:
            return build_path(result, visited_start, visited_goal)


