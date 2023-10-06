class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
       x1,x2,y1,y2 = 0,0,0,0

       if bx2>ax1 and bx1<ax2 or ax2>bx1 and ax1<bx2:#overlap horizontal
            x1=max(ax1,bx1)
            x2=min(ax2,bx2)
       if by2>ay1 and by1<ay2 or ay2>by1 and ay1<by2:#overlap vertical
            y1=max(ay1,by1)
            y2=min(ay2,by2)

       area1=abs(ax2-ax1)*abs(ay2-ay1)
       area2=abs(bx2-bx1)*abs(by2-by1)
       covered = abs(x1-x2)*abs(y1-y2)
       return area1+area2-covered
