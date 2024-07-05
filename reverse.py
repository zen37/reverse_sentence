
import sys

def calculate_memory_usage(input_list):
    # Calculate the size of an empty list
    size_of_list_structure = sys.getsizeof([])

    # Calculate the total size of the list structure and the strings it contains
    total_size = size_of_list_structure
    for s in input_list:
        total_size += sys.getsizeof(s)

    return total_size


def calculate_memory_space(list):

    space = 0

    for i in range(len(list)):
        for j in list[i]:
            space += 1
        if list[i] == '':
            space += 1

    return space


def is_memory_now_less(current, start):
    return current <= start


class Solution:
    def reverse_sentence(self, input :str) -> str:

        FILL = ''
        SPACE = ' '

        input_words = [FILL] * len(input)
        print(f"input_words: {input_words}")
        mem_start = calculate_memory_space(input_words) # calculate_memory_usage(input_words)
        print(f"mem start: {mem_start}")

        word =  [FILL] * len(input)
        print(f"word: {word}")

        output_words = [FILL] * len(input)
        print(f"output_words: {output_words}")

        output = [FILL] * len(input) 
        print(f"output: {output}")

        n, k, s, w = 0, 0, 0, 0
        for i in range(len(input)):
            input_word = FILL
            char = input[i]
            if not char.isspace():
                word[k] += char
                current = calculate_memory_space(word)
                if (not is_memory_now_less(current, mem_start )): 
                    print(f"You failed miserably! word memory now: {current} vs memory start: {mem_start}")
                    return
                #else:
                #    print(f"word memory now: {current} vs memory start: {mem_start}")
                k += 1
                s += 1 #deduct spaces
            else:   
                for i in range(len(word)):
                    input_word = input_word + word[i]
                input_words[n] = input_word
                if n == k:
                    input_words.pop() # take one out before putting back
                    input_words[n] = input_word 
                n += 1
                word =  [FILL] * len(input)
                k = 0
                s -= 1 #dcrease speace deduction

        if k > 0:
            for i in range(len(word)):
                if  word[i] != FILL:
                    input_word = input_word + word[i]
            for i in range(s):
               input_words.pop()
            #print("after pop: ", input_words)
            if input_words:
                input_words[n] = input_word
            else:
                input_words.append(input_word)
                            
        
        current = calculate_memory_space(input_words)
        if (not is_memory_now_less(current, mem_start )): 
            print(f"You failed miserably! input_words memory now: {current} vs memory start: {mem_start}")
            return
        else:
            print(f"input_words memory now: {current} vs memory start: {mem_start}")

        print(f"output_words{output_words}")
        j = 0
        for k in range(len(input_words) - 1, -1, -1):
            #print(f"input_words[{k}]: ", input_words[k] )
            if input_words[k] != '':
                for i in range(len(input_words[k])-1):
                    output_words.pop()
                #print(f"output_words after pop{output_words}")
                output_words[j] = input_words[k]
                #print(f"output_words {output_words} after adding {output_words[j]}")
                j += 1
            for i in range(len(output_words[j])-1):
                output_words.pop() 
          
        
        print("output_words: ", output_words)
        print("output: ", output)
        current = calculate_memory_space(output_words)
        if (not is_memory_now_less(current, mem_start )): 
            print(f"You failed! memory now: {current} vs memory start: {mem_start}")
            return
        else:
            print(f"output_words memory now: {current} vs memory start: {mem_start}")

        w, s = 0, 0
        for j in range(len(output_words)):
            if output_words[j] != FILL:
                m = len(output)
                if m > w + 3:
                    for i in range(len(output_words[j])+1):
                        output.pop()
                else:
                    for i in range(len(output_words[j])-1):
                        output.pop()
                s = 0
                w += 1
            
                if len(output) >= w - 1:
                    output[0] = output[0] + output_words[j] + SPACE
                    current = calculate_memory_space(output)
                    if (not is_memory_now_less(current, mem_start )): 
                        print(f"You failed miserably! output memory now: {current} vs memory start: {mem_start}")
                        return
                    #else:
                    #    print(f"output memory now: {current} vs memory start: {mem_start}")
                else:
                     output[0] = output[0] + output_words[j]
            
        print(f"output: {output}")
        current = calculate_memory_space(output)
        
        if (not is_memory_now_less(current, mem_start )): 
            print(f"You failed miserably! output memory now: {current} vs memory start: {mem_start}")
            return
        else:
            print(f"output memory now: {current} vs memory start: {mem_start}")
        

        return output[0]

if __name__ == "__main__":
    input = "THURSDAY 4th of JULY HAS BEEN A MISERABLE DAY"
    print(f"sentence: {input}")
    s = Solution()
    output = s.reverse_sentence(input)
    print(f"reversed sentence: {output}")