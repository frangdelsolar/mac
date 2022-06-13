import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientPlanModalComponent } from './client-plan-modal.component';

describe('ClientPlanModalComponent', () => {
  let component: ClientPlanModalComponent;
  let fixture: ComponentFixture<ClientPlanModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientPlanModalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientPlanModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
