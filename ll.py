class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'| DATA: {self.data} | NEXT: {self.next} |'
    
    