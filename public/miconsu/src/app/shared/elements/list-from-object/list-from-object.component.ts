import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-list-from-object',
  templateUrl: './list-from-object.component.html',
  styleUrls: ['./list-from-object.component.scss']
})
export class ListFromObjectComponent implements OnInit {

  @Input() object!: any;
  @Input() labels: any;
  items: any[] = [];

  constructor() { }

  ngOnInit(): void {
  }

  ngOnChanges() {
    if(this.object) {
      for (let key in this.object){
        this.items.push({'key': this.labels[key], 'value': this.object[key]})
      }
    }
  }

}
