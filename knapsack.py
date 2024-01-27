from box import Box 
from typing import List , Tuple

class Knapsack():
    def __init__(self,capacity) -> None:
        self.items: List[Box] = []
        self.capacity : int = capacity


    def add_box(self, box: Box) -> None:
        self.items.append(box)
    
    def calculate_totals(self) -> Tuple[float, float]:
        total_weight = sum(box.weight for box in self.items)
        total_value = sum(box.value for box in self.items)
        return total_weight, total_value
    
    def get_score(self) -> int:
        total_weight = sum(box.weight for box in self.items)
        if total_weight > self.capacity:
            return 0
        else:
            return sum(box.value for box in self.items)
    
    def empty(self) -> None:
        self.items: List[Box] = []
    
    def add_selected_boxes(self, available_boxes: List[Box], selected_boxes: List[int]) -> None:
        for box, isSelected in zip(available_boxes, selected_boxes):
            if isSelected:
                self.add_box(box)