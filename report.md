# Uhagre2

## x) Read/watch/listen and summarize

€ Schneier 2015: Applied Cryptography, 20ed
* **1.1 Terminology ("Historical Terms" to the end).** "Historically, a code refers to  cryptosystem that deals with linguistic units: words, phrases, sentences, and so forth." (Schneier 2015) He also mentions, "Codes are only useful for specialized circumstances. Ciphers are useful for any circumstance."
* **1.4 Simple XOR.** Actually I know this operation long time ago and I know how it works in encryption and decryption. One thing I learn from this chapter is that XOR is highly insecure when used with a short, repeating key because it preserves the underlying statistical patterns of the language (such as the frequency of specific letters). Schneier suggests the key beng used to be truly random, at least as long as the message itself, and never reused, to achieves perfect, unbreakable security.
* **1.7 Large Numbers.** In this section, by comparing large numbers used in keys to physical realities of the universe, Schneier explains that while a 128-bit or 256-bit key may seem small numerically, the total number of possible combinations is so vast that "brute-force" attacks (trying every possible key) are impossible by the fundamental laws of physics rather than just current technology. Schneier establishes that a well-designed modern cryptography is effectively unbreakable by raw calculation alone.

Karvinen 2024: [Python Basics for Hackers](https://terokarvinen.com/python-for-hackers/)
* Even though, Tero's guide is well writen and pretty detailed, but in my opinion, that is not enough to program the algorithms to decrypt ciphertexts. From my own experience, when dealing with a new programming language, not only we have to know the syntax, but we also have to research the libraries that we can use and the ecosystem around them. That's why in this homework, besides searching for how to program with Python on the Internet and using Tero's guide, especially how to use iPython, to practice, I have to use AI a lot to help me explain the syntax and usages of each function, as I'm just a beginner in this language.

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

## 6. Break repeating-key XOR

```shell
$ cat cryptopals/set1/6.txt | base64 -d | python3 breaking_repeating_key_xor.py
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 


```

## 7. AES in ECB mode

```bash
$ echo -n "YELLOW SUBMARINE" | od -A n -t x1 | sed 's/ *//g'
59454c4c4f57205355424d4152494e45
$ cat cryptopals/set1/7.txt | base64 -d | openssl enc -aes-128-ecb -d -K 59454c4c4f57205355424d4152494e45
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 

```

## 8. Detect AES in ECB mode

```bash
$ cat cryptopals/set1/8.txt | python3 detect_aes_128_ecb.py
Detected ECB-encrypted ciphertext with 3 repeated blocks:
d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a
```

## References
* Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C. 20th Anniversary Edition. Wiley.