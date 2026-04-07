class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        x, y = 0, 0
        direction = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        max_dist = 0
        for cmd in commands:
            if cmd==-1:
                direction=(direction+1)%4
            elif cmd==-2:
                direction=(direction-1)%4
            else:
                dx,dy=dirs[direction]
                for _ in range(cmd):
                    if (x+dx,y+dy) in obstacle_set:
                        break
                    x+=dx
                    y+=dy
                    max_dist=max(max_dist,x*x+y*y)
        return max_dist