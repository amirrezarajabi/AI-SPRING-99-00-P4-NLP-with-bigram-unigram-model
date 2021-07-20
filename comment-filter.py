from data import *

pos, neg = read()
pos_density, neg_density = extract_densitey(pos, neg)
uni_pos, m_pos = uni_density(pos_density)
bi_pos = bi_density(pos_density)
uni_neg, m_neg = uni_density(neg_density)
bi_neg = bi_density(neg_density)
flag = True
t = input("type(U/B): ")
while(flag):
    word = input(">>> ")
    if(word == "!q"):
        flag = False
    else:
        W = ["good"]
        if(t == "B"):
            print(filterWB(W, bi_pos, uni_pos, m_pos, bi_neg, uni_neg, m_neg, 0.00001, 0.0001, 0.001, 0.5))

        else:
            print(filterWU(W, uni_pos, m_pos, uni_neg, m_neg, 0.00001, 0.0001, 0.5))
