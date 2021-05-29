import sys
import glob
import os
import numpy as np
import re
from numpy import mean
from numpy import var
from math import sqrt
import scipy.stats as st
from tabulate import tabulate

logs=glob.glob(sys.argv[1] + "/mut_*")
original_scores=[]
optimized_scores=[]
score_dicts=dict()
score_dicts_opt=dict()
result_table = []
for m in logs:
    name=os.path.basename(m).split("_")[1]
    score_list=score_dicts.get(name, [])
    killed_p="NA"
    killed_p_opt="NA"
    #print(m)
    #print(m.split("_")[-1], end="&")
    try:
        f=glob.glob(m+"/**/html-original/index.html", recursive=True)[0]
        original=open(f).read()
        killed_original = re.findall("Killed ([0-9]+) out of ([0-9]+)", original)
        #print(killed_original)
        killed_p = 100*float(killed_original[0][0])/float(killed_original[0][1])
        #print("{0:.2f}\\%".format(killed_p), end="&")
        original_scores = original_scores + [killed_p]
        #score_list.append(killed_p)
    except:
        import traceback as tb
        tb.print_exc()
        print(name)
        #print("NA")
        #exit(1)
        #print("NA", end="&")
        pass

    try:
        f=glob.glob(m+"/**/html-optimized/index.html", recursive=True)[0]
        optimized=open(f).read()
        killed_optimized = re.findall("Killed ([0-9]+) out of ([0-9]+)", optimized)
        killed_p_opt = 100*float(killed_optimized[0][0])/float(killed_optimized[0][1])
        #print("{0:.2f}\\%".format(killed_p_opt), end="\\\\")
        optimized_scores = optimized_scores + [killed_p_opt]

    except:
        print("NA")
        print(name)
        #print("NA", end="\\\\")
        pass
    score_list.append((killed_p, killed_p_opt))
    score_dicts[name]=score_list
    #print("{0:.2f}\\%&{0:.2f}\\%".format(killed_p, killed_p_opt), end="\\\\")
    #print()
for k in sorted(score_dicts.keys()):
    #print(k, len(score_dicts[k]))
    ttest=st.ttest_ind([t[0] for t in score_dicts[k]], [t[1] for t in score_dicts[k]], equal_var=False)
    result_table.append([k,
                         "{0:.2f}%(+/- {1:.2f})".format(np.mean([t[0] for t in score_dicts[k]]),np.std([t[0] for t in score_dicts[k]])),
                         "{0:.2f}%(+/- {1:.2f})".format(np.mean([t[1] for t in score_dicts[k]]),np.std([t[1] for t in score_dicts[k]]))])

    # print("{0}&\\multicolumn{{2}}{{c}}{{ {1:.2f}\\% ($\\pm${2:.2f})}}&\\multicolumn{{2}}{{c}}{{ {3:.2f}\\% ($\\pm${4:.2f}) }}&{5:.2g}\\\\".format(k,
    #                                                                                                                                       np.mean([t[0] for t in score_dicts[k]]),
    #                                                                                                                                       np.std([t[0] for t in score_dicts[k]]),
    #                                                                                                                                       np.mean([t[1] for t in score_dicts[k]]),
    #                                                                                                                                       np.std([t[1] for t in score_dicts[k]]),
    #                                                                                                                                       ttest[1]))
    #))

result_table.append(["Average", "{0:.2f}%".format(sum(original_scores)/len(original_scores)), "{0:.2f}%".format(sum(optimized_scores)/len(optimized_scores))])
print(tabulate(result_table, headers=["Project", "Original", "Optimized"]))
# print("\\hline Average &{0:.2f}\%&&{1:.2f}\%&\\\\\\hline".format(sum(original_scores)/len(original_scores), sum(optimized_scores)/len(optimized_scores)))
