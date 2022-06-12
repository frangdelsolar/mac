import { SelectionModel } from '@angular/cdk/collections';
import { AfterViewInit, ViewChild, Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { BehaviorSubject, Observable } from 'rxjs';
import { PageEvent } from '@angular/material/paginator';
import { MatSort, Sort} from '@angular/material/sort';
import { FormControl } from '@angular/forms';
import { PaginatedResponse } from '@core/models/paginated-response.interface';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.scss']
})
export class TableComponent implements OnInit, AfterViewInit {
  
  @Input() tableHeader!: string;
  @Input() tableSubHeader!: string;
  @Input() baseUrl!: string;
  @Input() service!: any;

  //Actions
  @Input() showBulkDelete: boolean = false;
  @Input() showDelete: boolean = false;
  @Input() showEdit: boolean = false;
  @Input() showView: boolean = false;
  @Input() showAdd: boolean = false;

  // Data
  @Input() columns!: any[];
  @Input() dataSource!: Observable<PaginatedResponse>;
  @Input() refresh!: BehaviorSubject<boolean>; // Delete
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

  // Actions
  @Output() emitCreate = new EventEmitter<number>();
  @Output() emitEdit = new EventEmitter<number>();
  @Output() emitDelete = new EventEmitter<number>();

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;


  constructor(
    private router: Router,
    ) {}


  ngAfterViewInit() {
    this.data.paginator = this.paginator;
    this.data.sort = this.sort;
  }

  ngOnInit(): void {
    this.displayedColumns =  this.columns.map(c => c.columnDef);
    if (this.showActions()) this.displayedColumns.push('actions');
    this.refreshData();

  }

  refreshData(){
    this.dataSource.subscribe(res=>{
      this.data = new MatTableDataSource<any>(res.results);
      this.tableLength = res.count;
      this.data.paginator = this.paginator;
    })
  }

  applySearch() {
    let search = this.searchControl.value;
    let params = `?search=${search}`
    this.service.getAll(params).subscribe( (res: any) => {
      this.data = new MatTableDataSource<any>(res.results);
      this.tableLength = res.count;
      this.data.paginator = this.paginator;
    })
  }

  announceSortChange(sortState: Sort) {
    let params = `?ordering=${sortState.active}`;
    if (sortState.direction == 'desc'){
      params = `?ordering=-${sortState.active}`
    }

    let search = this.searchControl.value;
    if (search) params += `&search=${search}`;

    let limit = this.data.paginator?.pageSize;
    if (limit) params += `&limit=${limit}`
    
    this.service.getAll(params).subscribe( (res: any) => {
      this.data = new MatTableDataSource<any>(res.results);
      this.tableLength = res.count;
      this.data.paginator = this.paginator;
    })
  }

  pageChanged(event: any){
    let limit = event.pageSize;
    let offset = event.pageSize * event.pageIndex;
    let params = `?limit=${limit}&offset=${offset}`

    let search = this.searchControl.value;
    if (search) params += `&search=${search}`;

    let order = this.sort.active;
    if (order) {
      if (this.sort.direction == "asc") params += `&ordering=${order}`;
      if (this.sort.direction == "desc") params += `&ordering=-${order}`;
    }

    this.service.getAll(params).subscribe( (res: any) => {
      this.data = new MatTableDataSource<any>(res.results);
    })
  }

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

  addItem(){
    // this.router.navigate([this.baseUrl, 'nuevo'], { });
    this.emitCreate.emit(-1);
  }

  viewItem(id: number){
    this.router.navigate([this.baseUrl, id], { })
  }

  editItem(id: number){
    // let url = this.baseUrl + "/editar"
    // this.router.navigate([url, id], { })
    this.emitEdit.emit(id);
  }

  deleteItem(id: number){
    if (confirm("Esta acción es irreversible, ¿de verdad querés eliminar esto?")){
      this.emitDelete.emit(id);
    }
  }

  bulkDelete(){
    let selection = this.selection.selected;
    if(selection.length > 0 && confirm(`Esta acción es irreversible, ¿de verdad querés eliminar ${selection.length} registros?`)){
      for (let item of selection){
        this.emitDelete.emit(item.id);
      }
    }
  }

}
