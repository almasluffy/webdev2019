import { Injectable, EventEmitter } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { TaskLIst, Tasks, IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();
  constructor(http: HttpClient) {
    super(http);
   }

   search(se_name: string, t_id: number):Promise<Tasks[]>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/${t_id}/tasks/?search=` + se_name,{} );
   }

   filter(t_id: number, minC: number, maxC: number): Promise<Tasks[]>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/16/tasks/?min_cmx=${minC}&max_cmx=${maxC}`,{});
   }
   
   asc(t_id: number): Promise<Tasks[]>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/${t_id}/tasks/?ordering=complexity`, {});

   }
   desc(t_id: number): Promise<Tasks[]>{
    return this.get(`http://127.0.0.1:8000/api/task_lists/${t_id}/tasks/?ordering=-complexity`, {});
   }

   getTaskList():Promise<TaskLIst[]>
   {
     return this.get('http://127.0.0.1:8000/api/task_lists/', {});
   }
   getTasks(task_list: TaskLIst): Promise<Tasks[]> {
     return this.get(`http://127.0.0.1:8000/api/task_lists/${task_list.id}/tasks/`, {});
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

   auth(login: any, password: any):Promise<IAuthResponse>{
     return this.post('http://127.0.0.1:8000/api/login/',{
    username: login,
    password: password
     });
   }

   logout(): Promise<any>{
     return this.post('http://127.0.0.1:8000/api/logout/',{

     });
   }
   
}
