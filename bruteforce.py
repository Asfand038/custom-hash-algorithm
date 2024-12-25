from hash import string_to_ascii
from hash import custom_hash
import itertools
import time

def brute_force(hash):
    start_time = time.time()

    # Decide the range of ASCII values
    ascii_values = range(32, 127)

    # Convert ASCII values to characters
    characters = [chr(i) for i in ascii_values]

    # Generate and print all combinations
    for length in range(1,4):
        for combination in itertools.product(characters, repeat=length):
            combination = ''.join(combination)
            if custom_hash(string_to_ascii(combination)) == hash:
                end_time = time.time()
                print(f"original input: '{combination}' found in {end_time - start_time} seconds")
                return
        print(f"All combinations of length {length} checked.")
        
    end_time = time.time()
    print("Something went wrong") 


input = "a"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"hash = {hash}")
brute_force(hash)

print()

input = "hi"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"hash = {hash}")
brute_force(hash)

print()

input = "the"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"hash = {hash}")
brute_force(hash)

print()

input = "four"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"hash = {hash}")
brute_force(hash)

print()

input = "apple"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"hash = {hash}")
brute_force(hash)