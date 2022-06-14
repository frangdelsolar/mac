import { Component, Input, OnInit } from '@angular/core';
import { ButtonInterface } from '@core/models/button.interface';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { clientPlanEnum } from '@features/client-plan/client-plan.enum';
import { ClientService } from '@features/client/client-controller.service';
import { Client } from '@features/client/client.interface';
import { ClientFormComponent } from '../client-form/client-form.component';

@Component({
  selector: 'app-client-detail',
  templateUrl: './client-detail.component.html',
  styleUrls: ['./client-detail.component.scss']
})
export class ClientDetailComponent implements OnInit {
  header: string = "Cliente";
  subheader: string = "Detalle";
  buttons: ButtonInterface[] = [
    {
      label: 'Editar',
      callback: this.onClickEditItem.bind(this)
    },
  ];

  @Input() objectId!: number;

  object!: Client;
  labels = clientPlanEnum;
  constructor(
    private service: ClientService,
    private dialogSvc: DialogService,
  ) { }

  ngOnInit(): void {
    this.service.getById(this.objectId).subscribe(item=>{
      this.object=item;
    })
  }


  public onClickEditItem(){
    let dialogData: DialogData = {
      component: ClientFormComponent,
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
