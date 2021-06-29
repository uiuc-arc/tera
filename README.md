
This repository contains the implementation for our  ISSTA'21 paper: TERA: Optimizing Stochastic Regression Tests in Machine Learning Projects. 
We provide details for a docker based installation process for our tool. We provide both the docker file `root/Dockerfile` and a pre-setup image file to reproduce the experiments. We have tested the tool on an Ubuntu 18.04 machine using docker version 18.03.1-ce. However, we do not expect any issues on other systems. The artifact for our paper is also available at https://zenodo.org/record/4771137.


==============================================
# Overview
==============================================

TERA is a tool for reducing the execution time of tests for Machine Learning algorithms by tuning the algorithm hyper-parameters.
 
================================================
# Getting Started Instructions
===============================================

### Directory Structure

The source code for the project is mainly contained in the `tool/` directory. The `tool/` directory is further split into sub-directories like `src` which contains implementation files, folders with setup scripts (`build_scripts` and `scripts`), logs folders and other implementation files. The root directory further contains some top level files like `requirements.txt`.

### Docker Setup 
Install [Docker](https://www.docker.com/get-started)  for your OS, if not already installed

Building image using the provided tarball (See below if you want pre-built image)
 
1. Untar the provided tarball/zipped file `tera_main.zip`. cd into the folder
2. Run `docker build -t tera .` to create docker image
3. Run `docker run -i -t tera /bin/bash`
4. Run `bash setup.sh`

Downloading pre-built image

1. Pull the latest image using `docker pull aryaman4/tera:full`
2. Run `docker run -it aryaman4/tera:full /bin/bash` to create container and login into the image.

### Running some experiments to verify installation

1. Go to scripts folder: `cd tool/scripts`
2. Run `./autokeras_setup.sh ../../projects` to setup one project
3. Go to tool folder: `cd ..`
4. Run optimizer: `python3 optimizer.py -r autokeras -j 2 -file tests/integration_tests/task_api_test.py -test test_structured_data_from_numpy_classifier -cl none`. You can use more threads instead of 2 if you have more cores on your machine. This will produce output in `tool/logs` folder and take 10-15 mins. This experiment corresponds to Table 2 results.
5. Run the mutation script. Go to `tool` folder. Run `./mutation.sh autokeras 2 all`. You can use more threads instead of 2 if you have more cores. This will also produce output in `tool/logs` folder. Once it starts displaying progress as mutants killed/survived, you can kill the process early using `Ctrl-C`. This corresponds to Table 3 results.
6. If the above experiments finish, you can run `python3 logsummarytotable.py ../tool/logs` from the `tool/scripts` folder to print out the optimization results and `python3 mutlogtotable.py ../tool/logs` to print out the mutation experiment results.
 
=========================================
# Detailed Description 
=========================================

In the following sections, we provide instructions on how to run the tool and reproduce smaller scale results. The smaller scale experiments should provide similar speedups/mutation scores as the paper. However, there might be some differences in timings/speedup as it depends on the configuration of the host machine. 

## Running TERA Optimizer (Tables 2/5)

1. Before running any project, we need to setup its environment. Go to `tool/scripts` and run `bash {PROJECT_NAME}_setup.sh ../../projects` to set up the project. We evaluated 15 projects in TERA. 

2. Run `python3 optimizer.py -r {PROJECT_NAME} -j {THREADS}` to run TERA for the project. Check the next section for explanation on other flags used by optimizer.py. Output is produced on screen and saved in `logs` folder with name `optim_`. You can also run any individual test/group of tests by using any combination of filename (`-file` argument), classname (`-cl` argument), and testname (`-test` argument). You can find the specification of all tests we used in `tool/testspecs.py` file. We provide a description of this file later.

3. Run `cd scripts; python3 logsummarytotable.py ../logs` to print out the results (similar to table 2).

4. Run `cd scripts; python3 logtimestotable.py ../logs` to print out the timing results (similar to table 5).

For the small scale experiment, we recommend running autokeras/fairseq/pyGPGO projects here as they run relatively faster (Refer to Table 5 for average execution times).  

### Explanation of optimizer flags

- Repo Name: -r
- File name: -file
- Class name: -class 
- Test name: -test
- Max probability of failure: -p (we use 0.01 as default)
- Number of threads: -j
- Convergence threshold: -t (default is 1.0)

### Test specifications

TERA requires complete specification of a test, its parameters, and the assertion for optimization. All test specifications can be found in `tool/testspecs.py` file. The format of each spec is as follows:
```
Spec(
        repo=<reponame>,
        filename=<absolute path of file containing test>,
        classname=<classname; none if no class>,
        testname=<test name>,
        params=<list of all parameters>[ 
            Param(
                name=<name of parameter>,
                param_line=<line number>,
                param_col=<starting column number of the parameter value>,
                param_type=<type of parameter, can be ParamType.ITER for discrete bounded interval or .LR for continous bounded interval or .CHAINS for discrete choices>,
                default_val=<default value of parameter>,
                value_range=<either [min, max] for bounded range or [list of values] for discrete choices>
            ),...
        ],
        assertions=<list of assertions>[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename=<file containing assertion>,
                line=<line number of assertion>,               
                assert_type=<type of assertion, check src/lib/AssertType.py for all types>,
                assert_string=<string form of the assertion>,
                args=<any additional arguments>
            )
        ]
    )
```


## Running the mutation testing experiment (Table 3)

1. Run the setup script as the previous section if the project is not installed. Skip if already installed.
2. From `tool` folder, run `./mutation.sh [PROJECT_NAME] [THREADS] all` to run mutation experiment. This will also produce output in `logs` folder with name `mut_*`. This step runs mutation tests on the original and optimized versions of the tests.
3. Run `cd scripts; python3 mutlogtotable.py ../logs` to print out the results.

For the small scale experiment, we recommend running autokeras project which is the fastest one. Reviewers are welcome to try out other projects. The mutation scores are expected to be similar for original and optimized version.
  

## Reproducing Historical Failures (Table 4)

This experiment shows that both original and optimized test reproduce the historical failure.

To reproduce a historical failure for the failing build as well as the optimized version of the code, run

```   
    cd tool/comparison
    bash compare_script.sh {PROJECT_NAME} {FAILING_SHA} {TEST_NAME}
```

For example, you can run `bash compare_script.sh pyro 7f84f19841f21422b01ffb6010ef91e63939494e tests/infer/test_predictive.py::test_posterior_predictive_svi_manual_guide[False]` to reproduce the pyro failures. This will output if both versions reproduced the failure: "Success. Both tests fail". Note that this script will setup the conda environment for the historical version during first run, which takes some time.

The list of all projects, passing and failing commits is provided under `tool/historical_build_info.csv`. Use the hash provided in the  `after` column  and the testname in `test` column for input above.


The script `tool/comparison/before_script.sh` can be used to run the optimizer for historical builds (optional).

Please note that the commit used for optimizer set up is different than the one used for bug reproduction so it is advised to clean the projects directory before switching from one to the other. You can use `bash lib_reset.sh` to do this for all projects.

Note that this package does not support all the historical failures, since some of the old dependencies of some projects are not available anymore. For instance, this package cannot reproduce the tests from `gensim` project. However, it should work for other projects.

## Reproducing Time Consumed by selected Tests (Table 1)

Go to `tool` folder. Run `python3 spec_times.py` to print out the times consumed by tests we selected as % of total testing time. It will print out results in same format as Table 1. Note that this excludes the "Description" column, which was manually included in the paper.

================================
# Reproducing all results
================================

We provide all the log files from our experiments as shown in Tables 2, 3, and 5 in the file `all_results.tar.gz`. It contains two folders: `mutation_results` and `optimization_results`. You can download, untar, and then run the following scripts to get the full table:

`python3 logsummarytotable.py /path/to/optimization_results` (Table 2)

`python3 mutlogtotable.py /path/to/mutation_results` (Table 3)

`python3 logtimestotable.py /path/to/optimization_results` (Table 5)

==========================================
# Claims supported by the package
==========================================

We support the following claims in this package

- Optimization: TERA reduces the execution time of a test while preserving the passing probability of the test. This is supported by the experiments involving the optimizer above. 
- Fault detection ability of the test remains similar to the original. This is supported by the mutation experiments above.
- Optimized tests can reproduce historical failures (Table 4). We do not provide full support for reproducing this claim in this package, since this requires reproducing some very old builds/dependency versions, which are not available right now. We only provide the code versions and some scripts to run the original and optimized version of the tests for the repositories, although not all of them may work. At the time of creating this package, we were able to reproduce failures for all projects except `gensim`.

### Common runtime issues
- If you are running docker for the first time, it may take some time to download the ubuntu image file (~2-15 mins depending on network speed). The image is cached for subsequent runs. Please wait for sometime if you do not see any output.

- Each project installation script will take around 5-10 minutes. Each installed conda environment typically occupies >1gb space.

- Since TERA instruments the test files, if you kill the script during execution it might prevent TERA from reverting those changes. In such a scenario, use `git checkout -- .` in the project folder under `projects` or use the `bash lib_reset.sh` file to do it automatically for all projects 

- If running a bash script using `./<scriptname>.sh` throws an error, you can either use `bash <scriptname>.sh` or use `chmod +x <scriptname>.sh` to make it executable

