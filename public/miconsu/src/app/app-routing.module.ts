import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'administrador',
    loadChildren: () =>
    import("./layouts/app-administrator/app-administrator-routing.module").then(
      (m) => m.AppAdministratorRoutingModule
    ),
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
