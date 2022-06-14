import { Component, OnInit } from '@angular/core';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { SnackbarService } from '@core/services/snackbar.service';
import { ClientService } from '@features/client/client-controller.service';
import { Client } from '@features/client/client.interface';
import { TableService } from '@shared/elements/table/table.service';
import { ClientFormComponent } from '../client-form/client-form.component';
import { ClientModalComponent } from '../client-modal/client-modal.component';

@Component({
  selector: 'app-client-list',
  templateUrl: './client-list.component.html',
  styleUrls: ['./client-list.component.scss']
})
export class ClientListComponent implements OnInit {
  header: string = "Cliente";
  subheader: string = "Listado";
  baseUrl: string = "administrador/plan";

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
    public service: ClientService, 
    private dialogSvc: DialogService,
    private snackSvc: SnackbarService,
    private tableSvc: TableService
  ) { }

  ngOnInit(): void {
    this.service.getAll().subscribe(res=>{
      this.tableSvc.setTableData(res);
    })
  }

  applyFilter(params: string){
    this.service.filter(params).subscribe(res=>{
      this.tableSvc.setTableData(res);
    })
  }

  viewItem(id: number){
    let dialogData: DialogData = {
      component: ClientModalComponent,
      params: {'id': id}
    }
    this.dialogSvc.show(dialogData);
    this.dialogSvc.hasClosedObservable.subscribe(res=>{
      if(res){
        this.ngOnInit();
      }
    })
  }

  addItem(){
    let dialogData: DialogData = {
      component: ClientFormComponent,
      params: {}
    }
    this.dialogSvc.show(dialogData);
    this.dialogSvc.hasClosedObservable.subscribe(res=>{
      if(res){
        this.ngOnInit();
      }
    })
  }

  editItem(id: number){
    let dialogData: DialogData = {
      component: ClientFormComponent,
      params: {'id': id}
    }
    this.dialogSvc.show(dialogData);
    this.dialogSvc.hasClosedObservable.subscribe(res=>{
      if(res){
        this.ngOnInit();
      }
    })
  }

  deleteItem(id: number){
    this.service.delete(id).subscribe(res=>{
      this.snackSvc.openSnackBar('Elemento eliminado correctamente');
      this.ngOnInit();
    });
  }
}
