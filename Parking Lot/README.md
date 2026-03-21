# Parking Lot Design

## 1) Functional Requirements

- The parking lot has multiple parking spots, including compact, regular, and oversized spots.
- The parking lot supports parking for motorcycles, cars, and trucks.
- Customers can park their vehicles in spots assigned based on vehicle size.
- Customers receive a parking ticket with vehicle details and entry time at the entry point and pay a fee based on duration, vehicle size, and time of day at the exit point.

## 2) Non-functional Requirements

- The system must scale to support large parking lots with many spots and vehicles.
- The system must reliably track spot assignments and ticket details to ensure accurate operations.

## 3) Core Objects

- **_Vehicle_** : vehicle details like license plate and size (small for motorcycles, medium for cars, large for trucks.)
- **_Ticket_** : ticket details like entry time, spot, vehicle and exit time.
- **_Spot_** : spot details like availability and type (compact, regular, oversized, etc.)
- **_TicketManager_** : manages ticket
- **_FareCalculator_** : calculates fares based on vehicle type, duration and strategy.
- **_SpotManager_** : manages spot
- **_LotManager_** : manages parking lot