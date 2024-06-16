# -*- coding: utf-8 -*-
# @FileName : event_manager.py
# @Time : 2024/6/16 9:37
# @Author : Alves

"""
 假设你要在家中举办一场婚礼，你必须预定一家酒店或场地，与餐饮人员交代韭菜、布置场景，并且安排背景音乐。
 从门面模式的角度看待这件事情：
 客户端：你需要在婚礼前及时完成所有的准备工作。每一项的安排都是顶级的，这样客人才会喜欢这些活动。
 门面：会务经理负责与所有相关的人员进行交涉，这些人员负责处理食物、花卉装饰等。
 子系统：它们代表提供餐饮、酒店管理和花卉装饰等服务系统。
"""
"""
 EventManager扮演着门面角色，它将客户请求委托给子系统对象。
"""


class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")

    def arrange_event(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


"""
 Hotelier类应用于预订酒店
 Florist类负责花卉装饰
 Caterer类用于跟备办宴者打交道，并负责安排餐饮
 Musician类用于安排婚礼的音乐
"""


class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def _is_available(self):
        print("Hotelier: Checking if the hotel is free")
        return True

    def book_hotel(self):
        if self._is_available():
            print("Registered the Booking\n\n")


class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def set_flower_requirements(self):
        print("Carnations, Ross and Lilie would be used for Decorations\n\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event? --")

    def set_cuisine(self):
        print("Chinese & Continental Cuisine would be served\n\n")


class Musician(object):
    def __init__(self):
        print("Music Arrangements for the Marriage? --")

    def set_music_type(self):
        print("Jazz and Classical will be played\n\n")


class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements?!!!")

    def ask_event_manager(self):
        print("You:: Let's start the Marraige Preparations")
        event_manager = EventManager()
        event_manager.arrange_event()

    def __del__(self):
        print("You:: Thanks to Event Manager for making it happen!")


you = You()
you.ask_event_manager()

