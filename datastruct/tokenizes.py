#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Token(object):
    # 左括号、右括号、符号、表达式，SYMBOLS逻辑符号
    LEFT_BRACKETS = 'LEFT_BRACKETS'
    RIGHT_BRACKETS = 'RIGHT_BRACKETS'
    SYMBOL = 'SYMBOL'
    EXPRESSION = 'EXPRESSION'
    SYMBOLS = '&|!'

    # token的两个属性，一个值，一个类型。
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):  # 人类可视的方法，对人友好，str()可调用这个方法
        return '{0}<{1}>'.format(self.value, self.type)

    def __repr__(self):  # 机器可是的方法，对机器友好，print()调用这个方法
        return self.__str__()


def tokenize(origin):
    tokens = []
    is_expr = False  # flags标签
    expr = []
    for c in origin:
        if c == '#':
            # 如果表达式的flags是False，就把flags置为True
            if not is_expr:
                is_expr = True
            # 如果表达式的flags是True， 就把flags置为False
            else:
                is_expr = False
                value = ''.join(expr)
                token = Token(value, Token.EXPRESSION)
                tokens.append(token)
                expr = []
        elif c in Token.SYMBOLS and not is_expr:
            token = Token(c, Token.SYMBOL)
            tokens.append(token)
        elif c == '(' and not is_expr:
            token = Token(c, Token.LEFT_BRACKETS)
            tokens.append(token)
        elif c == ')' and not is_expr:
            token = Token(c, Token.RIGHT_BRACKETS)
            tokens.append(token)
        elif is_expr:
            expr.append(c)
            # 空格这里直接不判断，相当于丢弃了
    return tokens

# 测试代码：
if __name__ == '__main__':
    e = '#test# & #abc# | (!#123# | #456#)'
    # print(str(x) for x in tokenize(e))
    print(tokenize(e))
