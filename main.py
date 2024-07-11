from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def devops_noturno():
    return f"""
    <html>
        <body>
            <h1>DevOps Noturno</h1>
            <div style="display: flex; justify-content: space-around;">
                <div style="background-color: green; width: 100px; height: 100px;" onclick="contar('vermelho')">APROVADO</div>
            </div>
        </body>
    </html>
    """
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)