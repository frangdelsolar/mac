import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})
export class CardComponent implements OnInit {
  @Input() header!: string;
  @Input() subheader!: string | null;
  @Input() body!: string;
  @Input() link!: string;

  constructor() { }

  ngOnInit(): void {
  }

}
