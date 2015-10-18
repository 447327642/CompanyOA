__author__ = 'ASUA'

for k in range(1, 11):
    total = 5
    h_count = 1
    v_count = 4
    com_count = 1
    s = ""
    for i in range(v_count + 1, total):
        com_count *= i
    for i in range(1, h_count):
        com_count /= i
    start = 0
    res_str = ""
    while start < total:
        start += 1
        if k > com_count:
            s += 'V'
            k -= com_count
            com_count = com_count * v_count / (total - start)
            v_count -= 1
        elif k == com_count:
            s += 'H'
            h_count -= 1
            s += 'V'* v_count
            if h_count > 0:
                s += 'H'* h_count
            break
        else:
            s += 'H'
            com_count = com_count * (total - start - v_count) / (total - start)
            h_count -= 1
    print s
    s = ""
