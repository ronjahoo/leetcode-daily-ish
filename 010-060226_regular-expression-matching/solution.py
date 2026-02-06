
def _normalize_pattern(p: str) -> str:
    # collapse redundant repeats like: a*a*a* -> a*, .*.* -> .*
    out = []
    i = 0
    while i < len(p):
        if i + 1 < len(p) and p[i + 1] == "*":
            token = p[i]  # the repeated token
            # if last token in out is same "token*", skip this one
            if len(out) >= 2 and out[-2] == token and out[-1] == "*":
                i += 2
                continue
            out.append(token)
            out.append("*")
            i += 2
        else:
            out.append(p[i])
            i += 1
    return "".join(out)


def regExMatchFirst(s: str, p: str) -> bool:
    p = _normalize_pattern(p)

    m, n = len(s), len(p)

    # quick lower-bound pruning:
    # count required chars in pattern (tokens not followed by '*')
    req = 0
    j = 0
    while j < n:
        if j + 1 < n and p[j + 1] == "*":
            j += 2
        else:
            req += 1
            j += 1
    if req > m:
        return False

    # iterative backtracking stack of states (si, pi)
    stack = [(0, 0)]
    seen = set()  # states we've already proven lead to failure

    while stack:
        si, pi = stack.pop()

        if (si, pi) in seen:
            continue

        while True:
            if pi == n:
                if si == m:
                    return True
                break

            # invalid pattern position
            if p[pi] == "*":
                break

            next_is_star = (pi + 1 < n and p[pi + 1] == "*")
            first_match = (si < m) and (p[pi] == s[si] or p[pi] == ".")

            if next_is_star:
                # skip token * (use 0 occurrences)
                stack.append((si, pi + 2))

                # consume one char if possible, stay on same token (repeat)
                if first_match:
                    si += 1
                    continue
                else:
                    pi += 2
                    continue
            else:
                if not first_match:
                    break
                si += 1
                pi += 1

        # mark this starting state as failed so we don't redo it
        seen.add((si, pi))

    return False

def regExMatchSecond(s:str, p:str) -> bool:
    m, n = len(s), len(p)

    # does the remaining parts match? (dp[i][j] = s[i:] matches p[j:])
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # if both are empty
    dp[m][n] = True

    # fill table backwards
    i = m
    while i >= 0:
        j = n - 1
        while j >= 0:

            # if i is still in the string and characters are equal or pattern has "."
            first_match = (
                i < m and (p[j] == s[i] or p[j] == ".")
            )

            # if there is "*" pattern
            if j + 1 < n and p[j + 1] == "*":
                # zero copies of the previous character or one or more copies of the previous character
                dp[i][j] = (
                    dp[i][j + 2] or
                    (first_match and dp[i + 1][j])
                )
            # normal single character match
            else:
                dp[i][j] = (
                    first_match and dp[i + 1][j + 1]
                )

            j -= 1
        i -= 1

    return dp[0][0]

if __name__ == "__main__":
    s11 = "aa"
    s12 = "a"

    s21 = "aa"
    s22 = "a*"

    s31 = "ab"
    s32 = ".*"

    s41 = "ac"
    s42 = "a."

    print(regExMatchFirst(s11, s12))
    print(regExMatchFirst(s21, s22))
    print(regExMatchFirst(s31, s32))
    print(regExMatchFirst(s41, s42))
    print("---")
    print(regExMatchSecond(s11, s12))
    print(regExMatchSecond(s21, s22))
    print(regExMatchSecond(s31, s32))
    print(regExMatchSecond(s41, s42))
