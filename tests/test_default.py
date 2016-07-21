def test_confluence_user(User):
    user = User("confluence")

    assert user.exists
    assert user.group == "confluence"
    assert user.shell == "/sbin/nologin"


def test_confluence_group(Group):
    group = Group("confluence")

    assert group.exists


def test_confluence_directories(File):
    directories = [
        '/opt/atlassian/confluence/5.9.12',
        '/var/atlassian/application-data/confluence'
    ]
    for directory in directories:
        d = File(directory)
        assert d.is_directory
        assert d.user == 'confluence'
        assert d.group == 'confluence'


def test_server_xml(File):
    config = File('/opt/atlassian/confluence/5.9.12/conf/server.xml')
    assert config.is_file


def test_server_started(File):
    config = File('/opt/atlassian/confluence/5.9.12/logs/catalina.out')
    assert config.contains('Server startup in')


def test_service_running(Service):
    service = Service('confluence')
    assert service.is_running
    assert service.is_enabled


def test_service_listening(Socket):
    socket = Socket('tcp://:::8090')
    assert socket.is_listening


def test_java_package_version(Package):
    package = Package('jdk1.80_101')
    assert package.is_installed
