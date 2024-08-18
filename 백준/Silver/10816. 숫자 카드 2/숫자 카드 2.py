import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))

# 각 숫자의 빈도를 세어 딕셔너리로 저장
card_count = Counter(cards)

# 각 query에 대해 카드의 개수를 가져와서 리스트에 저장
result = [str(card_count[query]) for query in queries]

# 결과 출력
print(' '.join(result))
