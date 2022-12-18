import { Component, EventEmitter, Output } from '@angular/core';
import { AxiosService } from 'src/services/Axios.service';

@Component({
  selector: 'app-generate-otp',
  templateUrl: './generate-otp.component.html',
  styleUrls: ['./generate-otp.component.css'],
})
export class GenerateOTPComponent {
  @Output() getMail = new EventEmitter<{ mailID: string }>();
  email = '';
  constructor(private axios: AxiosService) {}
  async generateOTP() {
    await this.axios.generateOtpCall(this.email);
    this.getMail.emit({ mailID: this.email });
  }
  onUpdateEmail(event: Event) {
    this.email = (<HTMLInputElement>event.target).value;
  }
}
