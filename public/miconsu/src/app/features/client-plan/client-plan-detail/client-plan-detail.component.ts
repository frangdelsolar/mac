import { Component, OnInit } from '@angular/core';
import { clientPlanEnum } from '../client-plan.enum';
import { ClientPlan } from '../client-plan.interface';

@Component({
  selector: 'app-client-plan-detail',
  templateUrl: './client-plan-detail.component.html',
  styleUrls: ['./client-plan-detail.component.scss']
})
export class ClientPlanDetailComponent implements OnInit {
  header: string = "Plan de Servicios";
  subheader: string = "Detalle";

  object: ClientPlan = {
    id: 1,
    name: 'Plan Eterno',
  }
  labels = clientPlanEnum;
  constructor() { }

  ngOnInit(): void {
  }

}
