### Dependencies
* Python 3.6 or later

### Install
```bash
$ pip3 install su.aes
```

### Usage
```python
from su.aes import encrypt, decrypt

input_text = "nihao"
secret_key = "my_sec_key"

encrypted = encrypt(secret_key, input_text)
decrypted = decrypt(secret_key, encrypted)

assert decrypted == input_text
```


### Console
```bash
# test for input string
$ su-aes INPUT_STR -t -p

# file test
$ su-aes INPUT_FILE_PATH -f -t -o OUTPUT_FILE_PATH
```
