import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { ClientPlanService } from '@features/client-plan/client-plan-controller.service';
import { ClientTypeService } from '@features/client-type/client-type-controller.service';

@Component({
  selector: 'app-register-client',
  templateUrl: './register-client.component.html',
  styleUrls: ['./register-client.component.scss'],
})
export class RegisterClientComponent implements OnInit {
  header = 'Alta Cliente';
  subheader = '';

  stepOneForm: any;
  stepTwoForm: any;
  stepThreeForm: any;

  clientTypeData: any;
  clientPlanData: any;

  constructor(
    private fb: FormBuilder,
    private clientTypeSvc: ClientTypeService,
    private clientPlanSvc: ClientPlanService
  ) {
    this.stepOneForm = fb.group({
      client_type_id: new FormControl('', [Validators.required]),
      client_plan_id: new FormControl('', [Validators.required]),
    });

    this.stepTwoForm = fb.group({
      first_name: new FormControl('', [
        Validators.required,
        Validators.minLength(3),
      ]),
      last_name: new FormControl('', [
        Validators.required,
        Validators.minLength(3),
      ]),
      username: new FormControl('', [
        Validators.required,
        Validators.minLength(3),
      ]),
      email: new FormControl('', [Validators.required, Validators.email]),
    });

    this.stepThreeForm = fb.group({
      client_type_id: new FormControl('', [Validators.required]),
      client_plan_id: new FormControl('', [Validators.required]),
    });
  }

  ngOnInit(): void {
    this.clientTypeSvc
      .getAll()
      .subscribe((res) => (this.clientTypeData = res.results));

    this.clientPlanSvc
      .getAll()
      .subscribe((res) => (this.clientPlanData = res.results));
  }

  onClientTypeSelection() {
    console.log(this.stepOneForm.value['client_plan_id']);
  }
}
