This project notifies the person via the email if the International Space Station is passing through their night sky.

*************** IMPORTANT ***************
Changes to make:
1. In config.py file, make sure to provide details associated with your EMAIL Service (Current details are dummy details).
   (Password is the App Password which one can generate from the Account Settings.)

2. In main.py file, change the values of MY_LATITUDE and MY_LONGITUDE to make sure it corresponds to your location. If not done so, then the program will not display the 
   accurate time in your area.

3. Lastly, you can schedule this to run very frequently on a cloud service so you can get emails whenever the ISS is in your night sky.
   Alternatively, one can simply keep it running on their machine.

For the sunset and sunrise times based on the latitude and longitude, credit to SunriseSunset.io for their API.
