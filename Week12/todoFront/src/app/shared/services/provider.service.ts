import { Injectable, EventEmitter } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { TaskLIst, Tasks } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();
  constructor(http: HttpClient) {
    super(http);
   }

   getTaskList():Promise<TaskLIst[]>
   {
     return this.get('http://127.0.0.1:8000/api/task_lists/', {});
   }
   getProblems(task: TaskLIst): Promise<Tasks[]> {
     return this.get(`http://127.0.0.1:8000/api/task_lists/${task.id}/tasks/`, {});
   }

   createTaskList(name: any): Promise<TaskLIst>{
     return this.post( 'http://127.0.0.1:8000/api/task_lists/', { 
       name: name
     });
   }

   updateTaskList(tasklist: TaskLIst): Promise<TaskLIst>{
    return this.put(`http://127.0.0.1:8000/api/task_lists/${tasklist.id}/`, {
      name: tasklist.name
    });
   }

   deleteTaskList(id: number): Promise<any>{
      return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}/`, {});
   }
   
}
