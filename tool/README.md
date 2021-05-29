# Running TERA Optimizer

Step 1: Create `projects` directory in root.

Step 2: Go to `tool/scripts` and run `bash {PROJECT_NAME}_setup.sh ../../projects` to set up the project.

Step 3: Run `python3 optimizer.py -r {PROJECT_NAME}` to run TERA for the project. Check the next section for explanation on other flags used by optimizer.py.

## Explanation of optimizer flags

- Repo Name: -r
- ID of spec: -num
- File name: -file
- Class name: -class
- Test name: -test
- Max probability of failure: -p
- Number of threads: -j
- Convergence threshold: -t

## Docker Set Up

Run `docker build -t borntobeflaky1 .` in root to create the docker image. After that, run `docker run -i -t borntobeflaky1 /bin/bash` to start the container. In the docker env run `bash setup_python.sh`. After that follow the above instructions to run TERA for a project.
