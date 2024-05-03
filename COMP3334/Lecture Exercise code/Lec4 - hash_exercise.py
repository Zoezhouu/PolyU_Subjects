import hashlib

def find_near_collision(n):
    prefix_length = n
    bucket_size = 2 ** n  # Number of buckets based on prefix length

    buckets = {}  # Dictionary to store the buckets
    message = 0

    while True:
        if (len(buckets) > bucket_size):
            print("cannot find collision")
            break
        message += 1
        hash_value = hashlib.sha256(bytes(message)).hexdigest()  # Compute the SHA-256 hash

        prefix = hash_value[:prefix_length]  # Extract the prefix

        if prefix in buckets:
            # Near collision found!
            full_hash_1 = buckets[prefix]
            full_hash_2 = hash_value
            return full_hash_1, full_hash_2

        buckets[message] = prefix  # Store the full hash in the corresponding bucket
        print(hash_value)


# Usage
collision1, collision2 = find_near_collision(34)
print("Near Collision 1:", collision1)
print("Near Collision 2:", collision2)