import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListFromObjectComponent } from './list-from-object.component';

describe('ListFromObjectComponent', () => {
  let component: ListFromObjectComponent;
  let fixture: ComponentFixture<ListFromObjectComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListFromObjectComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListFromObjectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
