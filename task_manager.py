class User:

    def __init__(self,name):
        self.name = name 
        self.task_counter = 1
        self.task_list = {}
        
    
    def add_task(self, day, task_explanetion):
        
        self.task_list[self.task_counter] = {
            "Day": day,
            "Task": task_explanetion
        }
        self.task_counter += 1
            
    def read_task(self,day_to_read):
          for task_id, task in self.task_list.items():
            if day_to_read == task['Day']:
                print(f"{task_id}: {task['Task']}")
                
    def delete_task(self,day_to_read,task_to_delete):
        for task_id, task in list(self.task_list.items()):  
            if day_to_read == task['Day'] and task_to_delete == task['Task']:
                self.task_list.pop(task_id)
                print(f"Task '{task_to_delete}' on {day_to_read} deleted.")
                return
        print("Task not found.")
     
def introduction():
    print("Hello it's task bar program")
    print("Choose what u want")
    print("""1 - Add some task
             2 - Delete task
             3 - Read task
             4 - Quit""")