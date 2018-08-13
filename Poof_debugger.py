from ctypes import *
from Poof_defines import *

import sys
import time

kernel32 = windll.kernel32


class debugger():
    def __init__(self):
        self.h_process       = None
        self.pid             = None
        self.debugger_active = False

    def load(self, path_to_exe):
        creation_flags = DBG_PROCESS
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startupinfo.dwFlags     = 0x1
        startupinfo.wShowWindow = 0x0
        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe,
                                         None,
                                         None,
                                         None,
                                         None,
                               creation_flags,
                                         None,
                                         None,
                           byref(startupinfo),
                  byref(process_information)):

            print "[*] We have successfully launched the process!"
            print "[*] The Process ID I have is: %d" % process_information.dwProcessId
            self.h_process = self.open_process(process_information.dwProcessId)

        else:
            print "[*] Error with error code %d" % kernel32.GetLastError()

    def open_process(self, pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, pid, False)
        return h_process

    def attach(self, pid):
        self.h_process = self.open_process(pid)
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
        else:
            print "[*] Unable to attach to the process"

    def detach(self):
        if kernel32.DebugActiveProcess(self.pid):
            print "[*] Finished debugging. Exiting..."
            return True
        else:
            print "[*] There was an error"
            return False
