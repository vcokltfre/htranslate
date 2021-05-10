from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from htranslate import translate_to_h, translate_from_h


class TranslationRequest(BaseModel):
    text: str
    delim: str = " "


app = FastAPI(docs_url=None, redoc_url="/docs", swagger_ui_oauth2_redirect_url=None)

@app.get("/translate/to")
async def translate_to(req: TranslationRequest) -> str:
    """Translate a given string into h binary."""

    try:
        return translate_to_h(req.text, req.delim)
    except:
        raise HTTPException(400, "Bad input given.")

@app.get("/translate/from")
async def translate_from(req: TranslationRequest) -> str:
    """Translate from h binary to a string."""

    try:
        return translate_from_h(req.text, req.delim)
    except:
        raise HTTPException(400, "Bad input given.")
