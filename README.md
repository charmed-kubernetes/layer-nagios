# Nagios Layer for Juju Reactive Charms

This layer provides the standard boilerplate to relate your charm to
the nrpe subordinate (https://jujucharms.com/nrpe).

To use, reference this layer in your layer.yaml file. Add custom
nagios checks using the interface provided by the
nrpe-external-master interface
(https://github.com/cmars/nrpe-external-master-interface) or
charm-helpers (http://pythonhosted.org/charmhelpers/).

## Future

This layer may provide helpers to make maintaining nagios
checks easier.

## Contact

- https://launchpad.net/nagios-layer
