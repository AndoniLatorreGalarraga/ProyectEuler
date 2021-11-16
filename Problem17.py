def n2Text(n):
    dict1 = {'1':'One', '2':'Two','3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
    dict2 = {'2':'Twenty','3':'Thirty', '4':'Forty', '5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}
    dict3 = {'0':'Ten', '1':'Eleven', '2':'Twelve','3':'Thirteen', '4':'Fourteen', '5':'Fifteen', '6':'Sixteen', '7':'Seventeen', '8':'Eighteen', '9':'Nineteen'}
    dict4 = {'1':'One', '2':'Two','3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
    s = str(n)
    if n == 1000:
        return 'OneThousand'
    elif len(s) == 3:
        if n%100 == 0:
            return dict4[s[0]]+'Hundred'
        return dict4[s[0]]+'HundredAnd'+n2Text(int(s[1:]))
    elif len(s) == 2:
        if n%10 == 0 and n >= 20:
            return dict2[s[0]]
        elif n >= 20:
            return dict2[s[0]] + n2Text(int(s[1]))
        return dict3[s[1]]
    return dict1[s]

sum = 0
for n in range(1, 1+ 1000):
    sum += len(n2Text(n))
print(sum)