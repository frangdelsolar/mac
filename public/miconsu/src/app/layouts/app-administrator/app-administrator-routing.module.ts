import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { CrudComponent } from './crud/crud.component';
import { ClientPlanListComponent } from '@features/client-plan/client-plan-list/client-plan-list.component';

const routes: Routes = [
  {
    path: "",
    component: CrudComponent,
    children: [
      {
        path: "plan",
        component: ClientPlanListComponent
      },
    ]
  },

];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ]
})
export class AppAdministratorRoutingModule { }
