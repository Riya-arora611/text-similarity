# Text similarity between two documents

## Objective
This guide explains how to calculate text similarity between two documents using Python. Text similarity measures help you determine how closely related or similar two text documents are to each other.


## Setup

1.**Clone the Repository**: Clone this repository to your local machine:

```
git clone https://github.com/Riya-arora611/text-similarity.git
```

2.**Install Dependencies**: Create a virtual environment and Install the required dependencies using pip:

```
python3 -m venv venv
source venv/bin/activate
cd backend
pip3 install -r requirements.txt
cd ..

cd frontend
pip3 install -r requirements.txt
cd ..
```

3.**Start the server**: To start the server for the model you can run:

```
python3 frontend/main.py
```
and in new terminal start frontend server using streamlt UI:

```streamlit run backend/streamlit_app.py```


### Input
The  input of this module is two documents from local in .docx and .pdf format only. Now to send request to the server you can use:

```
curl --location --request POST 'http://127.0.0.1:8000/text-similarity' --header 'Content-Type: application/json'  --data-raw '{"text1":"Hello how are you","text2":"hi how are you"}'
```


## Containerising this code

1. If you want to run this in a docker container, the docker file is already made for this purpose. You can just build the image using:

```
sudo docker build -t text-similarity_v0.1 .  
```

2. Once the image is successfully built you can check it using:

```
sudo docker images
```

Here you should be able to see your image.

3. To run the image on the port you want to, run using:

```
sudo docker run -p 8000:8000 text-similarity_v0.1
```

Now to take inference from this server you can use the following curl command:

```
curl --location --request POST 'http://0.0.0.0:8000/text-similarity' --header 'Content-Type: application/json' --data-raw '{"text1":"Hello how are you","text2":"Hi How are you"}'
```

## Solution

This code is designed to calculate the similarity score between two text documents, using BERT embeddings and cosine similarity. Here's a summary of what each part of the code does:

- Load Pre-trained BERT Model and Tokenizer: It loads a pre-trained BERT model (bert-base-uncased) and its corresponding tokenizer. BERT (Bidirectional Encoder Representations from Transformers) is a state-of-the-art language representation model.


- Encode Text into BERT Embeddings: It encodes the extracted text from the resume and job description into BERT embeddings using the bert_encode function.

- Compute Similarity Score: The code calculates the similarity score between the two sets of BERT embeddings using cosine similarity. The similarity score represents how closely related the resume and job description are in terms of content. It's a value between -1 and 1, with higher values indicating greater similarity.

The output of this can be seen here:

```
{"similarity_score":0.9729417562484741}
```



A demonstration of Docker to implement a simple 2 tier architecture frontend will be able to access the backend In order to run this in docker, simply type
```
sudo docker-compose up
```
at the command prompt.