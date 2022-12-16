import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'OTP System';
  email = '';
  OTP = '';

  getEmail(generateData: { mailID: string }) {
    this.email = generateData.mailID ;
    console.log(generateData)
  } 
  getOTP(verifyData: { OTP:string }) {
    this.OTP = verifyData.OTP ;
    console.log(verifyData)
  } 
}
