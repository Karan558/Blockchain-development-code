import hashlib
import json

def crypto_hash(*args):


    "Return a sha-256 hash of the given arguments."


    # Converts number 2 to string "2"
    stringified_args = map(lambda data: json.dumps(data), args)

    print(f'args: {args}')
    joined_data = ''.join(stringified_args)
    print(f'Joined_data: {joined_data}')
    #Converts to computer numbers: [50]  .encode('utf-8')

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"Crypto_hash('One', 2 , [3]): {crypto_hash('one',2 ,[3])}")
    print(f"Crypto_hash(2,'one', [3]): {crypto_hash(2,'one' ,[3])}")

if __name__ == '__main__':
    main()