from fastapi import FastAPI,Request,Form,UploadFile,File
import uvicorn
import os,sys
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse,StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
app=FastAPI()
load_dotenv()

app.add_middleware(SessionMiddleware,secret_key=os.getenv("secret_key"),max_age=1000)
templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"templates"))
templates=Jinja2Templates(directory=templates_dir)


#static 
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"static"))
app.mount("/static",StaticFiles(directory=static_dir), name="static")



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sadeufotsing2002:brO3ZTgP5lNpvQqu@cluster0.xtie1iq.mongodb.net/Teyi?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
db=client['teyi']
user_collection=client['users']




@app.get("/")
async def home_page(request:Request):

    
   

        return templates.TemplateResponse("home.html",{"request":request })

@app.get('/register')
async def signup(request:Request):

        return templates. TemplateResponse('signup.html',{"request":request })

@app.post('/register')
async def signup(request:Request, nom:str=Form(...), email:str=Form(...), phone:str=Form(...),mdp:str=Form(...)):

        user={
                'nom':nom,
                'email':email,
                'phone':phone,
                'mdp':mdp,
                'role':1
       }
        x=user_collection.insert_one(user)
        print(x)

        return RedirectResponse(url="/login",status_code=302)

@app.get('/login')
async def log(request:Request):

        return templates. TemplateResponse('dashboard.html',{"request":request })


@app.get('/add')
async def addproduct(request:Request):

        return templates. TemplateResponse('dashboard.html',{"request":request })





if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0', port=8002, workers=1)