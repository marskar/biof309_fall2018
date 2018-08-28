from this import s
from codecs import decode
def get_zen():
    with open('zen.txt', 'w') as f:
        return f.write(decode(s, "rot-13"))
