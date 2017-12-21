def diamond():
    l = int(raw_input("Enter the Number of rows(odd)"))
    rows = ['*']
    for i in range(1, l, 2):
        rows.append('*' + ' ' * i + '*')
    rows += rows[:-1][::-1]
    align = lambda x: ('{:^%s}' % l).format(x)
    diamond = '\n'.join(map(align, rows))
    print(diamond)
