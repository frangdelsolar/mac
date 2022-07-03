import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CrudComponent } from './crud/crud.component';
import { SharedModule } from '@shared/shared.module';
import { RegisterClientComponent } from './register-client/register-client.component';


@NgModule({
  declarations: [
    CrudComponent,
    RegisterClientComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
  ]
})
export class AppAdministratorModule { }
