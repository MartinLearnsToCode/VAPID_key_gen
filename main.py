from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64

# Generate a new EC private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Export the private key in base64url format
vapid_private_key = base64.urlsafe_b64encode(
    private_key.private_numbers().private_value.to_bytes(32, 'big')
).rstrip(b'=').decode('utf-8')
print("VAPID Private Key:", vapid_private_key)

# Derive the public key from the private key
public_key = private_key.public_key()

# Export the public key in uncompressed point format as required for VAPID
public_numbers = public_key.public_numbers()
x = public_numbers.x.to_bytes(32, 'big')
y = public_numbers.y.to_bytes(32, 'big')
vapid_public_key = base64.urlsafe_b64encode(b'\x04' + x + y).rstrip(b'=').decode('utf-8')
print("VAPID Public Key:", vapid_public_key)
