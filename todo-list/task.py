import uuid
from datetime import datetime

class taskEntity():
    def __init__(self, task_name, task_status):
        self.task_id = self.generate_uuid()
        self.task_name = task_name
        self.task_status = task_status
        self.task_created_at = self.get_datetime()
        self.task_updated_at = self.get_datetime()
    
    def __str__(self):
        return f"Task ID: {self.task_id}, Task Name: {self.task_name}, Task Status: {self.task_status}, Task Created At: {self.task_created_at}, Task Updated At: {self.task_updated_at}"
    
    def __repr__(self):
        return f"Task ID: {self.task_id}, Task Name: {self.task_name}, Task Status: {self.task_status}, Task Created At: {self.task_created_at}, Task Updated At: {self.task_updated_at}"
    
    def generate_uuid(self):
        return str(uuid.uuid4())
    
    def get_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def update_task(self, task_name, task_status):
        self.task_name = task_name
        self.task_status = task_status
        self.task_updated_at = self.get_datetime()
        return self.__str__()