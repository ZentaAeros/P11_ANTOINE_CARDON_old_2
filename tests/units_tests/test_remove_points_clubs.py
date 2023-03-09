from server import app
import server

client = app.test_client()

""" TEST BOOKING COMPETITION : Check clubs points """


def test_to_remove_points_clubs():
    server.clubs[0]["points"] = "5"

    points_of_club_before_booking = server.clubs[0]["points"]
    response = client.post(
        "/purchasePlaces",
        data={
            "places": 3,
            "club": server.clubs[0]["name"],
            "competition": server.competitions[0]["name"],
        },
    )

    points_of_club_after_booking = server.clubs[0]["points"]

    assert int(points_of_club_after_booking) < int(points_of_club_before_booking)
    assert response.status_code == 200
