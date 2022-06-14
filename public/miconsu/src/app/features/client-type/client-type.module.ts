import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ClientTypeFormComponent } from './client-type-form/client-type-form.component';
import { ClientTypeListComponent } from './client-type-list/client-type-list.component';
import { ClientTypeDetailComponent } from './client-type-detail/client-type-detail.component';
import { SharedModule } from '@shared/shared.module';
import { ClientTypeModalComponent } from './client-type-modal/client-type-modal.component';

const myComponents = [
  ClientTypeDetailComponent,
  ClientTypeListComponent,
  ClientTypeModalComponent,
  ClientTypeFormComponent
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
export class ClientTypeModule { }
