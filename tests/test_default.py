def test_confluence_user(User):
    user = User("confluence")

    assert user.exists
    assert user.group == "confluence"
