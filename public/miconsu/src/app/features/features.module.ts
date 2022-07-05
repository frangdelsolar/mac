import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientModule } from './client/client.module';
import { ClientPlanModule } from './client-plan/client-plan.module';
import { ClientTypeModule } from './client-type/client-type.module';
import { ProfessionalModule } from './professional/professional.module';
import { SharedModule } from '@shared/shared.module';


const myModules = [
  // ClientModule,
  ClientPlanModule,
  ClientTypeModule,
  // ProfessionalModule,
  // SharedModule
]


@NgModule({
  declarations: [

  ],
  imports: [
    CommonModule,
    ...myModules
  ],
  exports: [
    ...myModules
  ]
})
export class FeaturesModule { }
