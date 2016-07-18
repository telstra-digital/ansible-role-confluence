require 'spec_helper'

context 'install' do
  describe group('confluence') do
    it { should exist }
  end

  describe user('confluence') do
    it { should exist }
    it { should belong_to_group 'confluence' }
    it { should have_login_shell '/sbin/nologin' }
  end
end

context 'directories' do
  [
    '/opt/atlassian/confluence/5.9.12',
    '/var/atlassian/application-data/confluence'
  ].each do |dir|
    describe file(dir) do
      it { should be_directory }
      it { should be_owned_by 'confluence' }
      it { should be_grouped_into 'confluence' }
    end
  end
end

context 'config files' do
  [
    '/opt/atlassian/confluence/5.9.12/conf/server.xml'
  ].each do |file|
    describe file(file) do
      it { should be_file }
      # its(:content) { should match /zone.*0.0.10.in-addr.arpa/ }
    end
  end
end

context 'server started' do
  describe file('/opt/atlassian/confluence/5.9.12/logs/catalina.out') do
    its(:content) { should match(/Server startup in/) }
  end
end

context 'service' do
  describe service('confluence') do
    it { should be_running }
  end

  describe port(8090) do
    it { should be_listening }
  end
end
