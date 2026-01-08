CREATE TABLE events(
                       EventID INTEGER PRIMARY KEY,
                       EventName VARCHAR(255),
                       EventDateTime TIMESTAMPTZ,
                       EventLocation VARCHAR(255)
);

CREATE TABLE users(
                      UserID INTEGER PRIMARY KEY,
                      Username VARCHAR(255) NOT NULL,
                      UserEmailId VARCHAR(255)
);

CREATE TABLE seats(
                      SeatIdentifier VARCHAR(255),
                      EventID INTEGER,
                      PRIMARY KEY (SeatIdentifier, EventID),
                      FOREIGN KEY (EventID) REFERENCES events(EventID)
);

CREATE TABLE bookings(
                         UserID INTEGER,
                         SeatIdentifier VARCHAR(255),
                         EventID INTEGER,
                         PRIMARY KEY (UserID, SeatIdentifier, EventID),
                         FOREIGN KEY (UserID) REFERENCES users(UserID),
                         FOREIGN KEY (SeatIdentifier, EventID) REFERENCES seats(SeatIdentifier,EventID)
);