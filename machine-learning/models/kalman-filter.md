- [wiki](https://en.wikipedia.org/wiki/Kalman_filter)
- transition model:
  - $x_k=F_kx_{k-1}+B_ku_k+w_k$
    - transition + control + noise
  - $z_k=H_kx_k+v_k$
    - observation + noise
- updated state estimate
  - $\hat x_{k|k}=(I-K_kH_k)\hat x_{k|k-1}+K_kz_k$
    - 联想“插值”，high error in the sensor是只看$\hat x_{k|k-1}$（“惯性导航”），反之只看$z_k$（observation）