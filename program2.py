def decode_message(s: str, p: str) -> bool:
    message_index = 0
    key_index = 0
    while message_index < len(s) and key_index < len(p):
        if p[key_index] == '*':
            
            while message_index < len(s) and p[key_index] == '*':
                message_index += 1
            key_index += 1
        elif p[key_index] == '?':
           
            message_index += 1
            key_index += 1
        elif s[message_index] != p[key_index]:
           
            return False
        else:
            message_index += 1
            key_index += 1
    
    
    if message_index < len(s) or key_index < len(p):
        return False
    
    return True
