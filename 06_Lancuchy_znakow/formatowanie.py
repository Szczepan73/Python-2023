s = 'Ala ma {0} kotów'.format(5)
s

'Ala ma ' + str(5) + ' kotów'

s = 'Ala ma {0} kot{1}'.format(5, 'ów')
s

s = 'Ala ma {0} kot{1}'.format(4, 'y')
s

f'Pi to jest mniej więcej {3.1415926:.3}'

for i in range(12):
    print(f'{i:2}')

for i in range(12):
    print(f'{i:02}')

from math import pi
pi

f'{pi:.3}'
f'{pi:.3f}'
f'{pi-3:.3f}'
f'{12:3d}'
f'{12:03d}'
f'{pi:<30.2f}'
f'{pi:>30.2f}'
f'{pi:->30.2f}'
f'{pi:^30.2f}'
f'{"-"*10}HELLO{"-"*10}'
f'{"HELLO":-^25s}'




a = "*"
#f'{a: ^10s}'
i = int(input("Podaj wysokosc choinki"))
for n in range (i):
    print (f'{" "* (i-n)} {a*(2*n+1)} {" "*(i-n)}')
 #   z = z - 1
for ogonek in range (2):
    print(f'{" " * (i-ogonek)} {a * (2 * ogonek + 1)} {" " * (i-ogonek)}')






