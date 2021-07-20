from simplify import *


def read():
    # open
    pos_file = open('./data/rt-polarity.POS', 'r')
    neg_file = open('./data/rt-polarity.NEG', 'r')

    # extract data from file
    pos = pos_file.readlines()
    neg = neg_file.readlines()
    neg_file.close()
    pos_file.close()
    for i in range(len(pos)):
        pos[i] = simplify(pos[i])
    for i in range(len(neg)):
        neg[i] = simplify(neg[i])

    return pos, neg


def extract_densitey(pos, neg):
    # POS density
    pos_density = {}
    for i in range(len(pos)):
        for j in range(len(pos[i])):
            if(pos_density.get(pos[i][j]) != None):
                pos_density[pos[i][j]][0] = pos_density[pos[i][j]][0] + 1
                if(j + 1 < len(pos[i])):
                    if(pos_density[pos[i][j]][1].get(pos[i][j+1]) != None):
                        pos_density[pos[i][j]][1][pos[i][j+1]] += 1
                    else:
                        pos_density[pos[i][j]][1][pos[i][j+1]] = 1
                else:
                    if(pos_density[pos[i][j]][1].get("\n") != None):
                        pos_density[pos[i][j]][1]["\n"] += 1
                    else:
                        pos_density[pos[i][j]][1]["\n"] = 1
            else:
                if(j + 1 < len(pos[i])):
                    pos_density[pos[i][j]] = [1, {pos[i][j+1]:1}]
                else:
                    pos_density[pos[i][j]] = [1, {"\n": 1}]

    # NEG density
    neg_density = {}
    for i in range(len(neg)):
        for j in range(len(neg[i])):
            if(neg_density.get(neg[i][j]) != None):
                neg_density[neg[i][j]][0] += 1
                if(j + 1 < len(neg[i])):
                    if(neg_density[neg[i][j]][1].get(neg[i][j+1]) != None):
                        neg_density[neg[i][j]][1][neg[i][j+1]] += 1
                    else:
                        neg_density[neg[i][j]][1][neg[i][j+1]] = 1
                else:
                    if(neg_density[neg[i][j]][1].get("\n") != None):
                        neg_density[neg[i][j]][1]["\n"] += 1
                    else:
                        neg_density[neg[i][j]][1]["\n"] = 1
            else:
                if(j + 1 < len(neg[i])):
                    neg_density[neg[i][j]] = [1, {neg[i][j+1]:1}]
                else:
                    neg_density[neg[i][j]] = [1, {"\n": 1}]
    return pos_density, neg_density


def uni_density(density):
    U = {}
    m = 0
    for s in density.keys():
        U[s] = density[s][0]
        m += U[s]
    return U, m


def bi_density(density):
    B = {}
    for s in density.keys():
        for n in density[s][1]:
            B[(s, n)] = density[s][1][n]
    return B


def bi_Prob(x, y, uni, bi):
    if(bi.get((x, y)) != None):
        return bi.get((x, y)) / uni.get(x)
    return 0


def uni_P(x, uni, m):
    if(uni.get(x) != None):
        return uni.get(x)/m
    return 0


def bi_p(x, y, uni, bi, m, lambda1, lambda2, lambda3, epsilon):
    return bi_Prob(x, y, uni, bi) * lambda3 + uni_P(y, uni, m) * lambda2 + lambda1 * epsilon


def P(W, bi, uni, m, lambda1, lambda2, lambda3, epsilon):
    p = uni_P(W[0], uni, m)
    for i in range(1, len(W)):
        p = p * bi_p(W[i-1], W[i], uni, bi, m, lambda1,
                     lambda2, lambda3, epsilon)
    return p


def P_U(W, uni, m, lambda1, lambda2, epsilon):
    p = 1
    for i in range(0, len(W)):
        p = p * (uni_P(W[0], uni, m) * lambda2 + lambda1 * epsilon)
    return p


def filterWB(W, bi_pos, uni_pos, m_pos, bi_neg, uni_neg, m_neg, lambda1, lambda2, lambda3, epsilon):
    if(P(W, bi_pos, uni_pos, m_pos, lambda1, lambda2, lambda3, epsilon) >= P(W, bi_neg, uni_neg, m_neg, lambda1, lambda2, lambda3, epsilon)):
        return "not filter this"
    return "filter this"


def filterWU(W, uni_pos, m_pos, uni_neg, m_neg, lambda1, lambda2, epsilon):
    if(P_U(W, uni_pos, m_pos, lambda1, lambda2, epsilon) >= P_U(W, uni_neg, m_neg, lambda1, lambda2, epsilon)):
        return "not filter this"
    return "filter this"


def testB(flag):
    pos, neg = read()
    pos_test = pos[int(len(pos) * 0.9):]
    neg_test = neg[int(len(neg) * 0.9):]
    pos = pos[:int(len(pos) * 0.9)]
    neg = neg[:int(len(neg) * 0.9)]
    pos_density, neg_density = extract_densitey(pos, neg)
    uni_pos, m_pos = uni_density(pos_density)
    bi_pos = bi_density(pos_density)
    uni_neg, m_neg = uni_density(neg_density)
    bi_neg = bi_density(neg_density)
    test = pos_test
    comment = "filter this"
    if(flag == False):
        test = neg_test
        comment = "not filter this"
    j = 0
    for i in range(len(test)):
        if(filterWB(test[i], bi_pos, uni_pos, m_pos, bi_neg, uni_neg, m_neg, 0.88, 0.10, 0.02, 0.001) == comment):
            j += 1
    print(len(test), j)
    print(round(1 - j/len(test), 4))


def testU(flag):
    pos, neg = read()
    pos_test = pos[int(len(pos) * 0.9):]
    neg_test = neg[int(len(neg) * 0.9):]
    pos = pos[:int(len(pos) * 0.9)]
    neg = neg[:int(len(neg) * 0.9)]
    pos_density, neg_density = extract_densitey(pos, neg)
    uni_pos, m_pos = uni_density(pos_density)
    bi_pos = bi_density(pos_density)
    uni_neg, m_neg = uni_density(neg_density)
    bi_neg = bi_density(neg_density)
    test = pos_test
    comment = "filter this"
    if(flag == False):
        test = neg_test
        comment = "not filter this"
    j = 0
    for i in range(len(test)):
        if(filterWU(test[i], uni_pos, m_pos, uni_neg, m_neg, 0.00001, 0.0001, 0.5) == comment):

            j += 1
    print(len(test), j)
    print(round(1 - j/len(test), 4))


# testU(True)
testB(True)
testB(False)
