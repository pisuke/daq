# DAQ scan report for device 9a02571e8f01

Started 2019-03-23 14:47:25+00:00

DAQ release 0.9.6

|  Role  |      Name       | Status |
|--------|-----------------|--------|
|Operator| <operator_name> |        |
|Approver| <approver_name> |        |


## Device identification

| Device        | Entry              |
|---------------|--------------------|
| Name          | <device_name>      |
| GUID          | <namespace>://<id> |
| MAC addr      | 9a:02:57:1e:8f:00  |
| Hostname      | <hostname>         |
| Type          | <device_type>      |
| Manufacturer  | <manufacturer>     |
| Model         | <model>            |
| Serial Number | <serial_number>    |
| Firmware      | <firmware_version> |
| Attempt Number| <attempt_number>   |


## Device description

<device description text>

![Image of device](https://company.com/device_image.jpg)

For example, here is an inline image.
![Image of a radio](https://wgp-cdn.co.uk/CESC/jpg/Marconi_crystal_radio_receiver-63177/600/600/)


### Device documentation

[Device datasheet name](https://company.com/datasheet.pdf)
[Device manual](https://company.com/manual.pdf)

For examplel, here is a link to a document (can be a PDF, an image, etc.)
[Link to specification sheet](https://i.pinimg.com/originals/88/10/a5/8810a5d931f120ddb8f9a77ec5e34d44.jpg)

### Manufacturer details

Company address
Company phone numbers
Company email
Company website

#### Technical contacts

Name Surname
Role
Address
Phone numbers
Email address

## Automatic tests report summary

| Compliance category  | Result |
|-----------------|---------|
| COMPLIANT       | PASS     |
| OPTIMISED       | PASS     |


### Automatic tests summary

| Test category   | PASS    |  FAIL | SKIP | ERROR |
|-----------------|---------|-------|------|-------|
| REQUIRED        | 12      |  1    |   3  |   0   |
| RECOMMENDED     | 0       |  0    |   1  |   0   |

### Automatic tests list

| Test name                  | Test category  |  Status | Link to test output                                             |
|----------------------------|----------------|---------|-----------------------------------------------------------------|
| connection.dhcp.short      | REQUIRED       | PASS    | [connection.dhcp.short output](#connection-dhcp-short)       |
| connection.min_send        | REQUIRED       | PASS    | [connection.min_send output](#connection-min_send)|
| connection.network.address | REQUIRED       | PASS    | [connection.network.address output](#connection-network-address)|
| connection.ping            | REQUIRED       | PASS    | [connection.ping output](#connection-ping)|  
| connection.port_duplex     | REQUIRED       | PASS    | [connection.port_duplex output](#connection-port_duplex)|   
| connection.port_link       | REQUIRED       | PASS    | [connection.port_link output](#connection-port_link)|  
| connection.port_speed      | REQUIRED       | PASS    | [connection.port_speed output](#connection-port_speed)|
| network.ntp_server         | REQUIRED       | FAIL    | [network.ntp_server output](#network-ntp_server)|
| poe.negotiation            | REQUIRED       | SKIP    | [poe.negotiation output](#poe-negotiation)|
| poe.power                  | REQUIRED       | SKIP    | [poe.power output](#poe-power)|
| poe.support                | REQUIRED       | SKIP    | [poe.support output](#poe-support)|
| protocol.bacnet.pic        | REQUIRED       | PASS    | [protocol.bacnet.pic output](#protocol-bacnet-pic)|
| protocol.bacnet.version    | REQUIRED       | PASS    | [protocol.bacnet.version output](#protocol-bacnet-version)|
| security.https             | REQUIRED       | PASS    | [security.https output](#security-https)|
| security.portscan          | REQUIRED       | PASS    | [security.portscan output](#security-portscan)|
| security.tls.v3            | REQUIRED       | PASS    | [security.tls.v3 output](#security-tls-v3)|
| security.tls.v4            | RECOMMENDED    | SKIP    | [security.tls.v4 output](#security-tls-v4)|


## Manual tests report summary

### Manual tests summary

| Test category   | PASS    |  FAIL | SKIP | ERROR |
|-----------------|---------|-------|------|-------|
| REQUIRED        | 0       |  0    |   1  |   0   |
| RECOMMENDED     | 0       |  0    |   13 |   0   |

### Manual tests list

| Test name                         | Test category  |  Status | Details                                                  |
|-----------------------------------|----------------|---------|----------------------------------------------------------|
| manual.bluetooth_support          | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.comms_down                 | REQUIRED       | SKIP    | N/A                                                      |
| manual.default_pwd_changeable     | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.dns_server                 | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.flash_plugin_not_required  | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.java_plugin_not_required   | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.sec_eth_port               | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.sec_eth_port_noip          | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.wireless_11ac_support      | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.wireless_11g_support       | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.wireless_11n_support       | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.wireless_ap_disabled       | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.wireless_support           | RECOMMENDED    | SKIP    | N/A                                                      |
| manual.wireless_wpa2-psk_support  | RECOMMENDED    | SKIP    | N/A                                                      |


## Module ping

Description of ping module

### ping tests

#### connection-ping
REQUIRED | PASS

Description of test

<test output>


## Module dhcp

Description of dhcp module

### dhcp tests

#### connection-dhcp-short
REQUIRED | PASS

Description of test

<test output>

## Module network

Description of network module

### network tests

#### connection-min_send
REQUIRED | PASS

Description of test

<test output>

## Module nmap

Description of nmap module

### nmap tests

#### connection.network.address
REQUIRED | PASS

Description of test
<test output>

#### network.ntp_server
REQUIRED | PASS
Description of test
<test output>

#### security.https
REQUIRED | PASS

Description of test
<test output>

#### security.portscan
REQUIRED | PASS

Description of test
<test output>

```
No open ports found.
```

## Module tls

Description of tls module

### tls tests

#### security.tls.v3
REQUIRED | PASS

Description of test
<test output>

#### security.tls.v4
REQUIRED | PASS

Description of test
<test output>

## Module switch

Description of switch module

### switch tests

#### connection.port_duplex
REQUIRED | PASS

Description of test
<test output>

#### connection.port_link
REQUIRED | PASS

Description of test
<test output>

#### connection.port_speed)
REQUIRED | PASS
Description of test
<test output>

#### poe.negotiation
REQUIRED | PASS
Description of test
<test output>

#### poe.power
REQUIRED | PASS
Description of test
<test output>

#### poe.support
REQUIRED | PASS
Description of test
<test output>


## Module bacnet

Description of bacnet module 
