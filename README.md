# Information Retrieval


## Setup

```
python -m venv venv
```

```
.\venv\Scripts\Activate.ps1
```

```
pip install -r requirements.txt
```

## In the terminal, run

```
uvicorn main:app --reload
```

`filename`(main):`fastapi_instance_name` (app)

## Postman

### Input
POST localhost:8000

Body raw JSON

```json
{
    "user_input": "What is the work station?"
}
```

### Output

```json
{
    "user_input": "What is the work station?",
    "distance": 1.167005873213956,
    "preidcted_q": "How to set the products and stations that operators can work on?",
    "preidcted_ans": "Service center background -> Service Settings -> Station Settings, select the operator, click [product Settings] to check the product, you can set the operator can work on the product; Click `Station Settings` to check `station Settings` to set the station that the operator can operate."
}
```