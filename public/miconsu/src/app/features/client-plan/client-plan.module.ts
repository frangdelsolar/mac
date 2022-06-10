import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientPlanFormComponent } from './client-plan-form/client-plan-form.component';
import { ClientPlanListComponent } from './client-plan-list/client-plan-list.component';
import { ClientPlanDetailComponent } from './client-plan-detail/client-plan-detail.component';
import { SharedModule } from '@shared/shared.module';

const myComponents = [
  ClientPlanDetailComponent,
  ClientPlanListComponent,
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
