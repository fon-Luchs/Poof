import Poof_debugger


debugger = Poof_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.detach()
