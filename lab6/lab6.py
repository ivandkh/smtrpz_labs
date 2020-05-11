import argparse

parser = argparse.ArgumentParser(description='Caesar cipher.')
parser.add_argument('key', type=str, help='Cipher key value.')
parser.add_argument('msg', type=str, help='Message to encode.')
parser.add_argument('-d', '--dec', action='store_true', help='Decode mode.')
args = parser.parse_args()

alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
nltrs = len(alph)

if len(args.key) > 1 or args.key not in alph:
    raise Exception('Expected a Latin character as a `key`.')
key = alph.index(args.key)


def encode(x):
    if x.isspace():
        return x

    shift = alph.index(x) + key
    if shift >= nltrs:
        shift -= nltrs

    return alph[shift]


def decode(x):
    if x.isspace():
        return x

    shift = alph.index(x) - key
    if shift >= nltrs:
        shift -= nltrs

    return alph[shift]


print(''.join(map(decode if args.dec else encode, args.msg)))
