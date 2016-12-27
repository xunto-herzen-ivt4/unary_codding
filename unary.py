def encode(data: list):
    # Encode phrase
    result = []
    for number in data:
        result = result + (number * [1]) + [0]

    return result


def decode(encoded_data: list):
    result = []

    accumulate = 0

    for number in encoded_data:
        if number == 0:
            result.append(accumulate)
            accumulate = 0
        else:
            accumulate += number

    return result
