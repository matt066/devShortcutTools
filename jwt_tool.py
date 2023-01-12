import jwt


def prepare_jwt():
    jwt_to_decoded = input('JWT: ')
    # encoded_jwt = jwt.encode(JSON, "secret", algorithm="HS256")
    # print(encoded_jwt)
    print(jwt.decode(jwt_to_decoded, options={"verify_signature": False}, algorithms=["HS256"]))
    # {'some': 'payload'}
