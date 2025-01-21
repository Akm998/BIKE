import numpy as np

def generate_random_binary_string(length):
    return np.random.randint(2, size=length).tolist()

def key_generation(length):
    h0 = generate_random_binary_string(length)
    h1 = generate_random_binary_string(length)
    public_key = (h0, h1)
    secret_key = (h0, h1)
    return public_key, secret_key

def encode(message, public_key):
    h0, h1 = public_key
    e = generate_random_binary_string(len(h0))
    c = [(m ^ e[i]) for i, m in enumerate(message)]
    return c, e  # Return the error vector for debugging

def decode(ciphertext, secret_key, error_vector):
    h0, h1 = secret_key
    decoded_message = [(c ^ error_vector[i]) for i, c in enumerate(ciphertext)]
    return decoded_message

def main():
    length = 256  # Example length, should be according to BIKE parameters
    public_key, secret_key = key_generation(length)
    
    # Predefined message
    message = [255, 195, 5]  # Example numerical values
    
    # Convert numerical message to binary
    message_binary = []
    for num in message:
        message_binary.extend([int(bit) for bit in format(num, '08b')])
    
    # Pad message to fit length
    message_binary = (message_binary + [0] * (length - len(message_binary)))[:length]

    ciphertext, error_vector = encode(message_binary, public_key)
    decrypted_message_binary = decode(ciphertext, secret_key, error_vector)

    # Convert binary to numerical values
    decrypted_message = [int(''.join(map(str, decrypted_message_binary[i:i+8])), 2) for i in range(0, len(decrypted_message_binary), 8) if i + 8 <= len(decrypted_message_binary)]
    decrypted_message = decrypted_message[:len(message)]  # Truncate to original message length

    print("Original message (numerical):", message)
    print("Binary message:", message_binary)
    print("Ciphertext:", ciphertext)
    print("Error vector:", error_vector)
    print("Decrypted message (binary):", decrypted_message_binary)
    print("Decrypted message (numerical):", decrypted_message)

if __name__ == "__main__":
    main()
