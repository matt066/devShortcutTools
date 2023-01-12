import base64
import sys


def encode_decode_base64():
    try:
        option = int(input('Encode(1) or Decode(2)?'))
    except Exception as e:
        return 'Finish with errors: Invalid option', e

    if option == 1:
        # Encode string
        e = input('Encode: ')
        encodedBytes = base64.b64encode(e.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")

        return "Encoded String:", encodedStr

    elif option == 2:
        # Decode string
        d = input('Decode: ')

        try:
            decodedBytes = base64.b64decode(d)
            decodedStr = str(decodedBytes, "utf-8")
            print("Decoded String:", decodedStr)

        except Exception as e:
            return e
            # sys.exit()

    elif option > 2 or isinstance(option, str):
        return 'Invalid option'


def encode_base64(e):
    try:
        encoded_bytes = base64.b64encode(e.encode("utf-8"))
        encoded_str = str(encoded_bytes, "utf-8")

        return "Encoded String:", encoded_str

    except Exception as e:
        return e


def decode_base64(d):
    try:
        decoded_bytes = base64.b64decode(d)
        decoded_str = str(decoded_bytes, "utf-8")
        return "Decoded String:", decoded_str

    except Exception as e:
        return e
