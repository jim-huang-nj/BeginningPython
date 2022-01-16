#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 解析器生成器.py
@time: 2020/11/17 15:47
"""
import datetime
c1 = datetime.datetime.now()
c2 = datetime.datetime.utcnow()
print(c1)
print(c2)
print(c1.date())
print(c1.time())
print(c1.timestamp() )
print(datetime.datetime.fromtimestamp(c1.timestamp()))
print(c1.isoweekday())
print(c1.isocalendar())
print(c1.strftime("%Y,%m,%d,%H,%M,%S"))