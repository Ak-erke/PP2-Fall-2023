a = int(input())
alln = set(range(1, a + 1))
possiblen = alln
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possiblen & guess) > len(possiblen) / 2:
        print('YES')
        possiblen &= guess
    else:
        print('NO')
        possiblen &= alln - guess

print(' '.join([str(x) for x in sorted(possiblen)]))
