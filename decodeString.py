# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
def decodeString(base_string):
        stack = []
        decoded = ''
        full_num = 0
        print(base_string)

        for char in base_string:
            if char == '[':
                stack.append(decoded)
                stack.append(full_num)
                decoded, full_num = '', 0
                print(stack,"\t",decoded)
            elif char == ']':
                curr_digit, curr_char = stack.pop(), stack.pop()
                decoded = curr_char + curr_digit * decoded
                print(stack,"\t",decoded)
            elif char.isdigit():
                full_num *= 10
                full_num += int(char)
                print(stack,"\t",decoded)
            else:
                decoded += char
                print(stack,"\t",decoded)

        return decoded

print(decodeString("abc3[cd]xyz"))