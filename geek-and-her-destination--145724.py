# Geek's Destination with Special Jump
# Platform: GFG
# Difficulty: Hard
# Topics: Prefix Sum, Number Theory, Greedy, Mathematics, Modular Arithmetic, Arrays

def solve():
    tokens = []
    while len(tokens) < 5:
        tokens.extend(input().split())
    a, b, d, l, r = map(int, tokens[:5])

    if d <= 0 or l > r:
        print(0)
        return

    ans = 0
    if l == 0:
        if d <= a:
            ans += d
        else:
            c = a - b
            k = (d - a + c - 1) // c
            ans += 2 * k * b + d
        l = 1

    if l <= r:
        j_ge_d_start = max(l, d)
        if j_ge_d_start <= r:
            ans += r - j_ge_d_start + 1

        j_lt_d_end = min(r, d - 1)
        if l <= j_lt_d_end:
            x_l = d - j_lt_d_end
            x_r = d - l

            u = max(x_l, 1)
            v = min(x_r, a)
            if u <= v:
                ans += (v - u + 1) * (u + v + 2) // 2

            U = max(x_l, a + 1)
            V = x_r
            if U <= V:
                ans += (V - U + 1) * (U + V + 2) // 2
                c = a - b

                def prefix_ceil_sum(n):
                    if n <= 0:
                        return 0
                    q, rem = divmod(n, c)
                    return c * (q * (q + 1) // 2) + rem * (q + 1)

                ans += 2 * b * (prefix_ceil_sum(V - a) - prefix_ceil_sum(U - a - 1))

    print(ans % MOD)

solve()