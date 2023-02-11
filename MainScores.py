from fastapi import FastAPI
from starlette.responses import HTMLResponse
import Utils

app = FastAPI()

@app.get("/")
async def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as score_file:
            score = score_file.read().strip()
            h1 = f'The score is <div id="score">{score}</div>'
            if score == '':
                h1 = 'The file is empty!'
            return HTMLResponse(f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>{h1}</h1>
                </body>
            </html>""")
    except Exception as e:
        return HTMLResponse(f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{e}</div></h1>
            </body>
        </html>""")
