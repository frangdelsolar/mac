import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientModule } from './client/client.module';


const myModules = [
  ClientModule,
]


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    ...myModules
  ],
  exports: [
    ...myModules
  ]
})
export class FeaturesModule { }
