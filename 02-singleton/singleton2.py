# -*- coding: utf-8 -*-
# @FileName : singleton2.py
# @Time : 2024/6/3 22:26
# @Author : Alves

"""
 为基础设施提供运行状况监测服务。创建HealthChecker类，它作为单例实现。
 还维护一个被监控的服务器列表。当一个服务器从这个列表中删除时，监控软件应该觉察这一情况，并从被监控的服务器列表中将其删除。
"""


class HealthChecker:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(HealthChecker, cls).__new__(cls, *args, **kwargs)
        return HealthChecker.__instance

    def __init__(self):
        self._servers = []

    def add_server(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def change_server(self):
        self._servers.pop()
        self._servers.append("Server 5")

    @property
    def servers(self):
        return self._servers


if __name__ == '__main__':
    health_checker1 = HealthChecker()
    health_checker2 = HealthChecker()
    health_checker1.add_server()
    print("Schedule health check for server (1)..")
    for i in range(4):
        print("Checking ", health_checker1._servers)

    health_checker2.change_server()
    print("Schedule health check for server (2)..")
    for i in range(4):
        print("Checking ", health_checker2._servers)
