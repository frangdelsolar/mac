import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientTypeModalComponent } from './client-type-modal.component';

describe('ClientTypeModalComponent', () => {
  let component: ClientTypeModalComponent;
  let fixture: ComponentFixture<ClientTypeModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClientTypeModalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClientTypeModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
