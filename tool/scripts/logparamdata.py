# spec_dict = dict()
# if "optim_" in sys.argv[1]:
#     logs = [sys.argv[1]]
# else:
#     logs=glob.glob(sys.argv[1] + "/optim_*/")
#
# for m in logs:
#     name=m.split("_")[-1].split("/")[0]
#     cur_spec_dict = spec_dict.get(name, [])
#     tests = glob.glob(m+"/run_*/log.txt")
#     for t in tests:
#         s = SpecData.getspecdata(t)
#         if s is not None:
#             cur_spec_dict.append(s)
#
#     spec_dict[name] = cur_spec_dict
#
# test_count=0
#
# for k in sorted(spec_dict.keys()):
#     if len(spec_dict[k]) == 0:
#         continue
#     numparams = [len(x.params) for x in spec_dict[k]]
#     for test in spec_dict[k]:
#         p=test.params
#         defaultp=test.
#     print(k, numparams)
import testspecs
#print(testspecs.testspecs)
from src.lib.ParamType import ParamType

i=0
repo_dict = dict()
for s in testspecs.testspecs:
    if s.skip:
        continue
    if s.repo in ["trax", "rasa"]:
        continue
    r=repo_dict.get(s.repo, [])
    r.append(s)
    repo_dict[s.repo] = r
    i+=1
print(i)
t= {ParamType.ITER : "discrete interval", ParamType.CHAINS : "discrete choices", ParamType.LR : "continuous interval"}
params = dict()
names = []
for k in sorted(repo_dict.keys()):
    # if k not in [ "trax", "rasa" ]:
    print(">>", k, len(repo_dict[k]))
    for s in repo_dict[k]:
        psize = len(s.params)
        cursize = params.get(psize, 0)
        params[psize] = cursize+1

        for p in s.params:
            names.append(p.name)
            print("%s,%s,%s" % (p.name,p.value_range, t[p.param_type]))
print("one param", params)
for k in set(names):
    print(k, len([s for s in names if s==k]))

