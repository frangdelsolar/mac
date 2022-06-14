import { Component, OnInit } from '@angular/core';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { SnackbarService } from '@core/services/snackbar.service';
import { TableService } from '@shared/elements/table/table.service';
import { ClientTypeService } from '../client-type-controller.service';
import { ClientTypeFormComponent } from '../client-type-form/client-type-form.component';
import { ClientTypeModalComponent } from '../client-type-modal/client-type-modal.component';
import { ClientType } from '../client-type.interface';

@Component({
  selector: 'app-client-type-list',
  templateUrl: './client-type-list.component.html',
  styleUrls: ['./client-type-list.component.scss']
})
export class ClientTypeListComponent implements OnInit {
  header: string = "Tipos de cliente";
  subheader: string = "Listado";
  baseUrl: string = "administrador/tipo-de-cliente";

  columns = [
    {
      columnDef: 'id',
      header: 'Id',
      cell: (client_plan: ClientType) => `${client_plan.id}`,
    },
    {
      columnDef: 'name',
      header: 'Nombre',
      cell: (client_plan: ClientType) => `${client_plan.name}`,
    },
  ];
    
  constructor(
    public service: ClientTypeService, 
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
      component: ClientTypeModalComponent,
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
      component: ClientTypeFormComponent,
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
      component: ClientTypeFormComponent,
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
