def score(plaintext: str) -> int:
    s = 0
    common = "ETAOINSHRDLU etaoinshrdlu"
    for c in plaintext:
        if c in common:
            s += 1
            
    return s
    
if __name__ == "__main__":
    raw_data = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    
    max_score = max_score1 = max_score2 = 0
    key = key1 = key2 = ""
    plaintext = plaintext1 = plaintext2 = ""
    for i in range(256):
        p = "".join([chr(b ^ i) for b in raw_data])
        s = score(p)
        if s > max_score:
            max_score2 = max_score1
            max_score1 = max_score
            max_score = s
            
            plaintext2 = plaintext1
            plaintext1 = plaintext
            plaintext = p
            
            key2 = key1
            key1 = key
            key = chr(i)
            
    print(f"k={key}, P=\"{plaintext}\", s={max_score}")
    print(f"k={key1}, P=\"{plaintext1}\", s={max_score1}")
    print(f"k={key2}, P=\"{plaintext2}\", s={max_score2}")
