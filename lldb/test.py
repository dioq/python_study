#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import lldb
import os

def test():
    debugger = lldb.debugger.SBDebugger.Create()
    target = debugger.CreateTarget('')
    error = lldb.SBError()
    process = target.AttachToProcessWithName(debugger.GetListener(), 'PROCESS_NAME', False, error)

    debugger.HandleCommand("process connect connect://127.0.0.1:8090")
    debugger.SetAsync (False)


if __name__ == '__main__':
    test()
