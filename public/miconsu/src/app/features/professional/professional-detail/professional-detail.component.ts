import { Component, Input, OnInit } from '@angular/core';
import { ButtonInterface } from '@core/models/button.interface';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { ProfessionalService } from '../professional-controller.service';
import { ProfessionalFormComponent } from '../professional-form/professional-form.component';
import { ProfessionalEnum } from '../professional.enum';
import { Professional } from '../professional.interface';

@Component({
  selector: 'app-professional-detail',
  templateUrl: './professional-detail.component.html',
  styleUrls: ['./professional-detail.component.scss']
})
export class ProfessionalDetailComponent implements OnInit {
  header: string = "Profesional";
  subheader: string = "Detalle";
  buttons: ButtonInterface[] = [
    {
      label: 'Editar',
      callback: this.onClickEditItem.bind(this)
    },
  ];

  @Input() objectId!: number;

  object!: Professional;
  labels = ProfessionalEnum;
  constructor(
    private service: ProfessionalService,
    private dialogSvc: DialogService,
  ) { }

  ngOnInit(): void {
    this.service.getById(this.objectId).subscribe(item=>{
      this.object=item;
    })
  }


  public onClickEditItem(){
    let dialogData: DialogData = {
      component: ProfessionalFormComponent,
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
