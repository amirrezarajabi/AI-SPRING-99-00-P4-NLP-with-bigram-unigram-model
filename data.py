
# Data
pos_file = open('./data/rt-polarity.POS', 'r')
neg_file = open('./data/rt-polarity.NEG', 'r')


# extract data from file
pos = pos_file.readlines()
neg = neg_file.readlines()
neg_file.close()
pos_file.close()
for i in range(len(pos)):
    pos[i] = pos[i].replace("\n", "")
    pos[i] = pos[i].replace("\"", "")
    pos[i] = pos[i].replace(".", "")
    pos[i] = pos[i].replace("'", "")
    pos[i] = pos[i].replace(",", "")
    pos[i] = pos[i].replace("-", "")
    pos[i] = pos[i].replace("?", "")
    pos[i] = pos[i].replace("!", "")
    pos[i] = pos[i].replace("the", "")
    pos[i] = pos[i].split(" ")
    pos[i] = [s for s in pos[i] if(s!= "")]
for i in range(len(neg)):
    neg[i] = neg[i].replace("\n", "")
    neg[i] = neg[i].replace("\"", "")
    neg[i] = neg[i].replace(".", "")
    neg[i] = neg[i].replace("'", "")
    neg[i] = neg[i].replace(",", "")
    neg[i] = neg[i].replace("-", "")
    neg[i] = neg[i].replace("?", "")
    neg[i] = neg[i].replace("!", "")
    neg[i] = neg[i].replace("the", "")
    neg[i] = neg[i].split(" ")
    neg[i] = [s for s in neg[i] if(s!= "")]
    


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
            if(j + 1< len(pos[i])):
                pos_density[pos[i][j]] = [1,{pos[i][j+1]:1}]
            else:
                pos_density[pos[i][j]] = [1,{"\n":1}]


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
            if(j + 1< len(neg[i])):
                neg_density[neg[i][j]] = [1,{neg[i][j+1]:1}]
            else:
                neg_density[neg[i][j]] = [1,{"\n":1}]

print(pos_density)
