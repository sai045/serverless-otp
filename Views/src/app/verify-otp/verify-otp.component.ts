import { Component, EventEmitter, Output, Input } from '@angular/core';

@Component({
  selector: 'app-verify-otp',
  templateUrl: './verify-otp.component.html',
  styleUrls: ['./verify-otp.component.css'],
})
export class VerifyOTPComponent {
  @Output() getOtp = new EventEmitter<{ OTP: string }>();
  OTP = '';
  verifyOTP() {
    this.getOtp.emit({ OTP: this.OTP });
  }
  onUpdateOTP(event: Event) {
    this.OTP = (<HTMLInputElement>event.target).value;
  }
}
