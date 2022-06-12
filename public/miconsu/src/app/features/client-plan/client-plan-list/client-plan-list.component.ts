import { Component, OnInit } from '@angular/core';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { SnackbarService } from '@core/services/snackbar.service';
import { BehaviorSubject } from 'rxjs';
import { ClientPlanService } from '../client-plan-controller.service';
import { ClientPlanFormComponent } from '../client-plan-form/client-plan-form.component';
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

  values!: any;
  refresh = new BehaviorSubject<boolean>(false);

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
      private snackSvc: SnackbarService) { }

  ngOnInit(): void {
    this.values = this.service.getAll()
  }

  addItem(event:any){
    let dialogData: DialogData = {
      component: ClientPlanFormComponent,
      params: {
        model: 'person', 
        referenced_object_id: 3
      }
    }
    this.dialogSvc.show(dialogData);
  }

  editItem(event:any){
    this.refresh.next(true);
    this.snackSvc.openSnackBar('Elemento eliminado correctamente');

  }

  deleteItem(id: number){
    this.service.delete(id).subscribe(res=>{
      this.snackSvc.openSnackBar('Elemento eliminado correctamente');
      this.refresh.next(true);

    });
  }
}
