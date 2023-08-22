numbers = list(map(int, input().split(", ")))
positives = []
negatives = []
even = []
odd = []
[positives.append(num) if num>=0 else negatives.append(num) for num in numbers ]
[even.append(el) if el%2==0 else odd.append(el) for el in numbers]


print(f"Positive: {', '.join([str(el) for el in positives])}")
print(f"Negative: {', '.join([str(el) for el in negatives])}")
print(f"Even: {', '.join([str(el) for el in even])}")
print(f"Odd: {', '.join([str(el) for el in odd])}")