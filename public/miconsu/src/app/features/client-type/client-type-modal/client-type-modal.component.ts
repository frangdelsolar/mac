import { Component, Inject, Input, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { ClientTypeService } from '../client-type-controller.service';
import { ClientTypeFormComponent } from '../client-type-form/client-type-form.component';
import { ClientTypeEnum } from '../client-type.enum';
import { ClientType } from '../client-type.interface';

@Component({
  selector: 'app-client-type-modal',
  templateUrl: './client-type-modal.component.html',
  styleUrls: ['./client-type-modal.component.scss']
})
export class ClientTypeModalComponent implements OnInit {
  header: string = "Tipo de cliente";
  subheader: string = "Detalle";

  @Input() objectId = null;

  object!: ClientType;
  labels = ClientTypeEnum;
  constructor(
    private service: ClientTypeService,
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
      component: ClientTypeFormComponent,
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
