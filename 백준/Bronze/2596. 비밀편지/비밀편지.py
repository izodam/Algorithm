code_dict = {
    '000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
}

unseen_code_dict = dict()
N = int(input())
cryptogram = input().strip()


def correction_code(code):
    for candidate, val in code_dict.items():
        diff = 0
        for i in range(6):
            diff += 0 if code[i] == candidate[i] else 1
        if diff == 1:
            return val

    raise ValueError()


def check_code(code, t):
    if code in code_dict:
        return code_dict[code]

    try:
        _code = correction_code(code)
        return _code

    except:
        return str(t)

result = ''
for i in range(N):
    code = check_code(cryptogram[i * 6:i * 6 + 6], i + 1)
    if code == str(i + 1):
        result = code
        break
    result += code

print(result)