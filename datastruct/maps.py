#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Nodes:
    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node):
        self.root = node

    def add_left(self, tree):
        self.root.left = tree

    def add_right(self, tree):
        self.root.right = tree

    @property
    def left(self):
        return self.root.left

    @property
    def right(self):
        return self.root.right

    def visit_first(self, fn):
        # 先序遍历
        try:
            fn(self.root._value)
            self.left.visit_first(fn)
            self.right.visit_first(fn)
        except:
            pass

    def visit_last(self, fn):
        # 后序遍历
        try:
            self.left.visit_last(fn)
            self.right.visit_last(fn)
        except:
            pass

        fn(self.root._value)

    def visit_mid(self, fn):
        # 中序遍历
        try:
            self.left.visit_mid(fn)
        except:
            pass

        fn(self.root._value)

        try:
            self.right.visit_mid(fn)
        except:
            pass

    def iter_visit_first(self, fn):
        # 栈先序遍历
        from datastruct.stack import Stack
        stack = Stack()

        stack.push(self)

        while True:
            p = stack.pop()

            fn(p.root._value)

            if p.right:
                stack.push(p.right)
            if p.left:
                stack.push(p.left)

            if not stack._top:
                break


if __name__ == '__main__':
    d = Tree(Nodes('D'))
    e = Tree(Nodes('E'))
    f = Tree(Nodes('F'))
    g = Tree(Nodes('G'))

    # h = Tree(Node('H'))
    # e.add_left(h)

    b = Tree(Nodes('B'))
    b.add_left(d)
    b.add_right(e)

    c = Tree(Nodes('C'))
    c.add_left(f)
    c.add_right(g)

    a = Tree(Nodes('A'))
    a.add_left(b)
    a.add_right(c)

    from functools import partial

    p = partial(print, end='')

    a.visit_first(p)
    print()
    a.visit_last(p)
    print()
    a.visit_mid(p)
    print()
    a.iter_visit_first(p)
