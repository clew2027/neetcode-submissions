class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        cars.sort(reverse=True)
        slowest = 0
        result = 0
        for car, time in cars:
            if time > slowest:
                slowest = time
                result += 1
        return result


