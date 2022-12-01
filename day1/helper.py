class Node:
    def __init__(self, val, next=None):
        self.item = val
        self.next = next

class PriorityQueueNode(Node):
    def __init__(self, value, pr, next=None):
        super().__init__(value, next)
        self.prio = pr

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.qsize = 0

    def isEmpty(self):
        return True if self.front == None else False
    
    def size(self):
        return self.qsize
    
    def push(self, value, pr):
        newNode = PriorityQueueNode(value, pr)
        self.qsize += 1

        if self.isEmpty():
            self.front = newNode
            return 1
        else:
            if self.front.prio > pr:
                newNode.next = self.front
                self.front = newNode
                return 1
            else:
                temp = self.front
                while temp.next:
                    if pr <= temp.next.prio:
                        break
                    temp = temp.next

                newNode.next = temp.next
                temp.next = newNode

                return 1

    def pop(self):
        if self.isEmpty():
            return
        else:
            popVal = self.front.item
            self.front = self.front.next
            self.qsize -= 1
            return popVal