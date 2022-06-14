import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientTypeDetailComponent } from './client-type-detail.component';

describe('ClientTypeDetailComponent', () => {
  let component: ClientTypeDetailComponent;
  let fixture: ComponentFixture<ClientTypeDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientTypeDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientTypeDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
