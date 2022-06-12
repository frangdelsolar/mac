import { Injectable } from '@angular/core';
import { PaginatedResponse } from '@core/models/paginated-response.interface';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TableService {

  private _data: BehaviorSubject<any> = new BehaviorSubject<any>(null);
  private _refresh: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);

  constructor() { }

  setTableData(data: PaginatedResponse){
    this._data.next(data);
    this._refresh.next(true);
  }

  get TableDataObservable(): Observable<PaginatedResponse> {
    return this._data.asObservable();
  }

  get refreshObservable(): Observable<boolean> {
    return this._refresh.asObservable()
  }


}
