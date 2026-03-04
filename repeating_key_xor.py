def repeating_key_xor(p: str, k: str) -> str:
    p_raw = bytes(p, "ascii")
    k_raw = bytes(k, "ascii")
    
    raw_data = bytes([b1 ^ b2 for b1, b2 in zip(p_raw, k_raw * (len(p_raw) // len(k_raw) + 1))])
    return raw_data.hex()


if __name__ == "__main__":
    p = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    k = "ICE"
    res = repeating_key_xor(p, k)
    print(res)
 