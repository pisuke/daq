# Changelog
* 1.9.10
  * IP addr flush (#672)
  * Fix Cisco switch power response (#679)
  * Add SSH Reporting, SSH Bug Fixes  (#670)
  * IP Change (11) (#658)
  * Update NTP support test fix #622 (#595)
  * set gateway set vlan (#671)
  * Update dependency jsoneditor to v9.1.1 (#654)
  * External Gateway (#664)
  * New "new ip" assignment, extend rpc_timeout_sec and ping counts for Cisco switches (#666)
  * Update dependency commons-net:commons-net to v3.7.1 (#663)
  * gateway refactoring (#662)
  * Add manual tests to resource config (#621)
  * Tls timeout fix and ohter updates (#651, #626)
  * Private Address (6) (#584)
  * DHCP Short (9) (#579)
  * Cisco switch more expected table output (#657)
  * Pin dependency node-forge to 0.10.0 (#653)
  * Basic UDMI provisioner test (#648)
  * Update dependency node-forge to v0.10.0 [SECURITY] (#650)
  * ipaddr DHCP timeout behavior change (#652)
  * Adding node-forge upgrade (#649)
  * fix no_test option (#647)
  * granular dhcp test timeouts. (#645)
  * Update UDMI version to 1.2.0 (#646)
  * Disable stickler print-function check (#637)
  * Clear out port_acls directory for local test runs. (#640)
  * Feature/native tests (#625)
  * Update dependency jsoneditor to v9.1.0 (#642)
  * Update dependency firebase-admin to v9.2.0 (#641)
  * switch config files (#633)
  * Add DNS hostname resolution test (#638)
  * Update dependency org.junit.jupiter:junit-jupiter to v5.7.0 (#639)
  * Bump node-fetch from 2.6.0 to 2.6.1 in /firebase/functions (#635)
  * add raw output from usi. (#636)
  * Merging ipaddr and dhcp (#634)
  * Update dependency io.grpc:grpc-protobuf to v1.32.1 (#630)
  * Update dependency io.grpc:grpc-bom to v1.32.1 (#631)
  * Update dependency io.grpc:grpc-stub to v1.32.1 (#632)
  * Update dependency io.grpc:grpc-netty-shaded to v1.32.1 (#629)
  * Update dependency jsoneditor to v9.0.5 (#628)
  * Adding timestamps to ipaddr test log messages. (#627)
* 1.9.6
  * Switch poe updates (#605) - Alignment of PoE test to test plan.
  * Cisco Switches parsing fix (#623)
  * usi logs gcp and local capture (#613)
* 1.9.5
  * Increase nmap module timeout (#611)
  * Improvements for test development debugging (#609)
  * Add module config system logging (#607)
* 1.9.4
  * Feature/convert switchtests (#601)
  * Do not infinite spawn ntp (#598)
  * security.nmap.http test (#563)
  * Update registrar tool for latest UDMI version (#596)
  * Feature/vlan trigger (#588)
  * fix gcp combine report test (#587)
  * Adding default dns for static ip faux devices (#576)
  * Add perodic tests (#575)
  * security.admin.password changes (#461)
* 1.9.0
  * Test infrastructure cleanup (#572)
  * Remove faux dependencies from subset directory (#567)
  * Github actions (#558)
  * misc updates to docs (#568)
  * Incorporate manual test comments (#499)
  * NTP Update (#525)
  * Automatic build script (#557)
* 1.8.2
  * GRPC timeouts + usi first command wait fix. (#555)
  * Numerous renovate bot updates.
* 1.8.0
  * add security.ssh.version test  (#523)
  * Refactor UDMI to external repo (#544)
  * Additional DHCP test part 3: IP change test (#543)
  * Additional DHCP test part 2: Multisubnet test (#539)
  * Additional DHCP test part 1 (#532)
  * Support for alternate sec switch (not managed by DAQ) (#531)
  * Add troubleshooting script (#529)
  * Using usi in daq (#520)
  * Use trunk rather than stack between switches (#526)
  * NTPv4 support (#487)
  * Feature/usi OVS switch (#521)
* 1.7.0
  * Add DAQ version to origin summary (#522)
  * Add check for git version tag in Travis (#519)
  * Minor UDMI updates for pubber keygen
  * Update Minimum Send Test (#498)
  * Universal Switch Interface (USI) (#496)
* 1.6.1
  * fix image pull in cmd/build (#503)
* 1.6.0
  * cloud test setup documentation (#495)
  * Baseline for NTP tests (#494)
  * Baseline for DNS test (#492)
  * Add manual test summary to test report (#481)
  * UDMI logentry schema update (#391)
* 1.5.1
  * Fix for local-port-as-string issue (#477)
* 1.5.0
  * Numerous renovate-bot updgrades
  * Move reporting.sh into docker/include (#473)
  * Remove redundant system.conf (#470)
  * Cleanup files from misc (#464)
  * Update UDMI asset naming (#457)
  * Make startup commands implicit (#466)
  * Whitespace testing changes (#468)
  * Add stickler.yml (#465)
  * Feature/combine reports from date range (#458)
  * Cleanup dot1x and docker test files from misc (#462)
  * port disconnect integration test fix.
  * Use module_config for module switch configuration (#459)
  * Fix network tests  (#440)
  * Add explicit faucet python base (#455)
  * Terminate on DAQ trunk port going down (#445)
  * UDMI Gateway Schema Update (#363)
  * Fix unit tests (#448)
  * MD Table Refactoring (#452)
  * Minor debug fixes (#453)
  * Convert PortInfo dict to class (#447)
  * cleanup misc folder, moving files to etc and resources (#449)
  * Fix flaky port disconnects (#450)
* 1.4.1
  * Fetch before checkout (#446)
  * Refactoring configuration mechanism (#444)
* 1.4.0
  * Update Faucet version to 1.9.43 (#443)
  * Minor release docs update (#442)
  * update techsupport to use new switchconfig names. include date-time in name of created file (#437)
  * Physical switch config tweaks (#436)
  * Firebase db Docs update (#433)
  * Check for missing docker images (#435)
  * Feature/allow port toggle (#423)
  * Refactoring switchconfig (#426)
  * Add switch report output (#431)
  * Test default clean base configuration (#430)
  * added EasyIO FW-14 to device_types (#427)
  * enable finish_hook by default (#425)
  * Move generated proto files out of daq/ (#424)
  * Apply strict config checking (#422)
  * UDMI change force_value to fix_value (#420)
  * leave venv for mininet build  (#421)
  * Introduce YAML config file (#418)
  * Add password switch config (#324)
  * Update TLS methods and tests (#362)
* 1.3.0
  * Cisco switch power (#375)
  * Firebase data storage changes and supporting filters on UI (#395)
  * Firebase data retention policy (#395)
  * script for setting up / resetting service account permissions (#409)
  * Fix misleading pics report output when no pics.csv file found (#404)
  * Use python3.7 for faux2 (#410)
  * add script to collect diagnostic info by user before they reach out (#405)
  * adding pdf report (#406)
  * Address cisco switch test access (#403)
  * add checks for interfaces to switch being defined and up (#399)
  * Introduction of the `resources` folder used for a device types library and for setups templates (#376)
* 1.2.0
  * ssh tunnel document addition (#393)
  * Build aardvark for travis module test (#388)
  * Feature/ui improvements v2 (#384)
  * adding time to log messages (#381)
  * Fix physical switch setup and test (#379)
  * Base configurator unit test (#373)
  * Fix up password test redaction (#370)
  * Feature/proper ip test (#369)
  * Make nmap more robust, add finish_hook (#368)
  * Fix result extraction for reports (#367)
  * Create alternate faux container image (#366)
  * Use VLANs for DAQ dataplane (#360)
  * Feature/push results as json (#357)
* 1.1.0
  * Fixing version to python 3.7, requires recent version of debian
  * Log and display more version info into GCP project
  * Don't abbreviate description in test module manifest
  * Overhaul of DHCP tests and test capabilities
  * Save all configs and many run logs to GCP
  * Update UDMI metadata validator to include site summary report
  * Use dockerhub docker images for tagged releases
  * Capability for specifying static_ips for devices
  * Individual module test capability (run docker test without daq)
  * Runtime logs to GCP stackdriver
  * Add basic site-indexed device-centric console
  * Create PDF reports
  * Device report output reformatting
  * Convert to base64 encoded credentials for cloud-based tests
  * Poe switch test capability
  * Added switch_model property in system.conf for using switch tests
  * Support for Cisco Catalyst 9300 series network switches in the switch test
  * Passwords test module for checking devices against a default set of passwords
  * BACnet firmware discovery test
  * Addition of port configuration for running nmap for port scanning
  * Updated to faucet 1.9.36 and forch 0.33
* 1.0.2
	* Faucet update to 1.9.19, including explicit LLDP stacking acls.
	* Update Travis build environment to Bionic (prev. Trusty).
	* Lock versions of some google pip packages: Firestore hang workaround.
	* Use base64 endcoded GCP cred rather than shell-encoded.
	* Deprecate GCP_SERVICE_ACCOUNT env for GCP_BASE64_CRED.
* 1.0.1
	* Category and expectation table outputs.
	* UDMI schema validator test module.
	* Build improvements for various base system configurations.
	* Firebase web authentication
	* Test module state names update
* 1.0.0
	* Device and system schema validation in web-ui.
	* Extended BACnet test module for PIC statements.
	* TLS security test module for certificate validation.
	* MAC OUI test module for manufacturer lookup.
	* Fix for Firestore-disconnect bug with long standing sessions.
	* Automatic population of new device directory from template.
	* Numerous docs fixes and updates.
	* Faucet version 1.9.8 update.
* 0.9.7:
        * Device-level test configuration (e.g. allowed open ports)
	* Use table for test report output
	* Dynaimic runtime config capability
	* Ability to select runtime test module execution
* 0.9.6:
	* UDMI Tech Stack definition (MQTT + JSON + UDMI).
	* Updating BacNET tests to have more predictable/regular identifiers.
	* Generate markdown-based reports in site device folder.
	* Registrar tool for cloud-based device registration.
	* Debian Stretch setup/install fixes.
	* Update to Faucet 1.9.1.
* 0.9.5
	* DAQ_TARGETS env variable for incremental builds.
	* Report file cleanup, with embedded test results.
	* DHCP long switchover and dhcp request logs.
	* Updating python package versions.
	* Forced workaround delay for faucet config change race-condition.
	* Faucet performance fix for large port counts.
	* Fix internal lint checks.
	* Faux command uses explicit interface designation.
	* Faux command does not rename explicit interface.
* 0.9.4
	* Faucet update to 1.8.35
	* Move device configuration data under `site_path` parameter.
	* Switch-based tests (port errors, port negotiation)
* 0.9.3
	* Device description capability for report generation.
	* Fixes for broken local_switch setup and docs.
	* Build and release documentation updates.
	* Dual stacking topology tests.
	* Port debounce feature for flaky ports.
	* Updates to FCU example status messages.
	* Debugging fail_hook setting.
	* Faucet update to version 1.8.34.
* 0.9.2
	* Stacking topology generator.
	* SWITCH_PORT env variable available to tests.
	* Automatic detection of re-build required.
	* Topology test for "commissioning".
	* Stability improvements for network topology tests.
* 0.9.1
	* Adding test_config option for dynamic test configurations.
	* Enforce gateway test group isolation.
	* Issue a representative FCU example for UDMI encodings.
	* Bacnet topology tests (open, single, halves, star)
	* Mock-switch capability for direct-to-switch tests.
	* Bacnet4j version updates for looped discovery tests.
	* Packet capture files for gateways and individual tests.
	* General improvements to system test stability.
	* Brute-force telnet password checks.
	* Update Faucet version to 1.8.32.
	* Increased MUD-file enforcement (to-device).
	* Misc build issues for current Debian/Ubuntu systems.
* 0.9.0
	* Upping major version number because of breaking config changes.
	* Updating schema validator code structure.
	* Improved internal checks on startup sequence.
	* Autogenerate faucet.yaml file, rather than relying on template.
* 0.8.3
	* Upload test report to a cloud storage bucket included in web page.
	* Bug fixes for startup pcap capture.
	* Minor debugging output improvements.
	* MUD file generator 'controller' capability.
	* Documentation updates: topology, firebase, validator, debugging.
	* Updated FAUCET to version 1.8.25.
* 0.8.2
	* Update to use python3 (may require bin/clean for local setups).
	* Adding docs for test lab setup.
	* Improvements to docker test stability.
	* Purge old docker containers after new image download.
	* MUD file generator error message improvements.
	* Add -n (no_test) mode to just put devices on network.
	* Make cmd/run behavior configurable (in- or ex- to container).
	* Preliminary schema validation capability.
* 0.8.1
	* Refactor gateway component out from individual device tests.
	* Move more configuration to faucet.yaml files.
	* Enable device groups.
	* Clean up testing infrastructure.
* 0.8.0
	* Dynamic application of MUD files.
	* Pull network topology from faucet.yaml file.
