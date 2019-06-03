    
export interface TaskLIst {
    id: number;
    name: string;
  }

export interface Tasks{
    id: number,
    name: string;
    complexity: number;
    status: string;
}
export interface IAuthResponse{
  token: string;
}

export interface IPage {
  next: string;
  previous: string;
  results: Tasks[];
}