def viralAdvertising(n):
    target = 5
    sum = 0
    for _ in range(n):
        target = math.floor(target/2)
        sum +=target
        target *=3
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
