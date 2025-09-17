class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine={}      # food -> cuisine
        self.food_to_rating={}       # food -> rating
        self.cuisine_to_foods={}     # cuisine -> max heap of (-rating, food)
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.food_to_cuisine[food]=cuisine
            self.food_to_rating[food]=rating
            if cuisine not in self.cuisine_to_foods:
                self.cuisine_to_foods[cuisine]=[]
            heapq.heappush(self.cuisine_to_foods[cuisine],(-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food]=newRating
        cuisine=self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_foods[cuisine],(-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap=self.cuisine_to_foods[cuisine]
        while heap:
            rating,food=heap[0]
            if self.food_to_rating[food]==-rating:
                return food
            else:
                heapq.heappop(heap)
        return ""
