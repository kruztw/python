#!/usr/bin/env python2

#encoding: utf-8

__import__('__builtin__', level=0)                                    # 取得 __builtin__ 函式集
__import__('__builtin__', level=0).__dict__['print']                  # 拿出 print 
__import__('__builtin__', level=0).__dict__['print']("hello world")
