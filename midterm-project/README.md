
# *Classification based on gene expressions* 

## Problem Description

Classifying breast cancer patients based on gene expression is a binary classification problem. The aim is to predict whether a patient has breast cancer or not, using gene expression information. Gene expression refers to the amount of proteins produced from a person’s genes. In this case, gene expression of a patient’s mammary cells is analyzed to determine whether they have breast cancer or not. Binary classification is a common problem in machine learning.

### Context 

The data used in this project was collected by the Cancer Genome Atlas (TCGA) program of the National Cancer Institute (NCI). TCGA is a cancer genomics program that has molecularly characterized more than 20,000 primary cancer samples and matched normal samples spanning 33 cancer types. TCGA data has led to improvements in the ability to diagnose, treat, and prevent cancer and is publicly available for any member of the research community to use.

### Significance

Binary classification based on gene expression of breast cancer patients can have several significant implications. Firstly, it can help doctors identify patients who have breast cancer and provide them with early and effective treatment. Secondly, it can help researchers better understand the biology of breast cancer and develop new treatments and therapies. Thirdly, it can help patients make informed decisions about their medical care and better understand their diagnosis.


## Data

The data used is compressed in the Data folder. Breast cancer dataset downloaded from Firehose [https://gdac.broadinstitute.org/](https://gdac.broadinstitute.org/). These are next generation sequencing data that are provided already normalized.

The dataset we are loading is called "BRCA.rnaseqv2illuminahiseq_rnaseqv2unc_eduLevel_3RSEM_genes_normalized__data.data.txt".

It looks like this:

Hybridization REF TCGA.3C.AAAU.01A.11R.A41B.07 TCGA.3C.AALI.01A.11R.A41B.07 ...

gene_id normalized_count normalized_count ...

?|100130426 0.0000 0.0000 ...

This dataset has genes as rows and patients as columns. Patient IDs refer to TCGA IDs such as TCGA.3C.AAAU.01A.11R.A41B.07, etc. 

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.


## Getting Started

This is a set of instructions on setting up this project locally. To get a local copy up and running follow these simple example steps.

Prerequisites. This is list things you need to use this software.

- Python
- Pipenv
- Docker 

### Installing Dependencies

You can install the dependencies with pipenv, as they are specified in the `Pipfile` and `Pipfile.lock`, by running the following commands:

```
pipenv install
pipenv shell
```

### Building the model

You have the option to execute either the `train.py` file  to carry out all the necessary steps for training the final model used in this project.

To initiate the model training, you can use the following command:

```
python train.py
```

### Serving the model (Locally)

To serve the model with Docker:

1. **First install docker:**

    - *Download Docker Desktop:*
        - Visit the official Docker website: [Docker Desktop](https://www.docker.com/products/docker-desktop).
        - Click on the "Get Docker Desktop for Windows" button.
        - You will be redirected to the download page. Download the installation file here.

    - *Install Docker Desktop:*
        - Run the installation file you just downloaded.
        - Follow the installer instructions to complete the installation.

    - *Launch Docker Desktop:*
        - Once installed, look for Docker Desktop in your start menu and run it.
    
    - *Verify the Installation:*
        - Open a terminal and run the following command to verify that Docker is installed correctly:
        
            ```bash
            docker --version
            ```
        - You can also run:
            ```bash
            docker run hello-world
            ```
        - This will download a small image, run it, and you should see a message indicating that Docker is working correctly.
    
    And that's it! Now you should have Docker installed and ready to use on your Windows system.

2. **Click and initialize the DOCKER DESKTOP app after installing it:**

    - Maybe it asks you to update wsl. Open your terminal and run the following command:
        ```bash
        wsl --update
        ```

3. **Build the Docker image and run it:**

    - *Build the Docker image*
        - Open a new terminal, enter the 'Midterm_Project' folder and run the following command:
            ```
            docker build -t midterm-project .
            ```
        
        - REMEMBER THE DOT (.) IN THE LAST COMMAND!!!This command builds a Docker image from the provided files.

    - *Run the previous image*
        ```
        docker run -it --rm -p 9696:9696 midterm-project
        ```
        - This command runs a container based on the previously built image. Maps port 9696 on the host system to port 9696 on the container. This is important if the application inside the container is listening on port 9696.

### Testing the model

Finally, you can test the model. Serving the model locally, open another terminal, and:

```
python predict_test.py
```

