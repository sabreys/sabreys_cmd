import hashlib
import sys
from Cryptodome.Cipher import AES


def main():
    if sys.argv[1] == "help":
        print("usage: decrypt file_name key skey.bin_path")
    else:
        file = open(sys.argv[1], "rb+")

        password = str.encode(sys.argv[2])
        key = hashlib.md5(password).digest()

        file_i = open(sys.argv[3], "rb")  # skey.bin file path
        nonce, tag= [file_i.read(x) for x in (16, 16)]

        cipher = AES.new(key, AES.MODE_EAX, nonce)
        try:
          data = cipher.decrypt_and_verify(file.read() , tag)
          file.seek(0)
          file.write(data)
          file.close()
        except ValueError as e:
          print('skey.bin file not match!!!')
          return

        print("\nsuccesfull\n")


if __name__ == "__main__":
    main()
