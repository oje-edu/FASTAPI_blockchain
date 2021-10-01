import fastapi as _fastapi
import blockchain as _blockchain

blockchain = _blockchain.Blockchain()

app = _fastapi.FastAPI()

@app.post("/mine_block")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
      return _fastapi.HTTPException(status_code=400, detail="Invalid chain")

    block = blockchain.mine_block(data=data)
    return block

@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
      return _fastapi.HTTPException(status_code=400, detail="Invalid chain")

    chain = blockchain.chain
    return chain

@app.get("/previous_block/")
def previous_block():
    if not blockchain.is_chain_valid():
      return _fastapi.HTTPException(status_code=400, detail="Invalid chain")

    previous_block = blockchain.get_previous_block()
    return previous_block

@app.get("/validate/")
def is_blockchain_valid():
    return blockchain.is_chain_valid()

