import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CrudComponent } from './crud/crud.component';
import { SharedModule } from '@shared/shared.module';


@NgModule({
  declarations: [
    CrudComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
  ]
})
export class AppAdministratorModule { }
