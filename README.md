
# HomeSolutions


![Logo](https://socialify.git.ci/arjyo851/HomeSolutions/image?font=Raleway&language=1&name=1&owner=1&pattern=Charlie%20Brown&theme=Dark)



Welcome to the Real Estate Manager! This application allows you to conveniently manage your real estate needs. You can register, login, buy properties, search for properties, and explore information about sellers.

## Features

- User Registration: Users can create an account to access the application.
- User Login: Registered users can securely log in to their accounts.
- Property Listing: View a list of available properties for sale or on rent.
- Property Details: Get detailed information about each property, including price, location, description, and images.
- Property Search: Search for properties based on specific criteria such as location, price range, or property type.
- Purchase Property: Registered users can buy properties directly through the application.
- Seller Information: Access details about the sellers, including their contact information and ratings.
- User Profile: Manage your profile, update personal information, and view purchase history.

## Demo / Screenshots


### 1. Home Page

When you first open the application, you will see the home page where you can see the search options and default search results just below. You will see two menu icons (One at right top and another at left top).

![HomeSolutions-Home](https://github.com/arjyo851/HomeSolutions/assets/77008381/4eac7f54-344b-4cb7-bc90-8e8728d470e6)

### 2. Listing page

You can see all the listings here.

![HomeSolution-LIsting](https://github.com/arjyo851/HomeSolutions/assets/77008381/1bf13d5d-bc02-4e6c-bcf4-ec23f019805f)

### 3. About page

In about page, you can see about the company, top sellers and listed sellers.

![HomeSolution-About](https://github.com/arjyo851/HomeSolutions/assets/77008381/137a6524-b39c-4bd5-8bbd-278beea52bef)

### 4. Contact page

There is a seperate contact page from where you can contact to the company. You will also get response email after sending messages.

<img width="960" alt="HomeSolution-Contact" src="https://github.com/arjyo851/HomeSolutions/assets/77008381/11d18236-441b-4876-a9f5-b77bc99d44a9">

### 5. Login and Signup Page

You need an account to view the details page and make order. For that you just need to go to Signup page and create an account.

![HomeSolutions-Login](https://github.com/arjyo851/HomeSolutions/assets/77008381/6b8121f0-a8ca-4be2-9753-2527a59e8530)

![HomeSolutions-signup](https://github.com/arjyo851/HomeSolutions/assets/77008381/2419b5d2-82bc-49b8-bf8c-61f36184b6ed)

### 6. Details Page

You can view the details page after logging in. You can see the complete details about the house/condo/townhouse in this page. You can also see the images and description of those and about the seller also. You can also contact the seller directly from the contact section. If you want to buy, then you just need to click on "BUY NOW" button.

![HomeSolutions - Details](https://github.com/arjyo851/HomeSolutions/assets/77008381/05480e5a-392e-4b89-9950-1e620154fcde)

### 7. Buy Page

You can use "DISCOUNT100" coupon to buy that item. If you could buy that item successfully, then you will get confirmation message there only.

![HomeSolutions - buy](https://github.com/arjyo851/HomeSolutions/assets/77008381/3d82fa04-b7e2-4da4-89a1-88d3fb9c6f65)

### 8. Profile Page

In profile page, you can see about your info as well as the orders you have made. You can see your buyings on clicking on the Item Name coloured in blue.

![HomeSolutions - Profile](https://github.com/arjyo851/HomeSolutions/assets/77008381/c1299ee3-b502-421e-b9de-e411e4ea03ac)


### 9. Brought Page

You can see full details about what you have brought.

![HomeSolutions - brought](https://github.com/arjyo851/HomeSolutions/assets/77008381/f43a335b-c223-4b46-b688-bef39d08b1ce)

### 10. Admin Page

From the admin page, you can manage almost all things.

![HomeSolutions-admin](https://github.com/arjyo851/HomeSolutions/assets/77008381/fa0633c8-a4d4-4913-9655-06ce803d1e4b)


## Technologies Used

**Client:** React, Material-UI

**Backend:** Python, Django

**Database:** Sqlite

## Installation for backend

- Clone the project

```bash
https://github.com/arjyo851/HomeSolutions.git
```

- Navigate to the project directory:

```bash
cd HomeSolutions
```

- Create and activate a virtual environment

```bash
python3 -m venv venv
```
- Install the dependencies:

```bash
pip install -r requirements.txt
```

- Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

- For using administration features, create a superuser in django administration

```bash
python manage.py createsuperuser
```

after running this command set email, username  and password for admin

- Start the application

```bash
python manage.py runserver
```

## Installation for frontend

- Clone the project

```bash
https://github.com/arjyo851/HomeSolutions.git
```

- Navigate to the project directory:

```bash
cd HomeSolutions
```

- change all occurences of https://homesolutions2-0.onrender.com/ from frontend to http://127.0.0.1:8000 from VSCode

- Install node dependencies and start server

```bash
npm install
npm start
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement" or "feature".
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

This application is released under MIT License for fair use (see [License](https://github.com/arjyo851/HomeSolutions/blob/main/LICENSE)).

