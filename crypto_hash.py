import hashlib
import json

def crypto_hash(data):
    "Return a sha-256 hash of the given data."

    # Converts number 2 to string "2"
    stringified_data = json.dumps(data)

    #Converts to computer numbers: [50]  .encode('utf-8')

    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

def main():
    print(f"Crypto_hash([2]): {crypto_hash([2])}")
    print(f"Crypto_hash([2]): {crypto_hash(1)}")

if __name__ == '__main__':
    main()