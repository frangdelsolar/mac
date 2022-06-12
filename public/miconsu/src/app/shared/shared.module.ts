import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ElementsModule } from './elements/elements.module';
import { MaterialModule } from './material.module';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

const myModules = [
  ElementsModule,
  MaterialModule,
  ReactiveFormsModule,
  RouterModule,

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
export class SharedModule { }
