#A
def solve():
    n, k = map(int, input().split())
    if k == 1 and n>=3:
        print(0)
        return
    unique_necklaces = set()
    def generate(pos, current):
        if pos == n:
            if current[0] != current[-1]:
                normal = normalize(current)
                unique_necklaces.add(normal)
            return

        for color in range(k):
            if pos > 0 and current[pos-1] == color:
                continue
            if pos == n-1 and current[0] == color:
                continue
            current.append(color)
            generate(pos+1, current)
            current.pop()
    def normalize(beads):
        rotations = []
        for i in range(n):
            rotation = beads[i:] + beads[:i]
            rotations.append(tuple(rotation))
        reflected = beads[::-1]
        for i in range(n):
            rotation = reflected[i:] + reflected[:i]
            rotations.append(tuple(rotation))

        return min(rotations)

    generate(0, [])
    print(len(unique_necklaces))
solve()
