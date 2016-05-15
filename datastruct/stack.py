#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datastruct import Node


class Stack:
    '''
    : 先进后出
    '''

    def __init__(self):
        self._top = None

    def push(self, value):
        node = Node(value)

        if not self._top:
            self._top = node
        else:
            node.next = self._top
            self._top = node

    def pop(self):
        node = self._top
        self._top = node.next
        return node.data


if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    while stack._top:
        print(stack.pop())
