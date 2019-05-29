# DAQ scan report for device 9a02571e8f00
Started %% 2019-05-29 11:15:03+00:00

|  Role  |      Name              | Status |
|--------|------------------------|--------|
|Operator| Francesco Anselmo |        |
|Approver| Trevor Pering |        |

| Test report date | 2019-05-29T11:15:03.268Z |
| DAQ version      | 0.9.7 |
| Attempt number   | 1 |

## Device Identification  

| Device            | Entry              |
|-------------------|--------------------|
| Name              | WF-1 |
| GUID              | N/A |
| MAC addr          | 9a:02:57:1e:8f:00 |
| Hostname          | N/A |
| Type              | Telegraph |
| Make              | Marconi Company |
| Model             | Wireless Telegraph |
| Serial Number     | N/A |
| Firmware Version  | N/A |

## Device Description

![Image of device](https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Marconi%27s_first_radio_transmitter.jpg/220px-Marconi%27s_first_radio_transmitter.jpg)

Guglielmo Marconi's first radio transmitter


### Device documentation

[Device datasheets]()
[Device manuals]()

## Report summary

|Result|Test|Notes|
|---|---|---|
|skip|base.switch.ping||
|pass|base.target.ping|target |
|skip|network.brute||
|pass|security.ports.nmap||

## Module ping

```
Baseline ping test report
%% 35 packets captured.
RESULT skip base.switch.ping
RESULT pass base.target.ping target %% 10.20.59.37
```

## Module nmap

```
No invalid ports found.
RESULT pass security.ports.nmap
```

## Module brute

```
Target port 10000 not open.
RESULT skip network.brute
```

## Report complete

