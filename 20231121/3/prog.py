import sys
import struct

a = sys.stdin.buffer.read()
length = len(a)
if length < 44:
    print('NO')
    exit()

ans = [
    struct.unpack("i", a[4:8])[0],
    struct.unpack("h", a[20:22])[0],
    struct.unpack("h", a[22:24])[0],
    struct.unpack("i", a[24:28])[0],
    struct.unpack("h", a[34:36])[0],
    struct.unpack("i", a[40:44])[0]
]

d = {
    str(slice(0, 4)): b'RIFF',
    str(slice(4, 8)): struct.pack('i', length - 8),
    str(slice(8, 12)): b'WAVE',
    str(slice(12, 16)): b'fmt ',
    str(slice(16, 20)): b'\x10\x00\x00\x00',
    str(slice(24, 28)): {b'D\xac\x00\x00', b'\x80\xbb\x00\x00'},
    str(slice(28, 32)): struct.pack('q', (ans[2] * ans[3] * ans[4]) >> 3),
    str(slice(32, 34)): {b'\x01\x00', b'\x02\x00', b'\x04\x00'},
    str(slice(36, 40)): b'data',
    str(slice(40, 44)): struct.pack('i', length - 44)
}

flag = False
for i in d.keys():
    exec(f'flag = ((a[{i}] not in d[str({i})]))')
    if flag:
        print('NO')
        exit()
if struct.unpack('h', a[32:34])[0] != ((ans[4] * ans[2]) >> 3):
    print('NO')
    exit()

print('Size={}, Type={}, Channels={}, Rate={}, Bits={}, Data size={}'.format(*ans))
