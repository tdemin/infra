# tdem.in Infrastructure Repository

Configuration of all machines holding tdem.in and related services,
provided as an Ansible project.

## Usage

With [Taskfile][taskfile] and Ansible installed:

```
% task provision-all
```

[taskfile]: https://taskfile.dev

## Caveats

The initial machine setup is currently expected to be handled elsewhere
(for example, on server hosting provider control panel). This may change
in the future, as the hosting provider selected by the author of this
provides a [Terraform provider][tf].

There's no AWX-like GitOps tooling in place (and hence no runs
auditing), Ansible is expected to be run by admins by hand.

[tf]: https://registry.terraform.io/providers/contabo/contabo/latest/docs

## Copying

See [LICENSE.txt](LICENSE.txt).
