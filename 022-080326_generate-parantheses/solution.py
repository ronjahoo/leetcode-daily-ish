from collections import deque

def generateParanthesesFirst(n: int) -> list[str]:
    results = []

    def build(current_string, open_count, close_count):
        """
        Recursively build valid parenthesis combinations.
        
        - current_string: the string built so far
        - open_count:     how many '(' we've used
        - close_count:    how many ')' we've used
        """
        if len(current_string) == 2 * n:
            results.append(current_string)
            return

        if open_count < n:
            build(current_string + "(", open_count + 1, close_count)

        if close_count < open_count:
            build(current_string + ")", open_count, close_count + 1)

    build("", 0, 0)
    return results


def generateParanthesesSecond(n: int) -> list[str]:
    results = []
    
    queue = deque([("", 0, 0)])

    while queue:
        current, open_count, close_count = queue.popleft()

        if len(current) == 2 * n:
            results.append(current)
            continue

        if open_count < n:
            queue.append((current + "(", open_count + 1, close_count))

        if close_count < open_count:
            queue.append((current + ")", open_count, close_count + 1))

    return results

if __name__ == "__main__":
    print(generateParanthesesFirst(3))
    print(generateParanthesesFirst(1))
    print(generateParanthesesSecond(3))
    print(generateParanthesesSecond(1))