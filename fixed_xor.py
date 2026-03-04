def fixed_xor(a: str, b: str) -> str:
    a_raw = bytes.fromhex(a)
    b_raw = bytes.fromhex(b)
    raw = bytes([b1 ^ b2 for b1, b2 in zip(a_raw, b_raw)])
    return raw.hex()

if __name__ == "__main__":
    res = fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
    print(res)
 