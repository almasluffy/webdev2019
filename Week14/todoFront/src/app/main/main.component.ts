import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { TaskLIst, Tasks, IPage } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public taskLists: TaskLIst[] = [];
  public tasks: Tasks[] = [];
  public name: any= '';
  public se_name: string = '';

  public login: any = '';
  public password: any = '';

  public logged = false;

  public taskList: TaskLIst;
  public minC: number;
  public maxC: number;

  public t_name: string = null;
  public complexity: number = null;
  public status: string = null;

  public c_tasks: Tasks[] = [];
  public c_task: Tasks;


  public pagelimit: number = 1;
  public pageoffset: number = 0;
  public nextUrl: string = '';
  public prevUrl: string = '';
  public curTaskList: TaskLIst;
  public curUrl: string = '';

  constructor(private provider: ProviderService) { }

  

  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }

    if(this.logged){
    this.provider.getTaskList().then(res=>{
      this.taskLists= res;
      });
    

    }
}

  paginateTasks(task_list: TaskLIst){
    this.provider.paginateTasks(this.curUrl).then(res => {
      this.curTaskList = task_list;
      this.curUrl = `http://127.0.0.1:8000/api/task_lists/${this.curTaskList.id}/tasks/?limit=${this.pagelimit}&offset=${this.pageoffset}`;
      this.tasks = res.results;
      this.nextUrl = res.next;
      this.prevUrl = res.previous;
    });
  }

  nextpage(){
    if (this.nextUrl != null) {
      this.curUrl = this.nextUrl;
      this.paginateTasks(this.curTaskList);
    }
  }

  prevpage(){
    if (this.prevUrl != null) {
      this.curUrl = this.prevUrl;
      this.paginateTasks(this.curTaskList);
    }
  }


  getTasks(task_list: TaskLIst) {
    this.provider.getTasks(task_list).then(res => {
      this.taskList = task_list;
      this.tasks = res;
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
      this.taskLists = r;
    });
  });
  }

  createTaskList(){
    if(this.name !== ''){
      this.provider.createTaskList(this.name).then(res=>{
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }

  // create(){
   
  //   // console.log(this.t_name);
  //   // console.log(this.complexity);
  //   // console.log(this.status);
  //   let self = this;
  //   self.c_task.status = self.status;
  //   console.log(self.c_task.status);
  // }

  search(){
    this.provider.search(this.se_name, this.taskList.id).then(res=>{
      this.tasks = res;
    });
  }

  asc(){
    this.provider.asc(this.taskList.id).then(res=>{
      this.tasks = res;
    });
  }
  desc(){
    this.provider.desc(this.taskList.id).then(res=>{
      this.tasks = res;
    });
  }

  filter(){
    this.provider.filter(this.taskList.id, this.minC, this.maxC).then(res=>{
      this.tasks = res;
    });
  }


  auth(){
    if(this.login !== '' && this.password !==''){
      this.provider.auth(this.login, this.password).then(r=>{
        localStorage.setItem('token', r.token);
        this.logged = true;
        this.provider.getTaskList().then(res=>{
          this.taskLists= res;
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
