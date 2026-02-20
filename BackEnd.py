# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 19:37:46 2026

@author: rjunco
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando 🚀"}

@app.get("/gastos")
def gastos():
    return [
        {"id":1,"concepto":"luz","cantidad":50},
        {"id":2,"concepto":"agua","cantidad":30}
    ]