# Ansible Role: Confluence

Installs and configures an Atlassian Confluence Wiki instance.

## Requirements

* Java

## Optional components

* PostgreSQL

## Role Handlers

* confluence

Service state is expected to be controlled by a playbook.

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
|`confluence_version`|`changes`|String|The version of Confluence to manage|
|`confluence_install_dir`|`/opt/atlassian/confluence`|String|The directory to install Confluence|
|`confluence_home`|`/var/atlassian/application-data/confluence`|String|The Confluence home directory|
|`confluence_download_base`|https://www.atlassian.com/software/confluence/downloads/binary|
|`confluence_user`|confluence|The user which confluence will run as|
|`confluence_group`|confluence|The group for the confluence user|
|`confluence_uid`|33000|The UID of the user|
|`confluence_gid`|33000|The GID of the group|
|`confluence_manage_service`|true|Whether to manage the systemd service|

## Example playbook

```yaml

---
- hosts: servers
  roles:
  - ansible-confluence
```

## License

Apache 2.0

## Run the tests

This role includes Molecule tests that demonstrate a Confluence installation.

To run the tests:

Make sure you have the following prerequisites installed:

* Vagrant
* virtualenvwrapper

```
$ mkvirtualenv molecule
$ pip install molecule
```

To set up and test the role:

```
$ molecule test
```
