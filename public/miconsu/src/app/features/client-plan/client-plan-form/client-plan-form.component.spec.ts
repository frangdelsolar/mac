import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientPlanFormComponent } from './client-plan-form.component';

describe('ClientPlanFormComponent', () => {
  let component: ClientPlanFormComponent;
  let fixture: ComponentFixture<ClientPlanFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientPlanFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientPlanFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
