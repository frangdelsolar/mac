import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientDetailComponent } from './components/client-detail/client-detail.component';
import { ClientFormComponent } from './components/client-form/client-form.component';
import { SharedModule } from '@shared/shared.module';


const myComponents = [
  ClientDetailComponent,
  ClientFormComponent
]

@NgModule({
  declarations: [
    ...myComponents
  ],
  imports: [
    CommonModule, 
    SharedModule
  ],
  exports: [
    ...myComponents
  ]
})
export class ClientModule { }
