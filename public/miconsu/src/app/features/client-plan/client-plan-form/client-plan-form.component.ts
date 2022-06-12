import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ClientPlanService } from '../client-plan-controller.service';


@Component({
  selector: 'app-client-plan-form',
  templateUrl: './client-plan-form.component.html',
  styleUrls: ['./client-plan-form.component.scss']
})
export class ClientPlanFormComponent implements OnInit {
  
  header: string = "Plan de servicios";
  form!: FormGroup;
  nameControl = new FormControl('', [Validators.required, Validators.minLength(3)]);

  constructor(
    private fb: FormBuilder, 
    private service: ClientPlanService
  ) {
    this.form = fb.group({
      name: this.nameControl
    });
  }

  ngOnInit(): void {

  }

  onSubmit(event: boolean){
    if (this.form.valid){
      this.service.create(this.form.value).subscribe((res)=>{
        alert(res);
      });
    }
  }

  onClearForm(event: boolean){
    this.form.reset();
  }

}
