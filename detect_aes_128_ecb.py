import sys

"""
Google Gemini AI's response:
Here is the corrected approach and the code to implement it:

1. Read each hex-encoded line from the input file.
2. For each line, break the ciphertext into 16-byte blocks.
3. Count how many of these blocks are duplicates.
4. The ciphertext with the highest number of duplicate blocks is the one encrypted with ECB.
"""

def find_ecb_ciphertext(ciphertexts):
    """
    Finds the ciphertext that is most likely encrypted with AES in ECB mode.
    It does this by finding the ciphertext with the most repeated 16-byte blocks.
    """
    max_repeats = 0
    ecb_ciphertext = None

    for line in ciphertexts:
        line = line.strip()
        if not line:
            continue # Skip empty lines

        try:
            # The input is hex-encoded
            ciphertext = bytes.fromhex(line)
        except ValueError:
            continue # Skip lines that are not valid hex

        block_size = 16 # 128-bit
        blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
        
        # The number of repeated blocks is the total number of blocks minus the number of unique blocks
        num_blocks = len(blocks)
        num_unique_blocks = len(set(blocks))
        repeats = num_blocks - num_unique_blocks

        if repeats > max_repeats:
            max_repeats = repeats
            ecb_ciphertext = line
            
    return ecb_ciphertext, max_repeats

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    
    ecb_line, repeats = find_ecb_ciphertext(lines)

    if ecb_line:
        print(f"Detected ECB-encrypted ciphertext with {repeats} repeated blocks:")
        print(ecb_line)
    else:
        print("No ECB-encrypted ciphertext detected.")
