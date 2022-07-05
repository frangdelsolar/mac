import { Injectable } from '@angular/core';
import { PaginatedResponse } from '@core/models/paginated-response.interface';
import { PrivateApiService } from '@core/services/privateApi.service';
import { environment } from '@env/environment';
import { Profile } from './profile.interface';


@Injectable({
  providedIn: 'root',
})
export class ProfileService {
  
  _apiUrl = environment.apiUrlProfile;

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
    return this.adminSvc.get<Profile>(this._apiUrl, id, true);
  }

  public create(body: Profile){
    return this.adminSvc.post<Profile>(this._apiUrl, body, true);
  }

  public update(id: number, body: Profile){
    return this.adminSvc.put<Profile>(this._apiUrl, body, id, true);
  }

  public delete(id: number) {
      return this.adminSvc.delete(this._apiUrl, id, true);
  }

}