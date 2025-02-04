#include <iostream>
#include <windows.h>
#include <cstdint>

int main() {
    uintptr_t base_address = (uintptr_t)LoadLibraryA("C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe");
    std::cout << "Base Address: 0x" << std::hex << base_address << std::endl;
    return 0;
}
