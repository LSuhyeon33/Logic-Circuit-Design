def compare_minterm(variable, minterm1, minterm2):
    l1 = list(minterm1)
    l2 = list(minterm2)
    count = 0
    for i in range(variable):
        if l1[i] != l2[i]:
            count += 1
            l1[i] = "-"
    if count > 1:
        return -1
    else:
        return "".join(l1)

def minterm_2_change(minterm):
    minterm_1 = []
    for m in minterm:
        m = list(m)
        for i in range(len(m)):
            if m[i] == '-':
                m[i] = '2'
        m = "".join(m)
        minterm_1.append(m)
    return minterm_1

def minterm_return_change(minterm):
    minterm_1 = []
    for m in minterm:
        m = list(m)
        for i in range(len(m)):
            if m[i] == '2':
                m[i] = '-'
        m = "".join(m)
        minterm_1.append(m)
    return minterm_1

def minterm_sort(minterm):
    minterm = minterm_2_change(minterm)
    minterm.sort(reverse=False)
    minterm = minterm_return_change(minterm)
    return minterm

def check(variable, binary):
    pi = []
    while 1:
        check1 = ["*"] * len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i + 1, len(binary)):
                k = compare_minterm(variable, binary[i], binary[j])    # 1의 개수 check
                if k != -1:
                    check1[i] = "^"
                    check1[j] = "^"
                    temp.append(k)
        for i in range(len(binary)):
            if check1[i] == "*":
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = list(set(temp)) 
 
def int_to_binary(variable, minterms):
    temp = []
    for m in minterms:
        m = format(m, "b").zfill(variable)
        temp.append(m)
    return temp

def solution(minterm):
    answer = []
    
    variable = minterm[0]
    del minterm[0]
    del minterm[0]
    minterm = int_to_binary(variable, minterm)
    minterm = check(variable, minterm)
    answer = minterm_sort(minterm)

    return answer

def main():
    output = []
    input_list = [int(i) for i in input().strip().split()]
    output = solution(input_list)
    print(output)

if __name__ == "__main__":
    main()
