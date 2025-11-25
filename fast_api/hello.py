from fastapi import FastAPI, Body, Header, Response

from fast_api.chapter.ch3.web import tag

app = FastAPI()

app.include_router(tag.router)

@app.get("/hi")
def greet(who: str):
    return f"Hello, {who}!"

@app.post("/hi")
def  greet_post(response: Response, who: str = Body(embed=True), h11_11: str = Header(embed=True)):
    response.headers["X_Hello"] = "Hello, World!"
    return f"Hello, {who}! {h11_11}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
