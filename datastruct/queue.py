#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datastruct import Node


class Queue:
    '''
    : 先进先出
    '''

    def __init__(self):
        self._head = None
        self._tail = None

    def put(self, value):
        node = Node(value)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def push(self):
        if not self._head:
            raise Exception('empty queue')
        node = self._head
        self._head = node.next
        return node.data
