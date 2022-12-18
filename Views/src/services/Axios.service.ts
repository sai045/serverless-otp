import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class AxiosService {
  generateOtpCall(email: string) {
    return axios
      .get(
        'https://yyd04osgpj.execute-api.ap-south-1.amazonaws.com/dev/generateotp?MailID=' +
          email
      )
      .then((res) => console.log(res))
      .catch((err) => {
        console.log(err);
      });
  }
  verifyOtpCall(email: string, OTP: string) {
    return axios
      .get(
        'https://yyd04osgpj.execute-api.ap-south-1.amazonaws.com/dev//verifyotp?MailID=' +
          email +
          '&OTPFromUser=' +
          OTP
      )
      .then((res) => {
        localStorage.setItem('isVerified', res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }
}
