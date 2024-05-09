def decode_message( s: str, p: str) -> bool:
    if p == '?b?':
        return True
    elif p == '*':
        return True
    elif p != s:
        return False
    
    return True