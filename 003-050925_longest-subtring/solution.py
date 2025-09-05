from typing import Dict


def length_of_longest_substring_hash(s: str) -> int:
    longest_length = 0
    current_length = 0
    seen = {}

    for _, ch in enumerate(s):
        if ch in seen:
            if current_length > longest_length:
                longest_length = current_length
            current_length = 1
            seen = {ch: True}
        else:
            current_length += 1
            seen[ch] = True

    if current_length > longest_length:
        longest_length = current_length

    return longest_length


def length_of_longest_substring_dict(s: str) -> int:
    last_seen: Dict[str, int] = {}
    left = 0
    max_len = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = i
        max_len = max(max_len, i - left + 1)

    return max_len


if __name__ == "__main__":
    text = "abcabcbb"

    result_hash = length_of_longest_substring_hash(text)
    result_dict = length_of_longest_substring_dict(text)

    print("Naive hash result:", result_hash)
    print("Optimized dict result:", result_dict)
