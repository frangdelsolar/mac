import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DialogData } from '@core/models/dialog.interface';
import { DialogService } from '@core/services/dialog.service';
import { Observable } from 'rxjs';
import { CardComponent } from '../card/card.component';

@Component({
  selector: 'app-dialog',
  templateUrl: './dialog.component.html',
  styleUrls: ['./dialog.component.scss']
})
export class DialogComponent implements OnInit {

  public show$: Observable<boolean>;
  public data$: Observable<DialogData>;
  private data!: DialogData;

  template: any = CardComponent;

  constructor(
      public dialog: MatDialog,
      private dialogSvc: DialogService
    ) {
        this.show$ = this.dialogSvc.DialogShowObservable;
        this.data$ = this.dialogSvc.DialogDataObservable;

        this.data$.subscribe(data=>{
          this.data = data;
        })
     }

  ngOnInit(): void {
    this.show$.subscribe( resp => { 
      resp ? this.openDialog(): this.dialog.closeAll(); 
    } )
  }


  openDialog() {
    let data = { 
      width: '50vw',
      data: this.data.params 
    };
    let dialogRef = this.dialog.open(this.data.component, data )
    
    dialogRef.afterClosed().subscribe(result => {
      // console.log({result})
    });
  }

}
