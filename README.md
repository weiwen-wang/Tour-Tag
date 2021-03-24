# Tour-Tag
## Runserver
open terminal and find the file in your computer, for example:
```
 cd /home/download/Tour_Tag_version1/
```
then run the server
```
 python manage.py runserver
```
It will show:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
If fail, you may need to install related module like crispy... check its error to install them

## File details
There are two files in file "app", "tour" and "user", They have different function:
### Tour
Tour has differents functions.
In file ```urls.py```, you can see different path:
```
path('index/', views.IndexView.as_view(), name='index'),
path('guide/', views.GuideView.as_view(), name='guide'),
path('driver/', views.DriverView.as_view(), name='driver', kwargs={'pk': 1}),
path('guide/turn_on/',views.turn_on),
path('guide/turn_off/',views.turn_off),
path('guide/refresh/',views.refresh),
```
They are subpath of tour, in other work, if you want to run them, you need to add ```tour``` in front of them. For example, if you want to go to tour page, the path
is: 
```
127.0.0.1:8000/tour/guide/
```
Differnt function can be seen in ```view.py``` and ```model.py```
In ```models.py```:
```PORT_STATUS``` refers to the 8 ports to choose in a Drop down box. ```Guide``` is the trip information input by tour guides, including name, start and end ports.
```Boot``` refers to the boat status like "driving" or "stopping" in which port. ```voyage``` stores the "departure time"
If you want to add information, you can add freely, but remenber to migrate 
Write the code in terminal:
```
python manage.py makemigrations tour
```
And choose 1 to write the missing data
Then:
```
python manage.py migrate
```
After success, run the server again:
```
python manage.py runserver
```

### User
The function of user is log in, it connect to the database to store the user information. Only the users in database hasve the permission to use this web software. 
Now the valid users are:
```
Username     Password
admin        admin123...
Guide01      team71234
Driver01     team71234
```

### Control of Raspberry Pi 
The code for control Raspberry Pi is in ```view.py```
There are three functions ```turn_on```, ```turn_off```, and ```refresh```.


### template
The user interface design is in template ```.html``` files
