import random
import string
import os

random.seed(42)

DATA_DIR = "/home/garan/code/C_Sharp/data"
CHARS = string.ascii_letters  # a-zA-Z full 52
LINE_LEN_FIELDS = 10
LINE_LEN_CHARS = 10
LINES_PER_FILE = 499_999

# 10 ranks, linear giảm 50/lần: 500, 450, 400, ..., 50
RANK_COUNTS = [500 - 50 * i for i in range(10)]  # [500, 450, ..., 50]
NUM_RANKS = len(RANK_COUNTS)
TOTAL_INJECTED_LINES = sum(RANK_COUNTS)  # 2750

# 10 shared popular tokens — dùng chung cho cả 10 file
SHARED_POPULAR = [
    'aBcDeFgHiJ',
    'KlMnOpQrSt',
    'UvWxYzAbCd',
    'EfGhIjKlMn',
    'OpQrStUvWx',
    'YzAbCdEfGh',
    'IjKlMnOpQr',
    'StUvWxYzAb',
    'CdEfGhIjKl',
    'MnOpQrStUv',
]

def rand_token():
    return ''.join(random.choices(CHARS, k=LINE_LEN_CHARS))

def gen_file(idx):
    path = os.path.join(DATA_DIR, f"da{idx}.dat")
    with open(path, 'w', buffering=1024*1024) as f:
        # inject 10 shared popular tokens with distinct counts
        for tok, count in zip(SHARED_POPULAR, RANK_COUNTS):
            for _ in range(count):
                line = [tok] + [rand_token() for _ in range(LINE_LEN_FIELDS - 1)]
                random.shuffle(line)
                f.write(';'.join(line))
                f.write('\n')
        # fill rest with all-random lines
        for _ in range(LINES_PER_FILE - TOTAL_INJECTED_LINES):
            f.write(';'.join(rand_token() for _ in range(LINE_LEN_FIELDS)))
            f.write('\n')

for i in range(1, 11):
    gen_file(i)
    print(f"da{i}.dat done")