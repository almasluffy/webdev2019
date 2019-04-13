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

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskList().then(res=>{
      this.my_tasks= res;
      });
  }

  getProblems(problem: TaskLIst) {
    this.provider.getProblems(problem).then(res => {
      this.problems = res;
    });
  }

}
