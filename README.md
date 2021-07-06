# My-Gallery
## Author
Nicholas Ngetich
*****
This is a personal gallery application that displays photos in grid format. It is built with Django python framework.
*****
### Prerequisites
* Python 3
* Text editor eg Visual Studio Code
* You need to have git installed. You can install it with the following command in your terminal
`$ sudo apt install git-all`
*****
## Setup Instruction
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone $ git clone https://github.com/ngetichnicholas/My-Gallery.git
1. This will clone the repositoty into your local folder
*****
### Admin Site
There is an admin site to manage the application resources like adding photos, updating photos,deleting and managing location and categories
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1625555259/Screenshot_from_2021-07-06_09-14-57_lfqbds.png)
### View Gallery photo items
A user can go to photos page and where all photos available will be displayed. The user can also select to view photos from different locations
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1625552653/Screenshot_from_2021-07-06_09-16-48_lmi3no.png)
*****
### View Photo details and copy URL to clipboard
A user can click on any image and a modal will be displayed containing the photo information like title, description, photo url and date posted.  
The user can also click on the image URL and it will be copied to machine clipboard.
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1625553740/Screenshot_from_2021-07-06_09-41-15_ov93ex.png)
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1625553894/Screenshot_from_2021-07-06_09-44-26_cetgzi.png)
*****
### Search Function
With the search function, a user can search images with keywords hike,selfie,travel,operating,coding and food to filter images by respective categories.
*****
![alt text](https://res.cloudinary.com/dbos9xidr/image/upload/v1625552943/Screenshot_from_2021-07-06_09-27-14_mfnjnc.png)
*****
## Behaviour Driven Development
1. Provides a dropdown button to select location 
   - INPUT: Click on location option
   - OUTPUT: Photos belonging to that particular location displayed in the page
1. Provides a search form
   - INPUT: Category keyword entered in the search field
   - OUTPUT: Photos belonging to that category is displayed in the page
1. Show photo details
   - INPUT: Image is clicked
   - OUTPUT: A model pop up with image details
1. Provides a copy function for image URL
   - INPUT: Photo URL is clicked
   - OUTPUT: The image link copied to machine clipboard

## Dependencies
* django-bootstrap
* Pillow
* psycopg2
* python-decouple
* Python Venv
* whitenoise
* gunicorn
*****
## Technologies Used
* HTML
* Python 3
* JavaScript
* CSS
******
### Live Link
Or you can access the web application directly via this [LIVE LINK](https://nick-gallery.herokuapp.com/).
*****
### License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
*****
### Questions?
Twitter: **[@ngetichnichoh](https://twitter.com/ngetichnichoh)**  
Email: **[nicholas.ngetich@student.moringaschool.com](mailto:nicholas.ngetich@student.moringaschool.com)**