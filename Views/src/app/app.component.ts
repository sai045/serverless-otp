import { Component } from '@angular/core';
import { AxiosService } from 'src/services/Axios.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'OTP System';
  email = '';
  OTP = '';
  pageName = 'generateOTP';

  constructor(private axios: AxiosService) {
    window.onload = () => {
      localStorage.removeItem('isVerified');
    };
  }

  getEmail(generateData: { mailID: string }) {
    this.email = generateData.mailID;
    if (localStorage.getItem('isVerified') == 'Verified') {
      this.pageName = 'home';
    } else {
      this.pageName = 'verifyOTP';
    }
  }
  getOTP(verifyData: { OTP: string }) {
    this.OTP = verifyData.OTP;
    this.axios.verifyOtpCall(this.email, this.OTP);
    if (localStorage.getItem('isVerified') == 'Verified') {
      this.pageName = 'home';
    }
  }
}
