# -*- coding: cp936 -*-
import ConvertPingYin
pp=raw_input('input')
pp=pp.decode('cp936')
cc=ConvertPingYin.CConvert().convert(pp)
print cc
