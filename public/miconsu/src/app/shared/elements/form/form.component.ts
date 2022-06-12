import { Component, Input, OnInit, Output, EventEmitter, Inject } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { DialogService } from '@core/services/dialog.service';


@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.scss']
})
export class FormComponent implements OnInit {
  @Input() header!: string;
  @Input() subheader!: string;
  btnLabel: string = "Guardar";

  @Input() showCard: boolean = true;
  @Input() showClearButton: boolean = true;
  @Input() showCancelButton: boolean = true;
  @Input() showSubmitButton: boolean = true;

  @Output() submitEmitter = new EventEmitter<boolean>();
  @Output() clearEmitter = new EventEmitter<boolean>();
  
  data!: any;

  constructor(
    private dialogSvc: DialogService,
   
  ) {
  }

  ngOnInit(): void {
  }

  formIsValid(){
  }


  onSubmit(): void {
    this.submitEmitter.next(true);
  }

  clearForm(){
    this.clearEmitter.next(true);
  }

  cancel(){
    this.dialogSvc.close();
  }
}
