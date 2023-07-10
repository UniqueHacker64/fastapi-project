from fastapi import FastAPI

app = FastAPI()

@app.get("/cybersmish")
def predict_output():
    predictions = 0  # Update this value based on your logic
    return {"predictions":"world"}
