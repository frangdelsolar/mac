import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientPlanListComponent } from './client-plan-list.component';

describe('ClientPlanListComponent', () => {
  let component: ClientPlanListComponent;
  let fixture: ComponentFixture<ClientPlanListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientPlanListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientPlanListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
