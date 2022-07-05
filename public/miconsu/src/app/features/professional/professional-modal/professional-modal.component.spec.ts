import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfessionalModalComponent } from './professional-modal.component';

describe('ProfessionalModalComponent', () => {
  let component: ProfessionalModalComponent;
  let fixture: ComponentFixture<ProfessionalModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfessionalModalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfessionalModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
