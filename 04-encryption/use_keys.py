import rsa

public_file = open("keys/public.txt", "r")
public_data = public_file.read()
public_key = rsa.PublicKey.load_pkcs1(public_data, "PEM")


private_file = open("keys/private.txt", "r")
private_data = private_file.read()
private_key = rsa.PrivateKey.load_pkcs1(private_data, "PEM")

message = "Hello World!"

message_bytes = message.encode('utf8')
print(message_bytes)

message_encrypted = rsa.encrypt(message_bytes, public_key)
print(message_encrypted)

message_bytes_decrypted = rsa.decrypt(message_encrypted, private_key)

original_message = message_bytes_decrypted.decode('utf8')

print(original_message)
