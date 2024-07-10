from typing import List

class Solution2:

    def reverse(self, input: List[str]) -> str:
        output = [' '] * len(input)

        n = len(input)
        j = n
        for i in range(n):
            temp = input[i]
            output[i] = input[j-1]
            output[j-1] = temp
            i += 1
            j -= 1
        return output

    def reverse_sentence(self, input: str) -> str:
        # Reverse the entire input string
        reversed_input = self.reverse(list(input))

        # Reverse each word in the reversed string
        n = len(reversed_input)
        start = 0
        while start < n:
            if reversed_input[start] != ' ':
                end = start
                while end < n and reversed_input[end] != ' ':
                    end += 1
                reversed_input[start:end] = self.reverse(reversed_input[start:end])
                start = end
            else:
                start += 1

        output = ""
        for char in reversed_input:
            output += char
        return output


if __name__ == "__main__":
    s = "MONDAY IS TODAY"
    print(f"sentence: {s}")
    sol = Solution2()
    r = sol.reverse_sentence(s)
    print(f"reversed sentence: {r}")