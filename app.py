#!/usr/bin/env python

from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    query_res =querydb()
    return query_res


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')