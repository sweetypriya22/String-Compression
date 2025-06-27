#String Compression
'''
Write a program to perform basic string compression using the counts of repeated characters. For each group of consecutive repeating characters in the input string, replace it with the character followed by the number of repetitions. If the compressed string is not shorter than the original string, return the original string.
Input Format:
A single string 's' consisting of only lowercase English letters.
'''

def compress_string(s):
    if not s:
        return s  # Edge case: empty string

    compressed = []
    count = 1

    # Traverse the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1  # reset count for new character

    # Append the last group
    compressed.append(s[-1] + str(count))

    compressed_str = ''.join(compressed)

    return compressed_str if len(compressed_str) < len(s) else s
