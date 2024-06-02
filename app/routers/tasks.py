from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

@router.post("/users/{user_id}/tasks/", response_model=schemas.Task)
def create_task_for_user(user_id: int, task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    return crud.create_task(db=db, task=task, user_id=user_id)

@router.put("/users/{user_id}/tasks/{task_id}/complete", response_model=schemas.Task)
def complete_task_for_user(user_id: int, task_id: int, db: Session = Depends(database.get_db)):
    db_task = crud.complete_task(db=db, task_id=task_id, user_id=user_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found or not authorized")
    return db_task

@router.get("/users/{user_id}/tasks/", response_model=list[schemas.Task])
def get_tasks_for_user(user_id: int, db: Session = Depends(database.get_db)):
    tasks = crud.get_tasks(db=db, user_id=user_id)
    return tasks
