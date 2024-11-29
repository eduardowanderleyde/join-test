# Target Map Project

## Description

**Target Map** is a Django-based project that allows you to visualize targets on an interactive map using the Google Maps API. Additionally, the system provides functionality to create new targets with geographic coordinates and an expiration date. This application is built to demonstrate how to integrate geospatial data with a Django backend and a frontend interface using JavaScript.

<img width="1511" alt="Captura de Tela 2024-11-29 às 17 34 09" src="https://github.com/user-attachments/assets/8118e069-d571-404c-9ef7-2be4b05f499a">

## Features

- **Display Targets on Map**: The map displays markers representing the registered targets.
- **Create New Targets**: Users can add new targets through a form that includes the name, latitude, longitude, and expiration date.
- **Dynamic Display**: When a new target is saved, the page automatically updates to show the new location on the map.

## Technologies Used

- **Django**: Backend framework for web development.
- **PostgreSQL**: Relational database used to store the target data.
- **Google Maps API**: Used for rendering the map and displaying target markers.
- **JavaScript** (with jQuery): Used for frontend interactions, such as map display and form manipulation.
- **Django REST Framework**: Used to create a RESTful API to handle CRUD operations for targets.
- **HTML/CSS**: Structure and styling of the page.

## Installation

### Prerequisites

- Python 3.x
- Django 5.x
- PostgreSQL (or another compatible database)

### Steps to Run the Project Locally

1. **Clone the repository:**

```bash
git clone (https://github.com/eduardowanderleyde/join-test.git
```

Frontend
The user interface is rendered in HTML with an interactive map, where targets are shown as geographical markers. The frontend uses JavaScript to send data via fetch to the API and update the map dynamically.

Contributing
If you would like to contribute to this project, please follow these steps:

Fork the project.
Create a branch for your feature (git checkout -b feature/new-feature).
Make your changes and commit them (git commit -am 'Add new feature').
Push your branch to your fork (git push origin feature/new-feature).
Open a pull request.

License


Contact
If you have any questions or suggestions, feel free to contact us!
