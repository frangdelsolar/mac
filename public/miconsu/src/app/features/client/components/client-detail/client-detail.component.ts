import { Component, OnInit } from '@angular/core';
import { clientEnum } from '@features/client/client.enum';
import { Client } from '@features/client/client.interface';

@Component({
  selector: 'app-client-detail',
  templateUrl: './client-detail.component.html',
  styleUrls: ['./client-detail.component.scss']
})
export class ClientDetailComponent implements OnInit {

  header: string = "Cliente";
  subheader: string = "Detalle";

  client: Client = {
    id: 1,
    name: 'Pepe',
    administrator: "Francisco Javier",
    client_plan: "Plan Eterno",
    client_type: "Profesional"
  }
  labels = clientEnum;
  constructor() { }

  ngOnInit(): void {
  }

}
