def g(df,a):
    extras=[]
    h=[]
    for i in df[a]:
        if type(i)!=int:
            for j in str(i).replace('[','').replace(']','').replace(' ','').replace("'",'').split(','):
                if j not in extras:
                    extras.append(j)
                h.append(j)
    return extras, h