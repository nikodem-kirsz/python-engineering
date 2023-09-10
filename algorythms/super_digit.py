def superDigit(n, k):  # 9875
    def recursive(num_str):   # 87
        if len(num_str) == 1:
            return num_str
        
        digit_sum = sum(int(digit) for digit in num_str) # 15 -> 6
        
        super_digit = recursive(str(digit_sum))

        return str(super_digit) * k


    return recursive(n)


print(superDigit('9875', 4))