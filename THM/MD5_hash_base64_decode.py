import hashlib
import base64

# Phrase to hash
phrase = "Insecure Algorithms"

# Generate MD4 hash
md4_hash = hashlib.new('md4', phrase.encode('utf-8')).digest()

# Encode hash in base64
md4_hash_base64 = base64.b64encode(md4_hash).decode('utf-8')
print(md4_hash_base64)
