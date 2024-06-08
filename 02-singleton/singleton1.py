# -*- coding: utf-8 -*-
# @FileName : singleton1.py
# @Time : 2024/6/3 22:26
# @Author : Alves

"""
单例模式：
    1. 单例模式（Singleton Pattern）是使用一个类只有一个实例的类设计模式。
    2. 单例模式确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例。
    3. 单例模式是简单工厂模式的变种，简单工厂模式是创建型模式，而单例模式是结构型模式。

    通过数据库应用程序来展示单例的应用
    完整的云服务被分解为多个服务，每个服务执行不同的数据库操作。
    1. 数据库操作的一致性，即一个操作不应与其他操作发生冲突
    2.优化数据库的各种操作，以提高内存和cpu的利用率
"""

import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)


