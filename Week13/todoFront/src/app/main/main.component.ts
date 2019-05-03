import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { TaskLIst, Tasks } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public my_tasks: TaskLIst[] = [];
  public problems: Tasks[] = [];
  public name: any= '';

  public login: any = '';
  public password: any = '';

  public logged = false;

  constructor(private provider: ProviderService) { }

  

  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }

    if(this.logged){
    this.provider.getTaskList().then(res=>{
      this.my_tasks= res;
      });
    }
  }

  getProblems(problem: TaskLIst) {
    this.provider.getProblems(problem).then(res => {
      this.problems = res;
    });
  }

  updateTaskList(t: TaskLIst){
    this.provider.updateTaskList(t).then(res =>{
       console.log(t.name + 'updated')
    });
  }

  deleteTaskList(t: TaskLIst){
    this.provider.deleteTaskList(t.id).then(res=>{
         console.log(t.name + "deleted");
    this.provider.getTaskList().then(r=>{
      this.my_tasks = r;
    });
  });
  }

  deleteTask(t: TaskLIst, t2 : Tasks){
    this.provider.deleteTask(t.id, t2.id).then(res=>{
         console.log(t.name + "deleted");
    this.provider.getProblems(t).then(r=>{
      this.my_tasks = r;
    });
  });
  }

  createTaskList(){
    if(this.name !== ''){
      this.provider.createTaskList(this.name).then(res=>{
        this.name = '';
        this.my_tasks.push(res);
      });
    }
  }


  auth(){
    if(this.login !== '' && this.password !==''){
      this.provider.auth(this.login, this.password).then(r=>{
        localStorage.setItem('token', r.token);
        this.logged = true;
        this.provider.getTaskList().then(res=>{
          this.my_tasks= res;
          });
      });
    }
  }

  logout(){
    this.provider.logout().then(res=>{
      localStorage.clear();
      this.logged = false;
    })
  }

}
