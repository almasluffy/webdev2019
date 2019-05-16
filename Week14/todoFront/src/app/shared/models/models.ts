    
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