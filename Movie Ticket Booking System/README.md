# Movie Ticket Booking System

Imagine you’re trying to book tickets for a blockbuster movie on a busy weekend. You log into the booking system, browse through the available showtimes, select your preferred seats, and proceed to book them. Within moments, your tickets are confirmed, and you receive a digital ticket. Behind the scenes, the system is efficiently managing seat availability, tracking screenings, and calculating ticket costs. Now, let’s design a movie ticket booking system that handles all of this seamlessly.

## 1) Functional Requirements

- Each cinema is located at a specific location and contains multiple rooms.
- Movies can have multiple screenings scheduled across different rooms, cinemas, and time slots.
- Each room has a grid of seats available for booking.
- Seats within a room can have varying pricing strategies (e.g., normal, premium, VIP) that affect ticket prices.
- Users can find and book available tickets.
- A ticket represents a specific seat to watch a movie in a room at a particular time.
- A user can book multiple tickets within the same order.
- The total cost for an order is computed by summing the prices of all selected seats, based on their pricing tiers.

## 2) Non-functional Requirements

- Fast searches for screenings for a smooth user experience.
- Basic error handling should prevent booking conflicts, such as double-booking the same seat.

## 3) Core Objects

- **_Seat_** : Represents an individual seat in a room linked to a pricing strategy.
- **_Movie_** : a movie object with details about the movie.
- **_Layout_** : Organizes the seating arrangement in a room as a grid, managing seat positions.
- **_Room_** : Defines a screening space within a cinema, tied to a unique layout of seats.
- **_Cinema_** : Models a physical location where movies are screened, containing multiple rooms.
- **_Screening_** : Combines a movie, a room, and a time slot to define when and where a movie is shown.
- **_Ticket_** : Captures a customer’s choice of a specific seat for a screening, including its price.
- **_Order_** : Groups multiple tickets purchased together into a single transaction, tracking the total cost.
- **_ScreeningManager_** : ScreeningManager class manages key operations, such as searching for screenings of specific movies, identifying available seats, and storing purchased tickets.
- **_MovieBookingSystem_** : It integrates the list of movies, cinema locations, and an instance of ScreeningManager into a cohesive system. It acts as a facade, streamlining user interactions by delegating tasks to underlying classes like ScreeningManager, Movie, and Cinema.