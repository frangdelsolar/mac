import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientPlanDetailComponent } from './client-plan-detail.component';

describe('ClientPlanDetailComponent', () => {
  let component: ClientPlanDetailComponent;
  let fixture: ComponentFixture<ClientPlanDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientPlanDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientPlanDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
