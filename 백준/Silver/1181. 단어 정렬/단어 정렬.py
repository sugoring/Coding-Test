import sys

number = int(sys.stdin.readline())
wordsset = set()

for i in range(number):
    word = sys.stdin.readline().strip()
    wordsset.add(word)

wordslist = list(wordsset)
wordslist.sort()  # 사전 순 정렬
wordslist.sort(key=len)  # 길이 순 정렬

for result in wordslist:
    print(result)
