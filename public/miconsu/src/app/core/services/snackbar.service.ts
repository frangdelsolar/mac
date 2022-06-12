import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root',
})
export class SnackbarService {
    constructor(private _snackBar: MatSnackBar) {}

    openSnackBar(message: string, action: string|null = null) {
        if (action){
            this._snackBar.open(message, action);
        } else {
            this._snackBar.open(message);
        }
    }
}