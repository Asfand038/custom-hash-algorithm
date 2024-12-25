from hash import string_to_ascii
from hash import custom_hash

input = "Hi, Im John"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"output: {hash}\n")

input = "Hi, im Johm"
print(f"input = {input}")
hash = custom_hash(string_to_ascii(input))
print(f"output: {hash}\n")

input = "Cryptography is the practice and study of techniques for secure communication in the presence of adversarial behavior."
print(f"input = {input[:64]}\n\t{input[64:]}")
hash = custom_hash(string_to_ascii(input))
print(f"output: {hash}\n")

input = "cryptography is the practice and study of techniques for secure communication in the presence of adversarial behavior."
print(f"input = {input[:64]}\n\t{input[64:]}")
hash = custom_hash(string_to_ascii(input))
print(f"output: {hash}\n")