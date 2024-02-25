<h1>Welcome to Django Blitzkrieg</h1>
<h2> CURRENT PHASE :: DEVELOPMENT</h2>
<h3> Contents :</h3>

1. Installation
2. Usage

<h4>Installation :-</h4>
To install django_blitzkrieg, <br> 
1. Add 'blitzkrieg_controls' to your INSTALLED_APPS list in settings.py <br>
2. Then you need to separate your applications in USER_APPS in settings.py for which you want to get the generated code. (INSTALLED_APPS += USER_APPS) <br>

<h4>Usage :-</h4>
Use <b>python manage.py blitzkrieg -A </b> to build generated code for all applications in settings.USER_APPS which includes serializers, views, admin <br>
If you want to build the generated code for a specific application in settings.USER_APPS use:- <br>
<b>"python manage.py blitzkrieg --app_label=<your_app_label>" </b>


If you want to build the generated code for a specific model of a specific application in settings.USER_APPS use:- <br>
<b>python manage.py blitzkrieg --model_name=<your_app_label>.<your_model_name></b>
