import { Component, OnInit } from '@angular/core';
import { ClientPlanService } from '../client-plan-controller.service';
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

  object!: ClientPlan;
  labels = clientPlanEnum;
  constructor(private service: ClientPlanService) { }

  ngOnInit(): void {
    this.service.getById(4).subscribe(item=>{
      this.object=item

    })
  }

}
