from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        emptyroom = 2147483647
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for i, row in enumerate(rooms):
            for j, room in enumerate(row):
                if room == 0:
                    q = deque([(i, j)])
                    d = 1
                    while len(q) != 0:
                        cnt = len(q)
                        while cnt > 0:
                            x, y = q.popleft()
                            for direction in directions:
                                x0, y0 = x + direction[0], y + direction[1]
                                if x0 < 0 or y0 < 0 or x0 > len(rooms)-1 or y0 > len(rooms[0])-1:
                                    continue
                                if rooms[x0][y0] > d:
                                    rooms[x0][y0] = d
                                    q.append((x0, y0))
                            cnt -= 1
                        d += 1
