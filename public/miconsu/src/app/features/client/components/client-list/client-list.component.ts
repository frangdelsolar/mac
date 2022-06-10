import { Component, OnInit } from '@angular/core';
import { Client } from '@features/client/client.interface';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-client-list',
  templateUrl: './client-list.component.html',
  styleUrls: ['./client-list.component.scss']
})
export class ClientListComponent implements OnInit {
  header: string = "Clientes";
  subheader: string = "Listado";
  baseUrl= '/';

  objects: Client[] = [
    {
      id: 1,
      name: 'Pepe',
      administrator: "Francisco Javier",
      client_plan: "Plan Eterno",
      client_type: "Profesional"
    },
    {
      id: 2,
      name: 'Roberto',
      administrator: "Francisco Javier",
      client_plan: "Plan Eterno",
      client_type: "Profesional"
    },
    {
      id: 3,
      name: 'Juan Carlos',
      administrator: "Francisco Javier",
      client_plan: "Plan Eterno",
      client_type: "Profesional"
    },
    {
      id: 4,
      name: 'Sebastián',
      administrator: "Francisco Javier",
      client_plan: "Plan Eterno",
      client_type: "Profesional"
    },
    {
      id: 5,
      name: 'Alguien más',
      administrator: "Francisco Javier",
      client_plan: "Plan Eterno",
      client_type: "Profesional"
    },
    {
      id: 6,
      name: 'El último',
      administrator: "Francisco Javier",
      client_plan: "Plan Eterno",
      client_type: "Profesional"
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
        cell: (client: Client) => `${client.id}`,
      },
      {
        columnDef: 'name',
        header: 'Nombre',
        cell: (client: Client) => `${client.name}`,
      },
      {
        columnDef: 'administrator',
        header: 'Administrador',
        cell: (client: Client) => `${client.administrator?.username}`,
      },
      {
        columnDef: 'client_type',
        header: 'Tipo de cliente',
        cell: (client: Client) => `${client.client_type?.name}`,
      },
      {
        columnDef: 'client_plan',
        header: 'Plan',
        cell: (client: Client) => `${client.client_plan?.name}`,
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
