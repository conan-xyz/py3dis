#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Field(object):
    def __init__(self, name, type):
        self.name = name
        self._type = type

    def __str__(self):
        return '{0}:{1}'.format(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

    def is_valid(self):
        return isinstance(self.name, (str, unicode))


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

    def is_valid(self):
        return isinstance(self.name, (int, long))


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':  # 排除对Model类的修改
            return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)

        print('Found model: {0}'.format(name))

        mappings = dict()

        for k, v in attrs.items():  # 查找生成类的所有属性并保存到mappings
            if isinstance(v, Field):
                print('Found mapping: {0} ==> {1}'.format(k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return super(ModelMetaclass, cls).__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def save(self):
        # print self
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into {0} {1} values {2}'.format(self.__table__, ','.join(fields), ','.join(params))
        print('SQL: {0}'.format(sql))
        print('ARGS: {0}'.format(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User()
u.id = 12345
u.name = 'Michael'
u.email = 'test@orm.org'
u.password = 'my-pwd'

# 保存到数据库：
u.save()
