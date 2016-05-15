#!/usr/bin/env python
# -*- coding: utf-8 -*-
class TypeSetter(object):
    def __init__(self, fieldtype):
        print("set attribute type {0}".format(fieldtype))
        self._fieldtype = fieldtype

    def is_valid(self, value):
        return isinstance(value, self._fieldtype)


class TypeCheckMeta(type):
    def __new__(cls, name, bases, dict):
        print('Allocating memory for class {0}'.format(name))
        print(name)
        print(bases)
        print(dict)
        return super(TypeCheckMeta, cls).__new__(cls, name, bases, dict)

    def __init__(cls, name, bases, dict):
        cls._fields = {}
        for key, value in dict.items():
            if isinstance(value, TypeSetter):
                cls._fields[key] = value


class TypeCheck(object):
    __metaclass__ = TypeCheckMeta
