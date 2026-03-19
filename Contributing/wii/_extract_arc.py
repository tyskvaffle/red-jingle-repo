import sys

SRC, DST = sys.argv[1], sys.argv[2]

MAGIC = b'\x55\xaa\x38\x2d'

with open(SRC, 'rb') as f:
    data = f.read()

offset = data.find(MAGIC)
if offset == -1:
    print("Could not find U8 header.")
    sys.exit(1)

with open(DST, 'wb') as f:
    f.write(data[offset:])
