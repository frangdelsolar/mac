import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProfessionalFormComponent } from './professional-form/professional-form.component';
import { ProfessionalListComponent } from './professional-list/professional-list.component';
import { ProfessionalDetailComponent } from './professional-detail/professional-detail.component';
import { SharedModule } from '@shared/shared.module';
import { ProfessionalModalComponent } from './professional-modal/professional-modal.component';

const myComponents = [
  ProfessionalDetailComponent,
  ProfessionalListComponent,
  ProfessionalModalComponent,
  ProfessionalFormComponent
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
export class ProfessionalModule { }
