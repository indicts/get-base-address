# get-base-address

This shows how to get a process's base address from user mode, even with anti-cheat protections. It includes C++ and Python examples. This method is less suspicious to ACs than using a kernel driver in a suspicious memory area.

## Usage

### C++ Example

```cpp
#include <iostream>
#include <windows.h>
#include <cstdint>

int main() {
    uintptr_t base_address = (uintptr_t)LoadLibraryA("C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe");
    std::cout << "Base Address: 0x" << std::hex << base_address << std::endl;
    return 0;
}
```

### Python Example

```py
import ctypes

path = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe"

ctypes.windll.kernel32.LoadLibraryA.restype = ctypes.c_void_p

base_address = ctypes.windll.kernel32.LoadLibraryA(path.encode('utf-8'))

print(f"Base Address: {hex(base_address)}")
```
