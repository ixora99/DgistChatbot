# -*- coding: utf8 -*-

import datetime

to=datetime.datetime(2020,3,2,9,0)

middle_time=datetime.datetime(2020,4,13,0,0)


def check():
    now=datetime.datetime.now()
    diff=to-now
    day=diff.days
    hour=diff.seconds//3600
    minute=(diff.seconds%3600)//60
    second=(diff.seconds%3600)%60

    return str(day)+"일"+str(hour)+"시간"+str(minute)+"분"+str(second)+"초"

def middledday():
    now=datetime.datetime.now()
    diff=middle_time-now
    day=diff.days
    hour=diff.seconds//3600
    minute=(diff.seconds%3600)//60
    second=(diff.seconds%3600)%60

    return str(day)+"일"+str(hour)+"시간"+str(minute)+"분"+str(second)+"초"
