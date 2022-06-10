import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientModule } from './client/client.module';
import { ClientPlanModule } from './client-plan/client-plan.module';


const myModules = [
  ClientModule,
  ClientPlanModule
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
