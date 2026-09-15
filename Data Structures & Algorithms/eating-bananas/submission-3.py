class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #4, 3, 2, 1
        
        left = 1
        right = max(piles)
        speed = right

        while left <= right:
            print("left")
            print(left)
            print("right")
            print(right)
            mid = ((right + left) //2)
            hours = 0
            for pile in piles:
                hours += -(-pile // mid)
            if hours > h:
                left = mid + 1
            elif hours <= h:
                
                right = mid - 1
                speed = min(mid, speed)
            
            print(hours)
            print(speed)
        
        return speed


            



        