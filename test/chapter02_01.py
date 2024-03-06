# chapter02_01
# print 사용법

print('python')
print("python")
print()

print('p', 'y', 't', sep='+')
print()

print('welcome', end=' ')
print('itnews', end=' ')
print('web')
print()

import sys
print('learn py', file=sys.stdout)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print('{:^10}'.format('nice'))
print('{:_>10}'.format('nice'))
print('{:_<10}'.format('nice'))
print('{:10}'.format('nice'))