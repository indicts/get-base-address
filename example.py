import ctypes

path = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe"

ctypes.windll.kernel32.LoadLibraryA.restype = ctypes.c_void_p

base_address = ctypes.windll.kernel32.LoadLibraryA(path.encode('utf-8'))

print(f"Base Address: {hex(base_address)}")
