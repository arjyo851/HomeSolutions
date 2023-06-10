
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

![HomeSolutios- Home](https://github.com/arjyo851/HomeSolutions/assets/77008381/23ad4890-ef61-4dcd-9a19-dc59b7f87502)

### 2. Listing page

You can see all the listings here.

![HomeSolutions - Listing](https://github.com/arjyo851/HomeSolutions/assets/77008381/767cc3ce-a051-4ead-8708-8d082211ec60)

### 3. About page

In about page, you can see about the company, top sellers and listed sellers.

![HomeSolutions - About](https://github.com/arjyo851/HomeSolutions/assets/77008381/19140113-3403-4166-a1aa-ea3fb0e8f9b6)

### 4. Contact page

There is a seperate contact page from where you can contact to the company. You will also get response email after sending messages.

![HomeSolutions - Contact](https://github.com/arjyo851/HomeSolutions/assets/77008381/4da9928a-504e-4a1b-a605-1498d52b962f)

### 5. Login and Signup Page

You need an account to view the details page and make order. For that you just need to go to Signup page and create an account.

![HomeSolution - login](https://github.com/arjyo851/HomeSolutions/assets/77008381/974e186a-29a9-41b0-a1cc-eda69b32072a)

![HomeSolutions-signup](https://github.com/arjyo851/HomeSolutions/assets/77008381/2748d524-3436-4c83-8f78-6fa1636ddb43)

### 6. Details Page

You can view the details page after logging in. You can see the complete details about the house/condo/townhouse in this page. You can also see the images and description of those and about the seller also. You can also contact the seller directly from the contact section. If you want to buy, then you just need to click on "BUY NOW" button.

![HomeSolutions - Details](https://github.com/arjyo851/HomeSolutions/assets/77008381/956cc47e-2e11-4d7b-9b6d-581b3be06515)

### 7. Buy Page

You can use "DISCOUNT100" coupon to buy that item. If you could buy that item successfully, then you will get confirmation message there only.

![HomeSolutions - buy](https://github.com/arjyo851/HomeSolutions/assets/77008381/a4b869c0-5b3d-49f2-b748-db84b9ec8ebd)

### 8. Profile Page

In profile page, you can see about your info as well as the orders you have made. You can see your buyings on clicking on the Item Name coloured in blue.

![HomeSolutions - Profile](https://github.com/arjyo851/HomeSolutions/assets/77008381/50f358c9-6973-4378-aa90-724693d5208c)


### 9. You can see full details about what you have brought.

You can see full details about what you have brought.

![HomeSolutions - brought](https://github.com/arjyo851/HomeSolutions/assets/77008381/bc069333-642c-47cd-9efa-99df1d8e20f6)

### 10. Admin Page

From the admin page, you can manage almost all things.

![HomeSolutions-admin](https://github.com/arjyo851/HomeSolutions/assets/77008381/e1e7c8dd-90de-4637-9203-5973c2421643)


## Technologies Used

**Client:** React, Material-UI
**Backend:** Python, Django
**Database"** Sqlite

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

