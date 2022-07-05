import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { DialogService } from '@core/services/dialog.service';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

import { SnackbarService } from '@core/services/snackbar.service';
import { ProfessionalService } from '../professional-controller.service';
import { ClientService } from '@features/client/client-controller.service';
import { PersonService } from '@features/person/person-controller.service';
import { UserService } from '@features/user/user.service';
import { ProfileService } from '@features/profile/profile.service';


@Component({
  selector: 'app-professional-form',
  templateUrl: './professional-form.component.html',
  styleUrls: ['./professional-form.component.scss']
})
export class ProfessionalFormComponent implements OnInit {
  
  header: string = "Profesional";
  subheader: string = "Nuevo";
  form!: FormGroup;

  clientData!: any[];
  profileData!: any[];
  personData!: any[];

  constructor(
    private fb: FormBuilder, 
    private modelSVc: ProfessionalService,
    private clientSvc: ClientService,
    private profileSvc: UserService,
    private personSvc: PersonService,
    private snackSvc: SnackbarService,
    private dialogSvc: DialogService,
    @Inject(MAT_DIALOG_DATA) public dialogData: any 
  ) {
    this.form = fb.group({
      contact_id: new FormControl('', [Validators.required]),
      profile_id: new FormControl('', [Validators.required]),
      client_id: new FormControl('', [Validators.required]),
    });
  }

  ngOnInit(): void {
    let id = this.dialogData['id'];
    if (id){
        this.subheader = "Editar";
        this.modelSVc.getById(id).subscribe(item=>{
          this.form.get('profile_id')?.setValue(item.profile_id);
          this.form.get('contact_id')?.setValue(item.contact_id);
          this.form.get('client_id')?.setValue(item.client_id);
          this.loadClient(item.client_id);
          this.loadProfile(item.profile_id);
          this.loadPerson(item.contact_id);
        })
    } else {
      this.loadClient(null);
      this.loadProfile(null);
      this.loadPerson(null)
    }
  }

  loadClient(id: number | null | undefined){
    if (id){
      this.clientSvc.getById(id).subscribe(res => {
        this.clientData = [res]
      });
    } else {
      this.clientSvc.filter("?limit=99999").subscribe(res => {
        this.clientData = res.results
      });   
    }
  }

  loadProfile(id: number | null | undefined){
    if (id){
      this.profileSvc.getById(id).subscribe(res => {
        this.profileData = [res]
      });
    } else {
      this.profileSvc.filter("?limit=99999").subscribe(res => {
        this.profileData = res.results
      });   
    }
  }

  loadPerson(id: number | null | undefined){
    if (id){
      this.personSvc.getById(id).subscribe(res => {
        this.personData = [res]
      });
    } else {
      this.personSvc.filter("?limit=99999").subscribe(res => {
        this.personData = res.results
      });   
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
