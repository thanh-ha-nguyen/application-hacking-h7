from sys import stdin

def hamming_distance(raw1: bytes, raw2: bytes):
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(raw1, raw2))

def find_keysize(raw: bytes, max_keysize = 40):
    value = float('inf')
    keysize = 0
    for size in range(2, max_keysize + 1):
        distances = []
        # Based on instructions, we should add [:4] at the end.
        # However, it seems 4 sammples are not enough to find the key size.
        # So I suggest using all the samples that can be calculated instead
        chunks = [raw[i:i+size] for i in range(0, len(raw), size)]#[:4]
        if len(chunks) < 2:
            continue
            
        for i in range(len(chunks) - 1):
            distances.append(hamming_distance(chunks[i], chunks[i+1]) / size)
            
        avg_distance = sum(distances) / len(distances)
        
        if avg_distance < value:
            value = avg_distance
            keysize = size    

    # print(f"keysize={keysize} value={value}")
    return keysize

def score(plaintext: str):
    s = 0
    common = "ETAOINSHRDLU etaoinshrdlu"
    for c in plaintext:
        if c in common:
            s += 1            
    return s

def detect_single_byte_xor(raw: bytes):
    max_score = 0
    single_byte = 0
    for i in range(256):
        p = "".join([chr(b ^ i) for b in raw])
        s = score(p)
        if s > max_score:
            max_score = s
            single_byte = i   
    return single_byte

def find_key(raw: bytes, keysize: int):
    key_bytes = []
    for j in range(keysize):
        block = raw[j::keysize]
        key_bytes.append(detect_single_byte_xor(block))
    return bytes(key_bytes)
    
def repeating_key_xor(p: bytes, k: bytes):
    return bytes([b1 ^ b2 for b1, b2 in zip(p, k * (len(p) // len(k) + 1))])

if __name__ == '__main__':
    ciphertext = stdin.buffer.read()
    keysize = find_keysize(ciphertext)
    key = find_key(ciphertext, keysize)
    plaintext = repeating_key_xor(ciphertext, key)
    print(plaintext.decode())