#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jingyu Wang <badpasta@gmail.com>
# 
# Environment:
# Python by version 2.7.

def sqlZip(table_name, sql_data):
    return  map(lambda x: dict(zip(table_name, x)), sql_data)


# Pwoer by bufferx
def singleton(cls, *args, **kw):
    """Make Class Single
    """
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton
