# **ISS overhead e-mail notifyer**
___
> It automaticly sends an email with notification when ISS is close to set location:
<br>
<a>The app uses API requests and respones to get ISS current coordinates and to get info about the sunrise and sunset in a location set by the user. And with the smtplib sends an email. </a>
<br>
<br>
<a> When the ISS longitude and latitude are close to the ones set by the user the code sends an email with smtplib module. </a>
<ul>
  <li>The user myst set their location using global variables MY_LAT and MY_LONG</li>
  <li>The user must set their email and app password as global variables MY_EMAIL, MY_PASSWORD. Take note that the password is diferent from the email account password. You need to create an app password here's a tip https://support.google.com/accounts/answer/185833?hl=en</li>
  
