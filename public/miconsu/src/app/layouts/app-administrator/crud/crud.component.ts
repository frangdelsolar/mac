import { Component, OnInit } from '@angular/core';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { RegisterClientComponent } from '../register-client/register-client.component';

@Component({
  selector: 'app-crud',
  templateUrl: './crud.component.html',
  styleUrls: ['./crud.component.scss']
})
export class CrudComponent implements OnInit {

  sections = [
    { 
      "title": "Usuarios",
      "description": "Listado de usuarios registrados.",
      "link": "usuario/",
    },
    { 
      "title": "Clientes",
      "description": "Estos son los clientes registrados en el sistema.",
      "link": "cliente/",
    },
    { 
      "title": "Tipos de clientes",
      "description": "Los tipos de clientes existentes.",
      "link": "tipo-de-cliente/",
    },
    { 
      "title": "Servicios Organizacionales",
      "description": "Habilitados en el sistema.",
      "link": "servicio-organizacion/",
    },
    { 
      "title": "Planes",
      "description": "Planes de servicio ofrecidos a los clientes.",
      "link": "plan/",
    },
    { 
      "title": "Profesionales",
      "description": "Estos son los profesionales dados de alta.",
      "link": "profesional/",
    },
  ]

  constructor(
    private dialogSvc: DialogService,
  ) { }

  ngOnInit(): void {
  }

  onRegisterClientClick(){
    let dialogData: DialogData = {
      component: RegisterClientComponent,
      params: {}
    }
    this.dialogSvc.show(dialogData);
    this.dialogSvc.hasClosedObservable.subscribe(res=>{
      if(res){
        this.ngOnInit();
      }
    })

  }
}
