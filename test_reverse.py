from reverse import Solution
test_cases = [
    ("TODAY IS MONDAY", "MONDAY IS TODAY")
]

def test_reverse_sentence():
    s = Solution()
    for (sentence, expected) in test_cases:
        result = s.reverse_sentence(sentence)
        print(result)
        assert result == expected, f"FAIL, reversed sentence: {result} vs {expected} "