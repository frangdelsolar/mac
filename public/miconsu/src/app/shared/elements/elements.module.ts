import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CardComponent } from './card/card.component';
import { MaterialModule } from '../material.module';
import { RouterModule } from '@angular/router';
import { ListFromObjectComponent } from './list-from-object/list-from-object.component';


const myComponents = [
  CardComponent,
  ListFromObjectComponent
]

@NgModule({
  declarations: [
    ...myComponents,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    RouterModule
  ],
  exports: [
    ...myComponents,
  ]
})
export class ElementsModule { }
