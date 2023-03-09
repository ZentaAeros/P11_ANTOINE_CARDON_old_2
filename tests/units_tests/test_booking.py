from server import app
import server

client = app.test_client()

server.competitions = [
    {"name": "closedCompetition", "date": "2020-03-05 23:14:00", "numberOfPlaces": "6"},
    {"name": "openCompetition", "date": "2024-03-05 23:14:00", "numberOfPlaces": "6"},
]

server.clubs = [
    {"name": "name of the club", "email": "john@simplylift.co", "points": "8"}
]


def test_booking_with_more_twelve_points():
    response = client.post(
        "/purchasePlaces",
        data={
            "places": 13,
            "club": server.clubs[0]["name"],
            "competition": server.competitions[0]["name"],
        },
    )

    assert "Vous ne pouvez pas réserver + de 12 places" in response.data.decode()
