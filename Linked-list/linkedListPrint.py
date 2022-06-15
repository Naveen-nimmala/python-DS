#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.head is None:
            print("Its empty list")
            return 
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_node(self):
        if self.length == 0:
            return None
        temp = self.head 
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0 :
            self.head = None
            self.tail = None
        return temp.value



my_linked_list = LinkedList(1)
my_linked_list.append_node(2)
my_linked_list.append_node(3)

print(my_linked_list.pop_node())


