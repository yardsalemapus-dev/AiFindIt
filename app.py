from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "YardSaleMap backend is alive!"}

@app.get("/api/sales")
def get_sales():
    return [
        {"id": 1, "title": "Sample Sale", "address": "123 Main St", "lat": 27.95, "lng": -82.46},
        {"id": 2, "title": "Another Sale", "address": "456 Oak Ave", "lat": 28.54, "lng": -81.38}
    ]
