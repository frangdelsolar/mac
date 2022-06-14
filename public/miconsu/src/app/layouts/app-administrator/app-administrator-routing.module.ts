import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { CrudComponent } from './crud/crud.component';
import { ClientPlanListComponent } from '@features/client-plan/client-plan-list/client-plan-list.component';
import { ClientTypeListComponent } from '@features/client-type/client-type-list/client-type-list.component';
import { ClientListComponent } from '@features/client/components/client-list/client-list.component';

const routes: Routes = [
  {
    path: "",
    component: CrudComponent,
    children: [
      {
        path: "cliente",
        component: ClientListComponent
      },
      {
        path: "plan",
        component: ClientPlanListComponent
      },
      {
        path: "tipo-de-cliente",
        component: ClientTypeListComponent
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
