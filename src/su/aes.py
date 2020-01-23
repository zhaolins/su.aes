from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify, unhexlify
import os

__all__ = ["encrypt", "decrypt", "main"]

MODE = AES.MODE_CTR
BS = AES.block_size
KS = AES.key_size[-1]


def _pad_bytes(byte_str, size):
    if len(byte_str) > size:
        return byte_str[:size]
    return byte_str.ljust(size)


def encrypt(key, data, output_binary=False):
    byte_key = bytes(key, 'utf-8') if not isinstance(key, bytes) else key
    encrypt_key = _pad_bytes(byte_key, KS)
    byte_data = bytes(data, 'utf-8') if not isinstance(data, bytes) else data
    counter_prefix = os.urandom(BS)

    cipher = AES.new(encrypt_key, MODE, counter=Counter.new(BS * 8))
    byte_result = counter_prefix + cipher.encrypt(byte_data)
    if output_binary:
        return byte_result
    return hexlify(byte_result).decode()


def decrypt(key, data, is_hex_input=True, output_binary=False):
    byte_key = bytes(key, 'utf-8') if not isinstance(key, bytes) else key
    encrypt_key = _pad_bytes(byte_key, KS)
    input_byte_data = bytes(data, 'utf-8') if not isinstance(data, bytes) else data
    byte_data = unhexlify(input_byte_data) if is_hex_input else input_byte_data

    counter_prefix = byte_data[:BS]
    ciphertext = byte_data[BS:]

    cipher = AES.new(encrypt_key, MODE, counter=Counter.new(BS * 8))
    byte_result = cipher.decrypt(ciphertext)
    if output_binary:
        return byte_result
    return byte_result.decode()


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser('A simple encrypt/decrypt lib based on AES.\n')
    parser.add_argument('data')
    parser.add_argument('-k', '--key', dest='key', default='123キー　你 好\xb6$')
    parser.add_argument('-o', '--output', dest='output', default='')
    parser.add_argument('-d', '--decrypt', dest='is_decrypt', default=False, action='store_true')
    parser.add_argument('-f', '--is_file', dest='is_file', default=False, action='store_true')
    parser.add_argument('-p', '--print', dest='print', default=False, action='store_true')
    parser.add_argument('-t', '--is_test', dest='is_test', default=False, action='store_true')
    options = parser.parse_args()

    if options.is_file:
        with open(options.data, 'rb') as f:
            input_data = f.read()
    else:
        input_data = options.data

    print(f'key: {options.key}')
    input_preview = f'{input_data[:10]}...{input_data[-10:]}' if len(input_data) > 30 else input_data
    print(f'input: {input_preview}')

    if options.is_test:
        encrypted = encrypt(options.key, input_data, output_binary=options.is_file)
        options.print and print('encrypted: ', encrypted)
        decrypted = decrypt(options.key, encrypted, is_hex_input=not options.is_file, output_binary=options.is_file)
        options.print and print('decrypted: ', decrypted)
        assert input_data == decrypted
        output = encrypted
        print('test passed')
    elif not options.is_decrypt:
        output = encrypted = encrypt(options.key, input_data)
        options.print and print('encrypted: ', encrypted)
    else:
        output = decrypted = decrypt(options.key, input_data, is_hex_input=not options.is_file,
                                     output_binary=options.is_file)
        options.print and print('decrypted: ', decrypted)

    if options.output:
        with open(options.output, 'wb') as f:
            f.write(output)
        print(f'output: {options.output}')


if __name__ == '__main__':
    main()
