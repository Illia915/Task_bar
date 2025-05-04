from task_manager import *


Illia = User("Illia")

Illia.add_task(20,"Go for a wolk")
Illia.add_task(1,"Go shit")
Illia.add_task(2,"Go to the shower")

Illia.read_task(20)
Illia.delete_task(20,"Go for a wolk")
Illia.read_task(20)
