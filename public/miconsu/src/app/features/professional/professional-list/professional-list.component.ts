import { Component, OnInit } from '@angular/core';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { SnackbarService } from '@core/services/snackbar.service';
import { TableService } from '@shared/elements/table/table.service';
import { ProfessionalService } from '../professional-controller.service';
import { ProfessionalFormComponent } from '../professional-form/professional-form.component';
import { ProfessionalModalComponent } from '../professional-modal/professional-modal.component';
import { Professional } from '../professional.interface';

@Component({
  selector: 'app-professional-list',
  templateUrl: './professional-list.component.html',
  styleUrls: ['./professional-list.component.scss']
})
export class ProfessionalListComponent implements OnInit {
  header: string = "Profesionales";
  subheader: string = "Listado";
  baseUrl: string = "administrador/tipo-de-cliente";

  columns = [
    {
      columnDef: 'id',
      header: 'Id',
      cell: (item: Professional) => `${item.id}`,
    },
    {
      columnDef: 'first_name',
      header: 'Nombre',
      cell: (item: Professional) => `${item.first_name}`,
    },
    {
      columnDef: 'last_name',
      header: 'Apellido',
      cell: (item: Professional) => `${item.last_name}`,
    },
  ];
    
  constructor(
    public service: ProfessionalService, 
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
      component: ProfessionalModalComponent,
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
      component: ProfessionalFormComponent,
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
      component: ProfessionalFormComponent,
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
