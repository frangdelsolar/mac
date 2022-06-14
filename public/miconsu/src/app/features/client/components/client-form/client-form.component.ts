import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { DialogService } from '@core/services/dialog.service';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

import { SnackbarService } from '@core/services/snackbar.service';
import { ClientService } from '@features/client/client-controller.service';
import { User } from '@features/user/user.interface';
import { ClientPlan } from '@features/client-plan/client-plan.interface';
import { ClientType } from '@features/client-type/client-type.interface';
import { ClientPlanService } from '@features/client-plan/client-plan-controller.service';
import { ClientTypeService } from '@features/client-type/client-type-controller.service';


@Component({
  selector: 'app-client-form',
  templateUrl: './client-form.component.html',
  styleUrls: ['./client-form.component.scss']
})
export class ClientFormComponent implements OnInit {
  
  header: string = "Cliente";
  subheader: string = "Nuevo";
  form!: FormGroup;
  nameControl = new FormControl('', [Validators.required, Validators.minLength(3)]);
  administratorControl = new FormControl('', []);
  clientPlanControl = new FormControl('', [Validators.required]);
  clientTypeControl = new FormControl('', [Validators.required]);

  userData!: User[];
  clientPlanData!: ClientPlan[];
  clientTypeData!: ClientType[];

  constructor(
    private fb: FormBuilder, 
    private modelSVc: ClientService,
    private clientPlanSvc: ClientPlanService,
    private clientTypeSvc: ClientTypeService,
    private snackSvc: SnackbarService,
    private dialogSvc: DialogService,
    @Inject(MAT_DIALOG_DATA) public dialogData: any 
  ) {
    this.form = fb.group({
      name: this.nameControl,
      administrator_id: this.administratorControl,
      client_plan_id: this.clientPlanControl,
      client_type_id: this.clientTypeControl,
    });
  }

  ngOnInit(): void {
    let id = this.dialogData['id'];
    if (id){
        this.subheader = "Editar";
        this.modelSVc.getById(id).subscribe(item=>{
          this.form.get('name')?.setValue(item.name);
          this.form.get('administrator_id')?.setValue(item.administrator?.id);
          this.form.get('client_plan_id')?.setValue(item.client_plan?.id);
          this.form.get('client_type_id')?.setValue(item.client_type?.id);
          this.form.get('administrator_id')?.disable();
          this.form.get('client_plan_id')?.disable();
          this.form.get('client_type_id')?.disable();
          this.loadClientPlans(item.client_plan?.id);
          this.loadClientTypes(item.client_type?.id);
          this.loadUsers(item.administrator?.id);
        })
    } else {
      this.loadUsers(null);
      this.loadClientPlans(null);
      this.loadClientTypes(null);  
    }
  }

  loadClientPlans(id: number | null | undefined){
    if (id){
      this.clientPlanSvc.getById(id).subscribe(res => {
        this.clientPlanData = [res]
      });
    } else {
      this.clientPlanSvc.filter("?limit=99999").subscribe(res => {
        this.clientPlanData = res.results
      });   
    }
  }

  loadClientTypes(id: number | null | undefined){
    if (id){
      this.clientTypeSvc.getById(id).subscribe(res => {
        this.clientTypeData = [res]
      });
    } else {
      this.clientTypeSvc.filter("?limit=99999").subscribe(res => {
        this.clientTypeData = res.results
      });   
    }
  }

  loadUsers(id: number | null | undefined){
    // if (id){
    //   this.clientTypeSvc.getById(id).subscribe(res => {
    //     this.clientTypeData = [res]
    //   });
    // } else {
    //   this.clientTypeSvc.filter("?limit=99999").subscribe(res => {
    //     this.clientTypeData = res.results
    //   });   
    // }
  }

  onSubmit(event: boolean){
    if (this.form.valid){
      let id = this.dialogData['id'];
      if (id){
        this.modelSVc.update(id, this.form.value).subscribe(
          (res)=>{
            this.snackSvc.openSnackBar("Plan de servicio editado correctamente", 'x');
            this.dialogSvc.close();
          }
        );
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
