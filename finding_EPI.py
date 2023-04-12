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

def check_pi(variable, binary):
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

def compare_pi_minterm(variable, pi, minterm, count):
    l1 = list(pi)
    l2 = list(minterm)
    count_n = 0
    for i in range(variable):
        if l1[i] != l2[i]:
            count_n += 1
    if count_n == count:
        return True
    else:
        return False

def pi_chart(variable, pi, binary):
    chart = [[0 for x in range(len(binary))] for x in range(len(pi))]
    for i in range(len(pi)):
        count = pi[i].count("-")
        for j in range(len(binary)):
            if compare_pi_minterm(variable, pi[i], binary[j], count):
                chart[i][j] = 1
    return chart

def check_epi(chart, pi):
    epi = []
    temp = []
    id = -1
    for i in range(len(chart[0])):
        count = 0
        for j in range(len(chart)):
            if chart[j][i] == 1:
                count += 1
                id = j
        if count == 1:
            temp.append(pi[id])
    epi = list(set(temp))
    return epi

def solution(minterm):
    answer = []
    
    variable = minterm[0]
    del minterm[0]
    del minterm[0]
    minterm = int_to_binary(variable, minterm)

    # pi
    pi = check_pi(variable, minterm)
    pi = minterm_sort(pi)

    # epi
    chart = pi_chart(variable, pi, minterm)
    epi = check_epi(chart, pi)
    epi = minterm_sort(epi)

    for i in range(len(pi)):
        answer.append(pi[i])
    answer.append("EPI")
    for i in range(len(epi)):
        answer.append(epi[i])

    return answer

def main():
    output = []
    input_list = [int(i) for i in input().strip().split()]
    output = solution(input_list)
    print(output)

if __name__ == "__main__":
    main()
