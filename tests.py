from unary import encode, decode
import random

for i in range(100):
    print(i, 'is started')
    array = [random.randint(0, 10) for _ in range(5)]
    encoded = encode(array)
    decoded = decode(encoded)
    print(array)
    print(decoded)
    assert array == decoded
    print(i, 'is completed')
