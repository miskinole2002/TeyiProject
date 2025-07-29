# uvicorn Backend.app:app --host 0.0.0.0 --port 8002 --workers 1 --reload 
#!/bin/bash
# Utilise le Python de ton environnement directement pour lancer uvicorn
./env/Scripts/python -m uvicorn Backend.app:app --reload
