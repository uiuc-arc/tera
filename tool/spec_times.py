from testspecs import testspecs
import glob
from tabulate import tabulate


def find_time(start, end, testspecs):
    repo_name = testspecs[start].repo
    try:
        file_name = glob.glob("test_times/" + repo_name + "*")[0]
    except:
        return -1
    t = open(file_name, "r", encoding='utf-8')
    total_time = 0.0

    t.close()
    with open(file_name, "r", encoding='utf-8') as f:
        text = f.read()
        try:
            ind = text.index("slowest")
            text = text[ind:]
        except:
            pass

        lines = text.split('\n')
        times = []
        for l in lines:
            if repo_name == 'cleverhans' and (l.startswith('[success]') or l.startswith('test')):
                try:
                    parts = l.split(' ')
                    if parts[len(parts) - 1].strip('()')[:-1] != 'SKI':
                        total_time += float(parts[len(parts) -
                                                  1].strip('()')[:-1])
                except:
                    pass
            else:
                if 'call' in l:
                    parts = l.split(' ')
                    total_time += float(parts[0][:-1])
        for i in range(start, end + 1):
            spec = testspecs[i]
            if spec.classname != "none":
                test_name = spec.classname + "::" + spec.testname
            else:
                test_name = spec.filename.split('/')[-1] + "::" + spec.testname
            for l in lines:
                if spec.repo == 'cleverhans':
                    if spec.classname in l and spec.testname in l:
                        parts = l.split(' ')
                        time = float(parts[len(parts) - 1].strip('()')[:-1])
                        times.append(time)
                        continue

                if test_name in l and test_name + "_" not in l:
                    parts = l.split(' ')
                    try:
                        time = float(parts[0][:-1])
                    except:
                        continue
                    times.append(time)
        f.close()

    return sum(times) / total_time


if __name__ == '__main__':
    start_index = 0
    result_dict = {}
    total_percent = 0.0

    repo_status = ['pyro', 'numpyro', 'pymc3', 'gpytorch', 'sbi', 'pyGPGO', 'pymc-learn', 'bambi',
                   'fairseq', 'autokeras', 'parlai', 'cleverhans', 'gensim', 'ml-agents', 'imbalanced-learn']
    result_table = []
    testspecs = list(
        filter(lambda spec: spec.repo in repo_status and spec.skip is False, testspecs))
    for i in range(len(testspecs) - 1):
        if testspecs[i + 1].repo != testspecs[i].repo or i == len(testspecs) - 2:

            result_dict[testspecs[i].repo] = find_time(
                start_index, i, testspecs)
            if result_dict[testspecs[i].repo] != -1:
                total_percent += result_dict[testspecs[i].repo]
            start_index = i + 1
    count_dict = {}
    total_count = 0

    for t in testspecs:
        if t.repo not in count_dict:
            count_dict[t.repo] = 0
        count_dict[t.repo] += 1
        total_count += 1

    for x in sorted(result_dict.keys()):
        result_table.append([x, count_dict[x], "{:.2f}".format(result_dict[x] * 100)])
    result_table.append(["Total/Avg", total_count, "{:.2f}".format((total_percent * 100) / (len(result_dict.keys())))])
    print(tabulate(result_table, headers=["Project", "#Tests", "%Time"]))
