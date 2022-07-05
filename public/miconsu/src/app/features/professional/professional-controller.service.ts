import { Injectable } from '@angular/core';
import { PaginatedResponse } from '@core/models/paginated-response.interface';
import { PrivateApiService } from '@core/services/privateApi.service';
import { environment } from '@env/environment';
import { Professional } from './professional.interface';


@Injectable({
  providedIn: 'root',
})
export class ProfessionalService {
  
  _apiUrl = environment.apiUrlProfessional;

  constructor(private adminSvc: PrivateApiService) {}

  public getAll(){
    let url = this._apiUrl;
    return this.adminSvc.get<PaginatedResponse>(url, null, true);
  }

  public filter(params: string ){
    let url = this._apiUrl;
    url += params;
    return this.adminSvc.get<PaginatedResponse>(url, null, true);
  }

  public getById(id: number){
    return this.adminSvc.get<Professional>(this._apiUrl, id, true);
  }

  public create(body: Professional){
    return this.adminSvc.post<Professional>(this._apiUrl, body, true);
  }

  public update(id: number, body: Professional){
    return this.adminSvc.put<Professional>(this._apiUrl, body, id, true);
  }

  public delete(id: number) {
      return this.adminSvc.delete(this._apiUrl, id, true);
  }

}