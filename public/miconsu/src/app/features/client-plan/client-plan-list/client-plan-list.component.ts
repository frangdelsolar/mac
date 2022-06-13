import { Component, OnInit } from '@angular/core';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { SnackbarService } from '@core/services/snackbar.service';
import { TableService } from '@shared/elements/table/table.service';
import { ClientPlanService } from '../client-plan-controller.service';
import { ClientPlanFormComponent } from '../client-plan-form/client-plan-form.component';
import { ClientPlanModalComponent } from '../client-plan-modal/client-plan-modal.component';
import { ClientPlan } from '../client-plan.interface';

@Component({
  selector: 'app-client-plan-list',
  templateUrl: './client-plan-list.component.html',
  styleUrls: ['./client-plan-list.component.scss']
})
export class ClientPlanListComponent implements OnInit {
  header: string = "Planes de Servicio";
  subheader: string = "Listado";
  baseUrl: string = "administrador/plan";

  columns = [
    {
      columnDef: 'id',
      header: 'Id',
      cell: (client_plan: ClientPlan) => `${client_plan.id}`,
    },
    {
      columnDef: 'name',
      header: 'Nombre',
      cell: (client_plan: ClientPlan) => `${client_plan.name}`,
    },
  ];
    
  constructor(
    public service: ClientPlanService, 
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
      component: ClientPlanModalComponent,
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
      component: ClientPlanFormComponent,
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
      component: ClientPlanFormComponent,
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
