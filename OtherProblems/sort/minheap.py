class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0
    
    def get_size(self):
        return self.heap_size

    def min_child(self, i):
        if i*2+1 > self.heap_size:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1

    def heapify_down(self, i):
        while i * 2 <= self.heap_size:
            minchild = self.min_child(i)
            if self.heap_list[i] > self.heap_list[minchild]:
                self.heap_list[i], self.heap_list[minchild] = self.heap_list[minchild], self.heap_list[i]
            i = minchild

    def heapify_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i = i // 2

    def insert(self, num):
        self.heap_list.append(num)
        self.heap_size += 1
        self.heapify_up(self.heap_size)

    def del_min(self):
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size -= 1
        self.heap_list.pop()
        self.heapify_down(1)
    
    def get_min(self):
        return self.heap_list[1]
