import { Injectable } from '@angular/core';
import { PaginatedResponse } from '@core/models/paginated-response.interface';
import { PrivateApiService } from '@core/services/privateApi.service';
import { environment } from '@env/environment';
import { ClientPlan } from './client-plan.interface';


@Injectable({
  providedIn: 'root',
})
export class ClientPlanService {
  
  _apiUrl = environment.apiUrlClientPlan;

  constructor(private adminSvc: PrivateApiService) {}

  public getAll(){
    let url = this._apiUrl;
    return this.adminSvc.get<PaginatedResponse>(url, null, true);
  }

  public search(params: string ){
    let url = this._apiUrl;
    url += params;
    return this.adminSvc.get<PaginatedResponse>(url, null, true);
  }

  public getById(id: number){
    return this.adminSvc.get<ClientPlan>(this._apiUrl, id, true);
  }

  public create(body: ClientPlan){
    return this.adminSvc.post<ClientPlan>(this._apiUrl, body, true);
  }

  public update(id: number, body: ClientPlan){
    return this.adminSvc.put<ClientPlan>(this._apiUrl, body, id, true);
  }

  public delete(id: number) {
      return this.adminSvc.delete(this._apiUrl, id, true);
  }

}