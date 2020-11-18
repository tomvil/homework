```
kitchen verify
-----> Starting Test Kitchen (v2.7.2)
-----> Verifying <node1-CumulusCommunity-cumulus-vx>...
       Preparing files for transfer
-----> Busser installation detected (busser)
-----> Busser plugin detected: busser-bats
       Removing /tmp/verifier/suites/bats
       Transferring files to <node1-CumulusCommunity-cumulus-vx>
-----> Running bats test suite
 ✓ Check if 10.1.1.2 bgp neighbor is UP
 ✓ Check if 10.1.2.2 bgp neighbor is UP
       
       2 tests, 0 failures
       Downloading files from <node1-CumulusCommunity-cumulus-vx>
       Finished verifying <node1-CumulusCommunity-cumulus-vx> (0m2.45s).
```
