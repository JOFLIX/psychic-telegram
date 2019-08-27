# django-gallery
A gallery that displays images and one of my favorite images.
### Description
This application allows users to view images according to their categories,location, view details of the image and the description of the album. This app also provides the date on which the image was uploaded. The admin is responsible for uploading, editing and deleting images. The users can search for images according to their categories or the album or tag name.

##screenshots


### BDD Specifications Table
|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| View all images                          |  Click on show more                       |    All images will be displayed          |
| Search for an image                      | Input the category name in the search bar | All images in that category will display |
| View the image details                   | Click on the image                        | All the image details will be displayed  |
| Share image                              | Click on the share link button            | The image link is shared                 |
|View magnified image size                 | Click on the image                        |  A large image is displayed with the     |
                                           |                                           |     share buttons and extra magnify icon |
### Setup/Installation Requirements
<ul>
<li>Ensure you have Python3.6.x installed</li>
<li>Clone the Pixels directory</li>
<li>Create your own virtual environment and activate it using these respective commands:python3.6 -m venv --without-pip virtual && source virtual/bin/activate</li>
<li>Install all the necessary dependencies necessarry for running the application using this command: pip install-r requirements.txt</li>
<li>Create a database: psql then create the databse using this command: CREATE DATABASE gallery</li>
<li>Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate</li>
<li>Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser</li>
</ul>

### Technologies Used
<ul>
<li>Python 3.6</li>
<li>Django</li>
<li>Django-Material</li>
<li>Gallery Extensions</li>
<li>HTML</li>
</ul>
### Known Bugs
After deployment, the following bugs were realised and I am working to resolve them:
The carousel at the legend doe not display,
Search functionality is not properly funcioning
### Support and Contact Details
Email : joflixooko@outlook.com

### Licence
Copyright(c) 2019  Joflix Ooko (MIT)
