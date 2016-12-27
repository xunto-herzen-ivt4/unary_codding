from unary import encode, decode
import random

for i in range(100):
    print(i, 'is started')
    array = [random.randint(0, 100) for _ in range(200)]
    encoded = encode(array)
    decoded = decode(encoded)
    assert array == decoded
    print(i, 'is completed')
