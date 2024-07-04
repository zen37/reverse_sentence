# Reverse Sentence

## Example:
 Input: "TODAY IS MONDAY"
 Output: "MONDAY IS TODAY"


## Whiteboard

input = "TODAY IS MONDAY"
K = 0

Input_words = [] * len(input) => output = [                        ]
output = [] * len(input) => output = [                        ]
word =  [] * len(input) => word = [                        ]
word  = [ T O D A Y   IS                 ]

n, k = 0
for i in range(len(input):
	char = input(i) 
	if char is not space
		word[k] = char
		k += 1
	else:	
        input_words[n] = word
		word =  [] * len(input)
		n += 1
		k = 0
		
word[6] = I
 input_words[1] =   IS

input_words = [today, is, monday, [], [], ……,[]]


j = 0
for k in range(len(input_words), -1)
	output_words[j] = input_words[k]
	j += 1

output_words[0] = []
output_words[1] = []
…
output_words = [[          ], [          ], … monday, is, today]


n = 0
for k in range(len(output_words)) 
	m = len(output_words[k])
	for  j in range(m)
		if output_words[k][j] is not nothing
			output[n] = output_words[k][j] 
        	n += 1
	if n != len(output) and output_words[k] not nothing 
		output[n] = space


return output

Output = monday space is space today
