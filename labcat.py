def mix_columns(state):
    # The AES MixColumns matrix
    matrix = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]

    # Perform matrix multiplication
    result = []
    for i in range(4):
        row = []
        for j in range(4):
            val = 0
            for k in range(4):
                val ^= mul(matrix[i][k], state[k][j])
            row.append(val)
        result.append(row)
    return result

def mul(a, b):
    # AES multiplication in Galois Field (GF)
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1B  # Rijndael's Galois field
        b >>= 1
    return p

def print_state(state):
    for row in state:
        print(' '.join(format(x, '02x') for x in row))

# Initialize the plaintext block as all-zero
plaintext_block = [[0] * 4 for _ in range(4)]

# Compute the output of MixColumns in Round 1
mix_columns_output = mix_columns(plaintext_block)

# Print the output
print("Output of MixColumns in Round 1:")
print_state(mix_columns_output)
