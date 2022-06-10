import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ClientPlan } from '../client-plan.interface';

@Component({
  selector: 'app-client-plan-list',
  templateUrl: './client-plan-list.component.html',
  styleUrls: ['./client-plan-list.component.scss']
})
export class ClientPlanListComponent implements OnInit {
  header: string = "Planes de Servicio";
  subheader: string = "Listado";
  baseUrl= '/';

  objects: ClientPlan[] = [
    {
      id: 1,
      name: 'Plan Eterno',
    },
    {
      id: 2,
      name: 'Plan Nuevo',
    },
    {
      id: 3,
      name: 'Plan 3',
    },
    {
      id: 4,
      name: 'Plan 4',
    },
    {
      id: 5,
      name: 'Plan 5',
    },
    {
      id: 6,
      name: 'Plan 6',
    }
  ]

  values$ = new Observable<any>();
  // this.values$.next({
  //     count: 6, 
  //     previous: 4,
  //     next: 7,
  //     results: this.objects
  //   })
  
    columns = [
      {
        columnDef: 'id',
        header: 'Id',
        cell: (client: ClientPlan) => `${client.id}`,
      },
      {
        columnDef: 'name',
        header: 'Nombre',
        cell: (client: ClientPlan) => `${client.name}`,
      }
    ];


  constructor(

    ) { }

  ngOnInit(): void {

  }

  addItem(){

  }

  editItem(id: any){

  }

  deleteItem(id: number){

  }
}
