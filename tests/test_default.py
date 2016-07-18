def test_confluence_user(User):
    user = User("confluence")

    assert user.exists
    assert user.group == "confluence"


def test_confluence_group(Group):
    group = Group("confluence")

    assert group.exists
