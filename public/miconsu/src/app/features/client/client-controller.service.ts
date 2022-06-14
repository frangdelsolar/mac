import { Injectable } from '@angular/core';
import { PaginatedResponse } from '@core/models/paginated-response.interface';
import { PrivateApiService } from '@core/services/privateApi.service';
import { environment } from '@env/environment';
import { Client } from './client.interface';


@Injectable({
  providedIn: 'root',
})
export class ClientService {
  
  _apiUrl = environment.apiUrlClient;

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
    return this.adminSvc.get<Client>(this._apiUrl, id, true);
  }

  public create(body: Client){
    return this.adminSvc.post<Client>(this._apiUrl, body, true);
  }

  public update(id: number, body: Client){
    return this.adminSvc.put<Client>(this._apiUrl, body, id, true);
  }

  public delete(id: number) {
      return this.adminSvc.delete(this._apiUrl, id, true);
  }

}