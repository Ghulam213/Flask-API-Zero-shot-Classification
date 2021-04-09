# Flask API Zero Shot Classification

This repo contains a flask API which lets people use Zero Shot Classifier from famous transformer library without any configuration. 

## Installation

Clone the Repo using Git.

```bash
git clone https://github.com/Ghulam213/Flask-API-Zero-shot-Classification.git
```

## Usage

After you have cloned the repo, install requirements by running following command.

```bash
pip install -r requirements.txt
```

Now Run the flask app by following command.

```bash
python server.py
```

Now you are ready to send POST request. You can use Postman for this purpose. The request is send to [YOUR_LOCALHOST]/zero-shot-classification/classify

Sample data 
```
{
     "sentence": "This computer is slow!",
     "categories": ["IT issue", "Price request", "Datetime query"]
}
```

Sample Response 
```
{
     "Datetime query": 0.009726298041641712,
     "IT issue": 0.9686093330383301,
     "Price request": 0.02166430838406086
}
```
