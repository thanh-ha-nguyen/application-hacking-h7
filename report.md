# Uhagre2

## x) Read/watch/listen and summarize

TBD

## 1. Convert hex to base64

```python
In [1]: import base64

In [2]: bytes.fromhex("49276d206b696c6c696e6720796f757220627261696
   ...: e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
Out[2]: b"I'm killing your brain like a poisonous mushroom"

In [3]: base64.b64encode(bytes.fromhex("49276d206b696c6c696e672079
   ...: 6f757220627261696e206c696b65206120706f69736f6e6f7573206d75
   ...: 7368726f6f6d"))
Out[3]: b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
```

## 2. Fixed XOR

```shell
$ python3 fixed_xor.py
746865206b696420646f6e277420706c6179
```

## 3. Single-byte XOR cipher

```shell
$ python3 single_byte_xor_cipher.py
k=X, P="Cooking MC's like a pound of bacon", s=23
k=R, P="Ieeacdm*GI-y*fcao*k*zedn*el*hkied", s=17
k=D, P="_sswur{<Q_;o<puwy<}<lsirx<sz<~}sr", s=13
```

## 4. Detect single-character XOR

```shell
$ python3 detect_single_character_xor.py
k="5", P="Now that the party is jumping
", s=22
k="     ", P="rSKHT]HHTYL]NHEUOVIQLUR[6", s=17
lKu*e_HP="HTADSOO{Dl
nXdLm", s=16
```

## 5. Implementing repeating-key XOR

```shell
$ python3 repeating_key_xor.py
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```