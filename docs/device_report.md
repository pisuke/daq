# DAQ scan report for device 9a02571e8f01
Started

|  Role  |      Name              | Status |
|--------|------------------------|--------|
|Operator| *** Operator Name *** |        |
|Approver| *** Approver Name *** |        |

| Test iteration   |                        |
|------------------|------------------------|
| Test report date | XXX |
| 
| Attempt number   |  |

## Device Identification  

| Device            | Entry              |
|-------------------|--------------------|
| Name              |  |
| GUID              |  |
| MAC addr          | 9a:02:57:1e:8f:01 |
| Hostname          |  |
| Type              |  |
| Make              |  |
| Model             |  |
| Serial Number     |  |
| Firmware Version  |  |

## Device Description

![Image of device]()

N/A


### Device documentation

[Device datasheets]()
[Device manuals]()

## Report summary

|Result|Test|Notes|
|---|---|---|
|skip|base.switch.ping||
|pass|base.target.ping|target |
|fail|network.brute||
|pass|security.ports.nmap||

## Module ping

```
Baseline ping test report

RESULT skip base.switch.ping
RESULT pass base.target.ping target
```

## Module nmap

```
Allowing 10000 open tcp snet-sensor-mgmt
No invalid ports found.
RESULT pass security.ports.nmap
```

## Module brute

```
Username:manager
Password:friend
Login success!
RESULT fail network.brute
```

## Module switch

```
LOCAL_IP not configured, assuming no network switch.
```

## Report complete

