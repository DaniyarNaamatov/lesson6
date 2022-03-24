def get_palindrome_no_less_than(n):
    sn = str(n)
    if len(sn) % 2 == 0:
        half_sn = sn[ : len(sn)//2 : ]
        sn_new = half_sn + half_sn[::-1]
        while sn_new < sn:
            n_half = int(half_sn)
            n_half += 1
            half_sn = str(n_half)
            sn_new = half_sn + half_sn[::-1]
            if len(sn_new) > len(sn):
                sn_new = half_sn[:-1] + half_ns[::-1]
    else:
        half_sn = sn[ : len(sn)//2 + 1 : ]
        sn_new = half_sn[:-1] + half_sn[::-1]
        while sn_new < sn:
            n_half = int(half_sn)
            n_half += 1
            half_sn = str(n_half)
            sn_new = half_sn[:-1] + half_sn[::-1]
            if len(sn_new) > len(sn):
                half_sn = half_sn[:-1]
                sn_new = half_sn + half_sn[::-1]
    return int(sn_new)

def main():
    n = int(input('n = '))
    res = get_palindrome_no_less_than(n + 1)
    print(res)
main()