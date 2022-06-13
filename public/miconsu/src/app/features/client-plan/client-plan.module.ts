import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientPlanFormComponent } from './client-plan-form/client-plan-form.component';
import { ClientPlanListComponent } from './client-plan-list/client-plan-list.component';
import { ClientPlanDetailComponent } from './client-plan-detail/client-plan-detail.component';
import { SharedModule } from '@shared/shared.module';
import { ClientPlanModalComponent } from './client-plan-modal/client-plan-modal.component';

const myComponents = [
  ClientPlanDetailComponent,
  ClientPlanListComponent,
  ClientPlanModalComponent,
  ClientPlanFormComponent
]

@NgModule({
  declarations: [
    ...myComponents,
  ],
  imports: [
    CommonModule,
    SharedModule
  ],
  exports: [
    ...myComponents,
  ],
})
export class ClientPlanModule { }
