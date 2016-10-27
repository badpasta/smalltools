#!/usr/bin/env python
#
# Author: Jingyu Wang <badpasta@gmail.com>
# 
# Environment:
# -*- coding: utf-8 -*-
# Python by version 2.7.

from parseConfig import AdvancedOptions,OtherOptions


kw = {'aa': dict(bb='cc')}
op = OtherOptions()
op.addParam('aa')
for key, value in kw['aa'].items():
    op.aa.define(key, value)

print op.aa.bb
