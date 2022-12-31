# Breast Cancer Chatbot

This project focuses on developing an AI Chatbot API for patients of Breast Cancer, and aims 
at answering their questions and concerns regarding the disease. 

This project was developed for an internship program at Folio3 inc.

The Questions and Answers data for this purpose was collected from the following website:

https://emedicine.medscape.com/article/1947145-questions-and-answers?reg=1

If you would like to use this project for any other chatbot purpose, you may replace the data with your own .csv file.

Note: Your data must contain the following:

- Questions (Including Different patterns for each question)
- Answers
- Tags (Keyword for the topic)
- (Optional) Link for the Full Source


## Features

- Streamlit UI
- FastAPI Deployment



## Installation

Install FastAPI

```bash
  pip install FastAPI
```
Install Streamlit
```bash
  pip install streamlit

```
Create a Virtual Environment
```bash
pip install virtualenv
python<version> -m venv <virtual-environment-name>
<virtual-environment-name>\Scripts\activate

```
Install the requirements.txt

```bash
pip install -r /requirements.txt
```
Run the front-end file on cmd
```bash
  streamlit run front.py
```
Run the back-end file on cmd
```bash
  uvicorn main:app --reload
```


## API Reference

#### Train the Model

```http
  GET /api/train
```

#### Self Learning (Add Questions)

```http
  POST /api/addQuestion
```

| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Questions, Index Number` | `string, int` | **Required**. Update Question and Index|


#### Predict The Answer
```http
  POST /api/predict
```


| Request Body | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Question` | `string` | **Required**. Question to Generate Answer|




## Authors

- [Abdullah Wahid](https://www.github.com/Abdullahw72)
- [Ahmed Ashraf](https://github.com/AhmedAshraf982)
- [Neeraj Prakash](https://github.com/neerajparkashsharma)
- [Hasnain Ali](https://github.com/beinghasnain16)

Under the Supervision of
- [Sanif Ali Momin](https://github.com/sanifalimomin)



## Used By

This project is used by the following company:

- Folio3


## Screenshots

![Screenshot 1](https://imgur.com/cVHTqSb.jpg)
![Screenshot 2](https://imgur.com/zZdMUsB.jpg)