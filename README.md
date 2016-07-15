# Ansible Role: Confluence

Installs and configures Confluence.

## Requirements

* Java

## Role Handlers

None. Service state is expected to be controlled by a playbook.

## Role Variables

|Name|Default|Type|Description|
|----|----|-----------|-------|
|`confluence_version`|`changes`|String|The version of Confluence to manage|
|`confluence_install_dir`|`/opt/atlassian/confluence`|String|The directory to install Confluence|
|`confluence_home`|`/var/atlassian/application-data/confluence`|String|The Confluence home directory|

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
$ git clone https://github.com/metacloud/molecule.git
$ pip install -U -e molecule/
```

To set up and test the role:

```
$ molecule test
```
