def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if(string[i] == sub_string[0]):
            incr = 0
            match = True
            for j in range(0, len(sub_string)):
                if ((string[i + incr]) != sub_string[j]):
                    match = False
                    break
                else:
                    incr += 1
            if match:
                count += 1
    return count

print(count_substring('ABCDCDC', 'CDC'))