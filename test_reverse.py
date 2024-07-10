from reverse2 import Solution2

test_cases = [
    ("HEUTE IST MONTAG!", "MONTAG! IST HEUTE"),
    ("HEUTE IST MONTAG ODER FREITAG", "FREITAG ODER MONTAG IST HEUTE"),
    ("123   ABC 45", "45 ABC   123"), #3 spaces
    ("A BC DEF G", "G DEF BC A")
]

def test_reverse_sentence2():
    s = Solution2()
    for sentence, expected in test_cases:
        result = s.reverse_sentence(sentence)
        assert result == expected, f"FAIL, reversed sentence: {result} vs {expected} "