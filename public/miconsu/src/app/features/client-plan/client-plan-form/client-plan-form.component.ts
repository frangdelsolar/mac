import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { DialogService } from '@core/services/dialog.service';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

import { SnackbarService } from '@core/services/snackbar.service';
import { ClientPlanService } from '../client-plan-controller.service';


@Component({
  selector: 'app-client-plan-form',
  templateUrl: './client-plan-form.component.html',
  styleUrls: ['./client-plan-form.component.scss']
})
export class ClientPlanFormComponent implements OnInit {
  
  header: string = "Plan de servicios";
  subheader: string = "Nuevo";
  form!: FormGroup;
  nameControl = new FormControl('', [Validators.required, Validators.minLength(3)]);

  constructor(
    private fb: FormBuilder, 
    private modelSVc: ClientPlanService,
    private snackSvc: SnackbarService,
    private dialogSvc: DialogService,
    @Inject(MAT_DIALOG_DATA) public dialogData: any 
  ) {
    this.form = fb.group({
      name: this.nameControl
    });
  }

  ngOnInit(): void {
    let id = this.dialogData['id'];
    if (id){
        this.subheader = "Editar";
        this.modelSVc.getById(id).subscribe(item=>{
          this.form.get('name')?.setValue(item.name);
        })
    }
  }

  onSubmit(event: boolean){
    if (this.form.valid){
      let id = this.dialogData['id'];
      if (id){
        this.modelSVc.update(id, this.form.value).subscribe((res)=>{
          this.snackSvc.openSnackBar("Plan de servicio editado correctamente", 'x');
          this.dialogSvc.close();
        });
      } else {
        this.modelSVc.create(this.form.value).subscribe((res)=>{
          this.snackSvc.openSnackBar("Plan de servicio creado correctamente", 'x');
          this.dialogSvc.close();
        });
      }
    } else {
      this.snackSvc.openSnackBar("Debes completar algunos campos obligatorios", 'x');
    }
  }

  onClearForm(event: boolean){
    this.form.reset();
  }

}
