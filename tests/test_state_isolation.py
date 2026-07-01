def test_state_change_does_not_break_current_test(client):
    # Arrange
    activity_name = "Chess Club"
    email = "isolation.check@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup", params={"email": email}
    )
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert email in activities_response.json()[activity_name]["participants"]


def test_state_is_reset_before_next_test(client):
    # Arrange
    activity_name = "Chess Club"
    email = "isolation.check@mergington.edu"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert email not in response.json()[activity_name]["participants"]
