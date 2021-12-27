class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        optimal = round(math.sqrt(area))
        while area % optimal != 0:
            optimal -= 1
        return [area // optimal, optimal]
