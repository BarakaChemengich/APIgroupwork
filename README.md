# API Groupwork - Travel Booking System

## Project Overview
**API Groupwork** is a Django-based web application for managing travel bookings.  
It allows users to view destinations, book trips, and manage their bookings easily through an interactive web interface.

---

## Apps in the Project

### 1. **Bookings App**
Handles all booking-related features:
- Create new trip bookings
- View all user bookings
- Admin approval (future feature)

**Main components:**
- `Booking` model — stores user, destination, date, number of people, and status.  
- `BookingForm` — allows users to select destinations, dates, and group size.  
- Views: `create_booking`, `view_bookings`  
- Templates: `create_booking.html`, `my_bookings.html`

---

### 2. **Destinations App**
Manages travel destinations users can choose from:
- Displays all available destinations.
- Future expansion may include prices, descriptions, and images.

**Main components:**
- `Destination` model — name, description, image, and price.
- View: `destination_list`
- Template: `destinations.html`

---

## Project Structure


