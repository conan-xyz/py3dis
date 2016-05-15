#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Field(object):
    def __init__(self, name, type):
        self.name = name
        self._type = type

    def __str__(self):
        return '{0}:{1}'.format(self.__class__.__name__, self.name)

    def __get__(self, instance, owner):
        print("Getting: %s" % self.name)
        return self.name

    def __set__(self, instance, value):
        print("Setting: %s" % value)
        if not instance(value, str):
            raise Exception('{0} must be str'.format(self.name))
        self.name = value

    def __delete__(self, instance):
        print("Deleting: %s" % self.name)
        del self.name
