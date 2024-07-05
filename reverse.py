
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
                #print(f"word[{k}]: {char}")
                word[k] += char  # Append char to current 
                #print(word)
                current = calculate_memory_space(word)
                if (not is_memory_now_less(current, mem_start )): 
                        print(f"You failed miserably! memory now: {current} vs memory start: {mem_start}")
                        return
                #else:
                #    print(f"memory now: {current} vs memory start: {mem_start} for word")
                k += 1
                s += 1 #deduct spaces
            else:   
                #print(f"word[{k}]: {char}")
                for i in range(len(word)):
                    input_word = input_word + word[i]
                #input_words.pop() # take one out before putting back
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
                    #print(input_word)
            #print("before pop: ", input_words)
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
            print(f"memory now: {current} vs memory start: {mem_start} for input_words")

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
            print(f"memory now: {current} vs memory start: {mem_start} for output_words")

        w = 0
        for j in range(len(output_words)):
            if output_words[j] != FILL:
                print(output_words[j])
                for i in range(len(output_words[j])):
                    #print(i)
                    #print("before pop:", output)
                    output.pop()
                    #print("after pop:", output)
                    w += 1

                if len(output) > 2:
                    output[0] = output[0] + output_words[j] + SPACE
                else:
                    output[0] = output[0] + output_words[j] 
                #print("oiutout: ", output)
                #print(len(output))
                if len(output) == w - 1:
                    output.pop()
                #print("createing the output: ", output)
        
        print(f"output: {output}")
        current = calculate_memory_space(input_words)
        if (not is_memory_now_less(current, mem_start )): 
            print(f"You failed miserably! memory now: {current} vs memory start: {mem_start}")
            return
        else:
            print(f"memory now: {current} vs memory start: {mem_start} for output")




        return output[0]

if __name__ == "__main__":
    input = "TODAY IS MONDAY"
    print(f"sentence: {input}")
    s = Solution()
    output = s.reverse_sentence(input)
    print(f"reversed sentence: {output}")