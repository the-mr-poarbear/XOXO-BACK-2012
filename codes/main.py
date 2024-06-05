from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from codes import  models, schemas
from codes.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def ReadUsers(db : Session = Depends(get_db)):
    return db.query(models.Users).all()



@app.get("/top10")
def get_top_10(db: Session = Depends(get_db)):
    query = db.query(models.Users).order_by(desc(models.Users.score)).limit(10)
    result = query.all()
    return [{"name": row.name, "score": row.score} for row in result]



@app.post("/")
def CreateUser(user : schemas.User , db : Session = Depends(get_db)):
    user_model = models.Users()
    user_model.name = user.name 
    user_model.score = user.score

    db.add(user_model)
    db.commit()

    return user

@app.put("/")
def UpdateUser(name , status ,  db : Session = Depends(get_db) ):
        user_model = db.query(models.Users).filter(models.Users.name == name).first()
        
        if user_model is None :
             raise HTTPException(
                  status_code=404,
                  detail="User Was Not Found"
             )
        
        if status == "WIN" :
            user_model.score += 1
        elif status == "LOSE" :
             user_model.score -= 1

        db.add(user_model)
        db.commit()

        return user_model
