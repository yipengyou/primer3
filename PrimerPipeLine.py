import primer3 as p3

#Read Coding sequence from text file
cds = ''
with open("cds.txt", 'r') as f:
    strin = f.readlines()
    for a in strin:
        a = a.strip()
        cds += a

#Creating the dictionary that results from Primer3's algorithms of 200 possible primers
res = p3.bindings.designPrimers(
    {'SEQUENCE_TEMPLATE': cds},
    {'PRIMER_PRODUCT_SIZE_RANGE': [[300, 400], [250, 500], [500, 1000]],
     'PRIMER_NUM_RETURN': 200,
     'PRIMER_MIN_SIZE': 18,
     'PRIMER_OPT_SIZE': 24,
     'PRIMER_MAX_SIZE': 30,
     'PRIMER_MIN_TM': 50,
     'PRIMER_OPT_TM': 60,
     'PRIMER_MAX_TM': 65,
     'PRIMER_MIN_GC': 40,
     'PRIMER_OPT_GC': 50,
     'PRIMER_MAX_GC': 60,
     'PRIMER_MAX_SELF_ANY': 3,
     'PRIMER_MAX_SELF_END': 3})

#Creating a readable version of the result dictionary that can be sorted based on certain parameters
counter = -7
useful = {}
for a in res.keys():
    if str(counter) not in a:
        counter += 1
        if counter > 0 and counter not in useful.keys():
            useful[counter] = [res[a]]
    elif counter not in useful.keys():
        useful[counter] = [res[a]]
    else:
        useful[counter].append(res[a])

#0=Pair Penalty, 1= Left Penalty, 2= Right penalty, 3= left sequence, 4= right sequence, 5= primer left, 6= primer right, 7=primer left TM, 8=primer right TM, 9=Primer left GC%, 10= primer right gc%, 11= primer left self anyTH, 12= primer right self anyTH, 13= primer left self endTH, 14=PRimerRight self endTH, 15= left hairpinTH, 16= right hairpinTH, 17=leftendStability,18=rightEndStability,19=pairComplAnyTH,20=pairComplyEndTH, 21=pairProductSize
#sortby = some int based on which number was picked or what not
useful = (sorted(useful.items(), key=lambda items: items[1][0]))
print(useful)

