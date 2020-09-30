
import sys
import hashlib
from Cryptodome.Cipher import AES


def main():
  if sys.argv[1] == "help":
        print("usage: encrypt file_name key skey_file_name")
  else:
    filem = open(sys.argv[1], "rb+")
    inside = filem.read()

    password = str.encode(sys.argv[2])
    key = hashlib.md5(password).digest()
    cipher = AES.new(key, AES. MODE_EAX)
    ciphertext , tag = cipher.encrypt_and_digest(inside)
    print("key=", key)

    # print(f.decrypt(token))
    filem.seek(0)
    filem.write(ciphertext)
    filem.close()

    file_out = open(sys.argv[3], "wb")
    [file_out.write(x) for x in (cipher.nonce, tag)]
    file_out.close()
    print("\nsuccesfull. save your",sys.argv[3], "file. it's private key to encrypt \n")

if __name__ == "__main__":
    main()
