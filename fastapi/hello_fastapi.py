from fastapi import FastAPI


import uvicorn


app = FastAPI() # 实例化


@app.get("/hello")
async def root(): # 查
    return {"message": "hello fastapi!"}



@app.get("/get")
async def get_test():
    return {"methold":"get methold!"}


@app.post("/post")       # 增
async def post_test():
    return {"methold":"post methold!"}



@app.put("/put")    # 改
async def put_test():
    return {"methold":"put methold!"}


@app.delete("/delete") # 删
async def delete_test():
    return {"methold":"put methold!"}





if __name__ == "__main__":
    uvicorn.run("hello_fastapi:app", host="127.0.0.1", port=8000)
