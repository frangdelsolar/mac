import { Component, Inject, Input, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { ProfessionalService } from '../professional-controller.service';
import { ProfessionalFormComponent } from '../professional-form/professional-form.component';
import { ProfessionalEnum } from '../professional.enum';
import { Professional } from '../professional.interface';

@Component({
  selector: 'app-professional-modal',
  templateUrl: './professional-modal.component.html',
  styleUrls: ['./professional-modal.component.scss']
})
export class ProfessionalModalComponent implements OnInit {
  header: string = "Profesional";
  subheader: string = "Detalle";

  @Input() objectId = null;

  object!: Professional;
  labels = ProfessionalEnum;
  constructor(
    private service: ProfessionalService,
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
      component: ProfessionalFormComponent,
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
