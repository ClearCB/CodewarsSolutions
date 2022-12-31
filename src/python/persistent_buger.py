def persistence(n):
    n = str(n)
    mulpt_times = 0
    lenght = len(n)
    while lenght > 1:
        multp = 1
        for i in n:
            i_int = int(i)
            multp *= i_int
            n = str(multp)
            lenght = len(n)
        mulpt_times += 1
    return mulpt_times

persistence(39)