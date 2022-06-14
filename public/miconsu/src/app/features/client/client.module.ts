import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from '@shared/shared.module';
import { ClientDetailComponent } from './components/client-detail/client-detail.component';
import { ClientFormComponent } from './components/client-form/client-form.component';
import { ClientListComponent } from './components/client-list/client-list.component';
import { ClientModalComponent } from './components/client-modal/client-modal.component';


const myComponents = [
  ClientDetailComponent,
  ClientFormComponent,
  ClientListComponent,
  ClientModalComponent
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
