# Valorant Trade
https://kukuh-cikal-valotrade.pbp.cs.ui.ac.id/

## Deployment Steps
1. Creating a new Django Project
    * Make a new directory, in my case called "valo-trade" as the name of my project. Then a command prompt is needed to execute the installation command. The command prompt (CMD) should be opened in the same directory of the projects. To do so, simply run these command in the CMD. However, in case the directory doesnt change after the command, simply run the disk partition name of the directory path (i.e. `D:`).
        ```bash
        cd "YourDirectoryPath"
        ```
    * Make a virtual environment by running command below in CMD
        ```pyton
        python -m venv env
        ```
    * Activate the virtual environment by following command in CMD
        ```bash
        env\Scripts\activate
        ```
    * Install the required dependencies by putting it inside a requirements.txt file, then simply run
        ```bash
        pip install -r requirements.txt
        ```
    * Create the django project by running the command below in CMD. The project is preferably be named after the same project name as the directory before, as in my case will be "valo_trade"
        ```bash
        django-admin startproject valo_trade .
        ```
2. Pushing the project into GitHub & PWS
    * **Giving access.** To make sure the project can be accessed throughout the local & PWS server, we need to add the http or ip address to the `ALLOWED_HOST` variable inside `settings.py`. This variable indicates list of hosts that is allowed to access the web application. As we want the project to be accessed by localhost & PWS, we will add the following inside the `ALLOWED_HOST`:
        ```python
        ...
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", "kukuh-cikal-valotrade.pbp.cs.ui.ac.id"]
        ...
        ```
    * **Pushing to GitHub.** A git tool must be installed to proceed after this step. Documentation of installation & GitHub setup available [here](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git). Before pushing to GitHub, the project must be defined/initiated as a git repository. To do so, by using the previous CMD, run the command `git init`. Then, create a new GitHub repository & connect it with the local repository by running `git remote add origin <URL_REPO>`. The rest is doing `add`, `commit` & `push` by respectively running `git add .`, `git commit -m "<COMMIT_COMMENT>"`, and `git push -u origin main`. 
    
    * **Pushing to Pacil Web Service (PWS).** A git tool is also needed to proceed this step. First thing first, simply create a new project at PWS. It is highly recommended to mark down the credentials provided by PWS. Then, add the deployment URL to the `ALLOWED_HOST` in `settings.py` file by the format of `<username-sso>-<nama proyek>.pbp.cs.ui.ac.id`. In my case, i named the project as valotrade thus making my deployment URL be `kukuh-cikal-valotrade.pbp.cs.ui.ac.id`. After that, run the commands provided by the PWS inside CMD, including:
        ```bash
        git remote add pws https://pbp.cs.ui.ac.id/kukuh.cikal/valotrade
        git branch -M master
        git push pws master
        ```
3. Creating a new app 'main' into the project
    * This django project is using **Model-View-Template (MVT)** with the documentation available [here](https://www.geeksforgeeks.org/django-project-mvt-structure/). MVT is used as it benefits developer to split their work on App Logic, Interface, and Data.
    * **Creating & adding main app.** a new app `main` can easily be created by running the command `python manage.py startapp main`. Then, adding the `main` app to the `INSTALLED_APPS` list in `settings.py` should be most necessary. Inside the `main` app directory , create a new directory named `templates`. Inside it, create a new file named `main.html` filled by desired code.
    * **Modifying & migrating models.** Inside the `main` directory, open the `models.py` and create a new class inheriting `models.Model`, containing the variable & fields required in the main application. Then, each time the models is modified, make a new migration to the local drive by running `python manage.py makemigrations` and `python manage.py migrate` from the CMD.
    * **Integrating the MVT Components.** Inside the `main` directory, open the `vies.py` and create a new function taking the parameter request `show_main(request)`, containing a dictionary `context` with key & value as a data to be used inside the main models.
    * **Configuring the main URL routing.** Inside the `main` directory, create a new file `urls.py` with the code below. Then, add the URL route to the `urls.py` inside project directory, as in my case `valo_trade`.
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ```
    * **Pushing to Github & PWS.** Do git add, commit, and push to GitHub & pws.

## Django Webservice Diagram
```mermaid
flowchart TD
    Client["Client"] -- Request --> internet["Internet"]
    internet -- Request --> urls.py["urls.py"]
    internet -- Render Web Page --> Client
    urls.py -- Maps to --> views.py["views.py"]
    views.py -- Calls --> models.py["models.py"]
    models.py -- Sends data --> views.py
    views.py -- Passes data --> Template("\HTML")
    Template -- Web Page --> internet
```
When a user is accessing a website, the `client`, usually a web browser, sends a request to the `internet`. This request first passes throught internet, then directed throught Django's routing managed by `urls.py`. `urls.py` is responsible for mapping the request URL to the appropriate function or classe in `views.py`. Once the request is routed to a view, Django’s view logic `view.py` takes over, calling a function in `models.py` to interact with the database. Then, the data is send back and rendered by Template `\HTML`. This HTML content is then sent through the internet again back to the client and displayed by the web page renderer.

## Additional Informations
### Git
This project is developed using git, a software development tool used to track and manage change in the codes, making it easier to revert to previous versions when needed. It also neables collaboration by allowing multiple developers to work on seperate branches and merge their changes into the main project without conflicts. With tools for conflict resolution, Git ensures code integrity while improving the overal efficiency of the development process. The distributed nature of git allows developer to work locally and push changes to online repositories like GitHub.
### Django
Django is considered beginner-friendly because it simplifies web development by providing a high-level, all-in-one framework with built-in tools for common tasks, such as authentication, database management, and URL routing. Beginners may also focus more on building features rather than setting up configurations in Django. Django also follows the Model-View-Template (MVT) architecture, which helps in organizing code efficiently, and has extensive documentation and a supportive community, making it easier for newcomers to learn and develop projects quickly.

### ORM in Django
Django models are called Object-Relationa Mapping (ORM) since they allow developers interact with databases without writing SQL, using python. This happens because ORM automatically translate Python code into SQL, making the database management easier for beginner and more intuitive.

# Contributing
Pull requests are welcome. For major changes or bug reports, especially from `asdos` or `friends`, please open an issue first
to discuss what you would like to change. Cheers -Kukuh