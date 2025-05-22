from fastapi import FastAPI, Path, Query, Header, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional
from datetime import datetime
import uvicorn


app = FastAPI()


@app.get("/user/{user_id}/", status_code=status.HTTP_200_OK)
async def get_user(
    user_id: int = Path(..., description="ID користувача", examples=[1, 42, 100]),
    timestamp: Optional[str] = Query(None, description="Поточний час (не обов'язково)"),
    x_client_version: str = Header(..., description="Версія клієнту")
):
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    response = {
        "user_id": user_id,
        "timestamp": timestamp,
        "X-Client-Version": x_client_version,
        "message": f"Hello, user {user_id}!"
    }

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=80)
