from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    nan_height = [int(input()) for _ in range(9)]
    diff = sum(nan_height) - 100
    
    for i in range(8):
        for j in range(i + 1, 9):
            if nan_height[i] + nan_height[j] == diff:
                res = sorted([nan_height[k] for k in range(9) if k != i and k != j])
                
                print(*res, sep='\n')
                exit(0)
