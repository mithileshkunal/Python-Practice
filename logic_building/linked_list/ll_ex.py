class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def print_list(self):
        now = self.head
        while now is not None:
            print(str(now.data) + "-->", end="")
            now = now.next
        print()

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            now = self.head
            while now.next is not None:
                now = now.next
            # we came to the last of the linked list
            # append the new data here
            now.next = newNode
    
    def insert_at(self, data, position):
        list_len = 0
        now = self.head
        newNode = Node(data)
        if now is None:
            if position == 0:
                self.push(data)
            else:
                print("Empty list!!! Position is not valid")
        else:
            while now.next is not None:
                list_len = list_len + 1
                # check if the current place is to be inserted
                if list_len == position:
                    newNode.next = now
                    if list_len == 1:
                        self.head = newNode
                    return
                now = now.next
            list_len = list_len + 1
            print(list_len)

if __name__ == "__main__":
    ll = LinkedList()

    for item in range(1, 11):
        ll.append(item)
        ll.push(100 - item)

    ll.insert_at(-111, 2)
    ll.print_list()
