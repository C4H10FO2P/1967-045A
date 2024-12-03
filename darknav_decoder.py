def decrypt_message(data):
    partial_key = "0x1F" # (fragment)
    return "".join([chr(ord(c) ^ int(partial_key, 16)) for c in data])
