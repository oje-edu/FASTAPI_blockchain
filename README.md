## setup

- python -m venv .venv
- `source .venv/Scripts/activate` for windows
- `source .venv\bin\activate` for linux
- `pip install -r requirements.txt`

## console tests

```py
ipyhton

import blockchain
bc = blockchain.Blockchain()
bc.chain
bc.mine_block("hello world")
bc.mine_block("hello yo")

bc.is_chain_valid()

bc.chain[1]["data"] = "hello yoyo"
bc.is_chain_valid()

bc.chain[1]["data"] = "hello world"
bc.is_chain_valid()
```

## fastapi

- `uvicorn main:app --reload`
- visit: http://localhost:8000/docs
