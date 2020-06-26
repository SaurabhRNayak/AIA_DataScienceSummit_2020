"""
By : Saurabh R Nayak [694547]
Created date : 26-06-2020

"""

import random

# Function to calculate attacks by queens positions
def fit_test(batch):
    hit = 0
    matrx=[['-' for i in range(n)] for j in range(n)]
    # print(matrx)
    # print(batch)
    for i in range(n):
        matrx[batch[i]][i]='Q'
    # print(matrx)
    for i in range(n):
        cnt=matrx[batch[i]].count('Q')
        if cnt>0:
            hit=hit+cnt-1
    for i in range(n):
        col=i
        row=batch[i]
        inc=1
        for l in range(0,i):
            c=col-inc
            ru=row-inc
            rd=row+inc
            if(c>=0 and ru>=0):
                if matrx[ru][c]=='Q':
                    hit+=1
            if (c >= 0 and rd <= n-1):
                if matrx[rd][c] == 'Q':
                    hit+=1
            inc+=1
        inc = 1
        for r in range(i, n):
            c = col + inc
            ru = row - inc
            rd = row + inc
            if (c <= n-1 and ru >= 0):
                if matrx[ru][c] == 'Q':
                    hit += 1
            if (c <= n-1 and rd <= n - 1):
                if matrx[rd][c] == 'Q':
                    hit += 1
            inc += 1
    return(hit)

# Function to perform mutation operation
def mutation(crossed_set):
    sel_list = [j for j in range(n) if(crossed_set[j] != target[j])]
    # print("sel",sel_list)
    if len(sel_list)==0 or len(sel_list)<n%2:
        sel_list=list(range(n))
    ind1=random.choice(sel_list)
    ind2=random.choice(sel_list)
    crossed_set[ind1],crossed_set[ind2]=crossed_set[ind2],crossed_set[ind1]
    # print("mut",crossed_set)
    return crossed_set

# Funcion to perform crossover among the best sets to reproduce new set
def crossover_best(best_set):
    for i in range(100):
        a=best_set[random.randint(0,len(best_set)-1)]
        b=best_set[random.randint(0,len(best_set)-1)]
        ind=random.randint(0,n-1)
        crossed_set=a[0:ind]
        crossed_set.extend(b[ind:n])
        # print("cs",crossed_set)
        # if i%2==0:
        crossed_set=mutation(crossed_set)
        if crossed_set in valid_nontarget:
            continue
        batches[i]=crossed_set

if __name__ == "__main__":
    global n
    n=8
    n_list = [i for i in range(n)]
    global batches
    batches = []
    # target = [3, 6, 2, 7, 1, 4, 0, 5]
    target=[3, 1, 6, 4, 0, 7, 5, 2]
    # create initial random positioning
    for _ in range(100):
        tm= n_list[:]
        # print(n_list)
        random.shuffle(tm)
        batches.append(tm)
        # print(batches)
    iterations = 1
    done=0
    hits=None
    global valid_nontarget
    valid_nontarget=[]
    dict_={}
    while(True):
        # print("::: iteration {} :::".format(iterations))
        for i in batches:
            hits=fit_test(i)
            if(hits==0):
                # print("::: iteration {} :::".format(iterations))
                if(i==target):
                    # print("Queen row positions for 0-N columns :\n",i)
                    ans = ' '.join([str(x) for x in i])
                    print(ans)
                    done=1
                    break
                else:
                    if i not in valid_nontarget:
                        valid_nontarget.append(i)
                    # print(valid_nontarget)
            else:
                if hits in dict_.keys():
                    dict_[hits].append(i)
                else:
                    dict_[hits]=[i]
        if done==1:
            break
        #fitness function call
        best_set=dict_[min(dict_.keys())]
        #crossover and mutaion function call
        crossover_best(best_set)
        iterations += 1