import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-generate-otp',
  templateUrl: './generate-otp.component.html',
  styleUrls: ['./generate-otp.component.css'],
})
export class GenerateOTPComponent {
  @Output() getMail = new EventEmitter<{ mailID: string }>();
  email = '';
  generateOTP() {
    this.getMail.emit({ mailID: this.email });
    console.log(this.email);
  }
  onUpdateEmail(event: Event) {
    this.email = (<HTMLInputElement>event.target).value;
  }
}
