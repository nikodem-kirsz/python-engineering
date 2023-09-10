from abc import ABC, abstractmethod

# strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete sorting strategies
class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)    

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data)

class MergeSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Merge Sort")
        return sorted(data)
    
# Context class that uses selected sorting strategy

class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)

# Client code
data = [5,2,9,1,5,6]

bubble_sort = BubbleSort()
quick_sort = QuickSort()
merge_sort = MergeSort()

# Sort data using different strategies
sorter = Sorter(bubble_sort)
sorted_data = sorter.sort_data(data)
print("Sorted Data:", sorted_data)

sorter = Sorter(quick_sort)
sorted_data = sorter.sort_data(data)
print("Sorted Data:", sorted_data)

sorter = Sorter(merge_sort)
sorted_data = sorter.sort_data(data)
print("Sorted Data:", sorted_data)