import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from './card/card.component';
import { MaterialModule } from '../material.module';
import { RouterModule } from '@angular/router';
import { ListFromObjectComponent } from './list-from-object/list-from-object.component';
import { TableComponent } from './table/table.component';
import { ReactiveFormsModule } from '@angular/forms';


const myComponents = [
  CardComponent,
  ListFromObjectComponent,
  TableComponent,

]

@NgModule({
  declarations: [
    ...myComponents,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    ReactiveFormsModule,
    RouterModule
  ],
  exports: [
    ...myComponents,
  ]
})
export class ElementsModule { }
