def check(sost, k, pam):
    if sost in pam:
        return pam[sost]

    for kuch in set(sost):
        niz = max(1, (kuch + k) // (k + 1))
        verh = (kuch - 1) // 2
        for b in range(niz, verh + 1):
            a = kuch - b
            if a <= k * b:
                sled = list(sost)
                sled.remove(kuch)
                sled.append(b)
                sled.append(a)
                sled_sost = tuple(sorted(sled))
                if not check(sled_sost, k, pam):
                    pam[sost] = True
                    return True

    pam[sost] = False
    return False


def main():
    t = int(input())  # тесты

    for _ in range(t):
        n, k = map(int, input().split())  # сколько куч и коэффицент
        piles = list(map(int, input().split()))  # кучи

        pam = {}
        sost = tuple(sorted(piles))

        schet = 0
        for kuch in set(sost):
            niz = max(1, (kuch + k) // (k + 1))
            verh = (kuch - 1) // 2
            for b in range(niz, verh + 1):
                a = kuch - b
                if a <= k * b:
                    sled = list(sost)
                    sled.remove(kuch)
                    sled.append(b)
                    sled.append(a)
                    sled_sost = tuple(sorted(sled))

                    if not check(sled_sost, k, pam):
                        schet += 1

        if schet > 0:
            print(f"Win {schet}")
        else:
            print("Lose 0")


if __name__ == "__main__":
    main()
