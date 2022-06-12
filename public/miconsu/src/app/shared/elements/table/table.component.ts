import { SelectionModel } from '@angular/cdk/collections';
import { AfterViewInit, ViewChild, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { BehaviorSubject, Observable } from 'rxjs';
import { PageEvent } from '@angular/material/paginator';
import { MatSort, Sort} from '@angular/material/sort';
import { FormControl } from '@angular/forms';
import { PaginatedResponse } from '@core/models/paginated-response.interface';
import { TableService } from './table.service';
import { SnackbarService } from '@core/services/snackbar.service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.scss']
})
export class TableComponent implements OnInit, AfterViewInit {
  
  @Input() tableHeader!: string;
  @Input() tableSubHeader!: string;
  @Input() columns!: any[];

  // Data
  dataSource!: Observable<PaginatedResponse>;
  displayedColumns:string[] = [];
  selection = new SelectionModel<any>(true, []);

  // Paginator
  data!: MatTableDataSource<any>;
  pageEvent!: PageEvent;
  tableLength!: number;

  // Search
  searchControl = new FormControl('', []);

  // State
  editMode = false;
  @Input() showBulkDelete: boolean = true;
  @Input() showDelete: boolean = true;
  @Input() showEdit: boolean = true;
  @Input() showView: boolean = true;
  @Input() showAdd: boolean = true;

  // Actions
  @Output() emitFilter = new EventEmitter<string>();
  @Output() emitView = new EventEmitter<number>();
  @Output() emitCreate = new EventEmitter<number>();
  @Output() emitEdit = new EventEmitter<number>();
  @Output() emitDelete = new EventEmitter<number>();

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  _filters: {[key:string]: string} = {
    'search': '',
    'ordering': '',
    'page': ''
  };

  constructor(
    private service: TableService,
    private snackSvc: SnackbarService,
  ) {
  }

  ngOnInit(): void {
    this.dataSource = this.service.TableDataObservable;
    this.displayedColumns =  this.columns.map(c => c.columnDef);
    if (this.showActions()) this.displayedColumns.push('actions');
    this.loadData();
  }

  ngAfterViewInit() {
    this.data.paginator = this.paginator;
    this.data.sort = this.sort;
  }

  loadData(){
    this.dataSource.subscribe(res=>{
      if (res){
        this.tableLength = res.count;
        this.paginator.pageSize = res.results.length;
        this.paginator.length = res.count;
        this.data = new MatTableDataSource<any>(res.results);
      }
    })
  }

  // Filters And Search
  applyFilters() {
    let params = '';
    for (let key in this._filters){
      if (this._filters[key] !== ''){
        if (params == ''){
          params += `?${key}=${this._filters[key]}`
        } else {
          params += `&${key}=${this._filters[key]}`
        }
      }
    }
    this.emitFilter.next(params);
  }

  searchChanged(){
    this._filters['search'] = this.searchControl.value;
    this.applyFilters();
  }

  announceSortChange(sortState: Sort) {
    this._filters['ordering'] = `${sortState.active}`;
    if (sortState.direction == 'desc'){
      this._filters['ordering'] = `-${sortState.active}`;
    }    
    this.applyFilters();
  }

  pageChanged(event: any){
    this._filters['page'] = event.pageIndex + 1;
    this.applyFilters();
  }


  // Edit Mode
  switchEditMode(){
    if(this.editMode == true){
      this.displayedColumns.splice(this.displayedColumns.indexOf('select'), 1);
      this.editMode = false;
    } else {
      this.displayedColumns.splice(0, 0, 'select')
      this.editMode = true;
    }
  }

  isAllSelected() {
    const numSelected = this.selection.selected.length;
    const numRows = this.data.data.length;
    return numSelected === numRows;
  }

  masterToggle() {
    if (this.isAllSelected()) {
      this.selection.clear();
      return;
    }
    this.selection.select(...this.data.data);
  }

  showActions(){
    return (this.showEdit || this.showDelete || this.showView);
  }


  // Events
  onClickAddItem(){
    this.emitCreate.emit(-1);
  }

  onClickViewItem(id: number){
    this.emitView.emit(id);
  }

  onClickEditItem(id: number){
    this.emitEdit.emit(id);
  }

  onClickDeleteItem(id: number){
    this.snackSvc.confirm('¿Desea eliminar esto?').subscribe(res=>{
      if(res===true){
        this.emitDelete.emit(id);
      }
    })
  }

  bulkDelete(){
    let selection = this.selection.selected;
    if(selection.length){
      this.snackSvc.confirm(`Esta acción es irreversible, ¿de verdad querés eliminar ${selection.length} registros?`).subscribe(res=>{
        console.log(res)
        if (res === true){
          for (let item of selection){
            this.emitDelete.emit(item.id);
          }   
        }
      })
    } 
  }

}
