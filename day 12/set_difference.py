english = int(input())
eng_ppl = set(map(int, input().split()))
french = int(input())
french_ppl = set(map(int, input().split()))

print(len(eng_ppl.difference(french_ppl)))