import { Component, Inject, Input, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { ClientPlanService } from '../client-plan-controller.service';
import { ClientPlanFormComponent } from '../client-plan-form/client-plan-form.component';
import { clientPlanEnum } from '../client-plan.enum';
import { ClientPlan } from '../client-plan.interface';

@Component({
  selector: 'app-client-plan-modal',
  templateUrl: './client-plan-modal.component.html',
  styleUrls: ['./client-plan-modal.component.scss']
})
export class ClientPlanModalComponent implements OnInit {
  header: string = "Plan de Servicios";
  subheader: string = "Detalle";

  @Input() objectId = null;

  object!: ClientPlan;
  labels = clientPlanEnum;
  constructor(
    private service: ClientPlanService,
    private dialogSvc: DialogService,
    @Inject(MAT_DIALOG_DATA) public dialogData: any
  ) { }

  ngOnInit(): void {
    let id = this.dialogData['id'];
    if (id){
      this.service.getById(id).subscribe(item=>{
        this.object=item;
      })
    }
  }

  onClickEditItem(){
    let dialogData: DialogData = {
      component: ClientPlanFormComponent,
      params: {'id': this.object.id}
    }
    this.dialogSvc.show(dialogData);
    this.dialogSvc.hasClosedObservable.subscribe(res=>{
      if(res){
        this.ngOnInit();
      }
    })
  }

}
