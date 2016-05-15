#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter(self):
        if not self.head:
            return
        cursor = self.head
        yield cursor.data
        while cursor.next:
            cursor = cursor.next
            yield cursor.data

    def insert(self, index, value):
        if not isinstance(index, (int, long)):
            raise Exception('index must be number')

        cursor = self.head
        count = 0

        while count < index - 1:
            cursor = cursor.next
            if not cursor:
                raise Exception('list length less than index')
            count += 1

        node = Node(value)
        node.next = cursor.next
        cursor.next = node

        if node.next is None:
            self.tail = node

    def remove(self, index):
        if not isinstance(index, (int, long)):
            raise Exception('index must be number')

        cursor = self.head
        count = 0

        while count < index - 1:
            cursor = cursor.next
            if not cursor:
                raise Exception('list length less than index')
            count += 1

        cursor.next = cursor.next.next

        if not cursor.next:
            self.tail = cursor


if __name__ == '__main__':
    linkedlist = LinkedList()
    for i in range(10):
        linkedlist.append(i)

    linkedlist.insert(2, 10)

    for data in linkedlist.iter():
        print(data)
