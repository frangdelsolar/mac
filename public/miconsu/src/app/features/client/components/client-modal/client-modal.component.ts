import { Component, Inject, Input, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { clientPlanEnum } from '@features/client-plan/client-plan.enum';
import { ClientService } from '@features/client/client-controller.service';
import { Client } from '@features/client/client.interface';
import { ClientFormComponent } from '../client-form/client-form.component';

@Component({
  selector: 'app-client-modal',
  templateUrl: './client-modal.component.html',
  styleUrls: ['./client-modal.component.scss']
})
export class ClientModalComponent implements OnInit {
  header: string = "Cliente";
  subheader: string = "Detalle";

  @Input() objectId = null;

  object!: Client;
  labels = clientPlanEnum;
  constructor(
    private service: ClientService,
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
      component: ClientFormComponent,
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
