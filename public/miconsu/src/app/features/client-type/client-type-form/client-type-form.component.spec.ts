import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientTypeFormComponent } from './client-type-form.component';

describe('ClientTypeFormComponent', () => {
  let component: ClientTypeFormComponent;
  let fixture: ComponentFixture<ClientTypeFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientTypeFormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientTypeFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
