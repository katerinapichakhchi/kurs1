def second_index(text: str, some_str: str) -> int:
        if text.count(some_str) < 2:
            return None
        return text.find(some_str, text.find(some_str,0)+1)


assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo") == 10
print('ОК')