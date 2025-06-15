import argparse
from hashes import *

#parser
parser = argparse.ArgumentParser(description="HashBuster", epilog="Crack hashes with ease!")

parser.add_argument("--algo", help="Hash the string using which algorithm? (Supported: md5, sha1, sha224, sha256, sha384, sha512)")
parser.add_argument("--w", help="String to hash.")
parser.add_argument("--hash" , help="Give the hash" , default=None) 
parser.add_argument("--list", help="Provide wordlist", default=None)

args = parser.parse_args()

# hash a string
if args.algo and not args.w or not args.algo and args.w:
    print("Error: Both --algo and --w arguments are required.")
    exit(1) 
if args.algo and args.w:
    a = args.algo + "_hash"
    if a not in globals():
        print(f"Error: Hash type '{args.algo}' is not supported.")
        exit(1)
    else:
        print(f"Algorithm: {args.algo}")
        print("Hash: ", globals()[a](args.w))
        exit(0)
        


# crack a hash
if args.list and not args.hash or not args.list and args.hash:
    print("Error: Both --list and --hash arguments are required.")
    exit(1)
if args.hash and args.list:
    algo = ret_algo(args.hash)
    a = algo + "_hash"
    if algo == "unknown" or algo is None:
        print("Error: Hash type is unknown. Please provide a valid hash.")
        exit(1)
    try:
        with open(args.list, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if a not in globals():
                        print(f"Error: Hash type '{algo}' is not supported.")
                        exit(1)
                    else:
                        if globals()[a](line) == args.hash:
                            print(f"Hash type: {algo}")
                            print(f"Hash cracked: {line}")
                            break      
            else:
                print("Hash not found in the wordlist.")                     
    except FileNotFoundError:
        print(f"Error: Wordlist file '{args.list}' not found.")
        exit(1)
    except PermissionError:  # ADDED: Handle permission errors
        print(f"Error: Permission denied accessing '{args.list}'.")
        exit(1)
    except UnicodeDecodeError:  # ADDED: Handle encoding errors
        print(f"Error: Cannot read '{args.list}'. File encoding issue.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
