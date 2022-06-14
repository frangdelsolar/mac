import { Component, Input, OnInit } from '@angular/core';
import { ButtonInterface } from '@core/models/button.interface';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { ClientPlanService } from '../client-plan-controller.service';
import { ClientPlanFormComponent } from '../client-plan-form/client-plan-form.component';
import { clientPlanEnum } from '../client-plan.enum';
import { ClientPlan } from '../client-plan.interface';

@Component({
  selector: 'app-client-plan-detail',
  templateUrl: './client-plan-detail.component.html',
  styleUrls: ['./client-plan-detail.component.scss']
})
export class ClientPlanDetailComponent implements OnInit {
  header: string = "Plan de Servicios";
  subheader: string = "Detalle";
  buttons: ButtonInterface[] = [
    {
      label: 'Editar',
      callback: this.onClickEditItem.bind(this)
    },
  ];

  @Input() objectId!: number;

  object!: ClientPlan;
  labels = clientPlanEnum;
  constructor(
    private service: ClientPlanService,
    private dialogSvc: DialogService,
  ) { }

  ngOnInit(): void {
    this.service.getById(this.objectId).subscribe(item=>{
      this.object=item;
    })
  }


  public onClickEditItem(){
    let dialogData: DialogData = {
      component: ClientPlanFormComponent,
      params: {'id': this.objectId}
    }
    this.dialogSvc.show(dialogData);
    this.dialogSvc.hasClosedObservable.subscribe(res=>{
      if(res){
        this.ngOnInit();
      }
    })
  }
}
