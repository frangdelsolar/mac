import { Component, Input, OnInit } from '@angular/core';
import { ButtonInterface } from '@core/models/button.interface';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { ClientTypeService } from '../client-type-controller.service';
import { ClientTypeFormComponent } from '../client-type-form/client-type-form.component';
import { ClientTypeEnum } from '../client-type.enum';
import { ClientType } from '../client-type.interface';

@Component({
  selector: 'app-client-type-detail',
  templateUrl: './client-type-detail.component.html',
  styleUrls: ['./client-type-detail.component.scss']
})
export class ClientTypeDetailComponent implements OnInit {
  header: string = "Tipo de cliente";
  subheader: string = "Detalle";
  buttons: ButtonInterface[] = [
    {
      label: 'Editar',
      callback: this.onClickEditItem.bind(this)
    },
  ];

  @Input() objectId!: number;

  object!: ClientType;
  labels = ClientTypeEnum;
  constructor(
    private service: ClientTypeService,
    private dialogSvc: DialogService,
  ) { }

  ngOnInit(): void {
    this.service.getById(this.objectId).subscribe(item=>{
      this.object=item;
    })
  }


  public onClickEditItem(){
    let dialogData: DialogData = {
      component: ClientTypeFormComponent,
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
