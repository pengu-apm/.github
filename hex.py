#!/usr/bin/python3

offset = 64
padding = b"\x41" * offset
eip = b"\x42\x42\x42\x42"
payload = b"\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21\x0a"

run = padding + eip + payload

print(run)
