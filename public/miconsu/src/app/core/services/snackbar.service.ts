import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SnackbarService {
    obs = new BehaviorSubject<boolean>(false);

    constructor(private _snackBar: MatSnackBar) {}

    openSnackBar(message: string, action: string|null = null) {
        if (action){
            this._snackBar.open(message, action, {
                duration: 3000
              });
        } else {
            this._snackBar.open(message);
        }
    }

    confirm(message: string){
        let snackRef = this._snackBar.open(message, 'Aceptar', {
            duration: 3000
        });
        snackRef.onAction().subscribe(()=>{
            this.obs.next(true);
        });
        this.obs.next(false);
        return this.obs;
    }
}