from fastapi import FastAPI

app = FastAPI(title="Fintech Payment Platform API")


@app.get("/health")
def health():
    return {"status": "ok"}
