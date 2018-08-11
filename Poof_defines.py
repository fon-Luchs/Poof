from ctypes import *

# MICROSOFT TYPES
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# CONSTANTS
DBG_PROCESS = 0x00000001
CRT_NEW_CONSOLE = 0x00000010

# STRUCTURES FOR CreateProcessA() FUNCTION


class STARTUPINFO(Structure):
    _fields_ = [
        ("cd", DWORD),
        ("lpReserved", LPTSTR),
        ("lpDesktop", LPTSTR),
        ("lpTitle", LPTSTR),
        ("DwX", DWORD),
        ("DwY", DWORD),
        ("DwXSize", DWORD),
        ("DwYSize", DWORD),
        ("DwXCountChars", DWORD),
        ("DwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", DWORD),
        ("cbReserved2", DWORD),
        ("lpReserved2", DWORD),
        ("hStdInput", DWORD),
        ("hStdOutput", DWORD),
        ("hStdError", DWORD)
    ]


class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD)
    ]