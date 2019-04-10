import rubik
import Queue

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if start == end:
        return []
    
    start_frontier = Queue.Queue()
    start_parent = {}
    start_level = {}
    start_parent_move = {}
    start_frontier.put(start)
    start_level[start] = 0
    start_parent[start] = None
    start_parent_move[start] = None
    
    end_frontier = Queue.Queue()
    end_parent = {}
    end_level = {}
    end_parent_move = {}
    end_frontier.put(end)
    end_level[end] = 0
    end_parent[end] = None
    end_parent_move[end] = None
    
    intersectFound = False
    intersect = None
    level = 0
    while (True):
        level += 1
#        print ("level = " + str(level))
        if not start_frontier.empty():
            vertex = start_frontier.get()
            for move in rubik.quarter_twists:
                position = rubik.perm_apply(move,vertex)
                if position not in start_parent:
#                    print ("start permutation unvisited")
                    start_parent[position] = vertex
                    start_level[position] = level
                    start_parent_move[position] = move
                    start_frontier.put(position)
                    if position in end_parent:
#                        print ("position exists in end_parent")
                        intersect = position
                        intersectFound = True
                        break
            if intersectFound:
                break
        if not end_frontier.empty():
            vertex = end_frontier.get()
            for move in rubik.quarter_twists:
                position = rubik.perm_apply(move,vertex)
                if position not in end_parent:
#                    print ("end permutation unvisited")
                    end_parent[position] = vertex
                    end_level[position] = level
                    end_parent_move[position] = move
                    end_frontier.put(position)
                    if position in start_parent:
#                        print ("position exists in start_parent")
                        intersect = position
                        intersectFound = True
                        break
            if intersectFound:
                break
        if end_frontier.empty() and start_frontier.empty():
            break
    
    if intersect is None:
        return None
    
    path = []
    pos = intersect
    while (start_parent[pos] is not None):
        path.insert(0,start_parent_move[pos])
        pos = start_parent[pos]
        
    pos = intersect
    while (end_parent[pos] is not None):
        move = rubik.perm_inverse(end_parent_move[pos])
        path.append(move)
        pos = end_parent[pos]
    
#    path = [None] * start_level[intersect]
#    pos = intersect
#    move = start_parent_move[pos]
#    path[start_level[intersect]-1] = move
#    for i in range(start_level[intersect]-2,-1,-1):
#        if (start_parent[pos] is not None):
#            pos = start_parent[pos]
#            move = start_parent_move[pos]
#            path[i] = move
#    
#    pos = intersect
#    while (end_parent[pos] is not None):
#        move = rubik.perm_inverse(end_parent_move[pos])
#        path.append(move)
#        pos = end_parent[pos]
    
    return path
    
    
#    pathLength = end_level[intersect] + start_level[intersect]
#    return getPath(start_parent, end_parent, intersect, start_level[intersect],end_level[intersect])

def getPath (start_parent, end_parent, intersect, startIntersectLevel, endIntersectLevel):
    path = [None] * (startIntersectLevel)
    path[startIntersectLevel] = intersect
    currentPos = intersect
    for i in range(startIntersectLevel-1,-1,-1):
        currentPos = start_parent[currentPos]
        path[i] = currentPos
    
    currentPos = intersect
    while (end_parent[currentPos] is not None):
        currentPos = end_parent[currentPos]
        path.append(currentPos)
    
    return path
        

def getNextPermutations (position):
    nextPerms = []
    for perm in rubik.quarter_twists:
        newP = rubik.perm_apply(perm,position)
        nextPerms.append(newP)
    return nextPerms
    
    
