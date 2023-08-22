n = int(input())

matrix = [list(map(int, input().split(", "))) for _ in range(n)]


print(f"First diagonal: {', '.join([str(matrix[i][i]) for i in range (n)])}. Sum: {sum([matrix[i][i] for i in range(n)])}")
print(f"Second diagonal: {', '.join([str(matrix[i][i]) for i in range (n)])}. Sum: {sum([matrix[i][i] for i in range(n)])}")
print(sum([matrix[i][i] for i in range(n)]))


