# Class MidiDeviceProvider

**Source:** `java.desktop\javax\sound\midi\spi\MidiDeviceProvider.html`

### Class Description

```java
public abstract class
MidiDeviceProvider

extends
Object
```

A

MidiDeviceProvider

is a factory or provider for a particular type
of MIDI device. This mechanism allows the implementation to determine how
resources are managed in the creation and management of a device.

---

### Field Details

*No entries found.*

### Constructor Details

#### public MidiDeviceProvider()

*No description found.*

---

### Method Details

#### public boolean isDeviceSupported​(
MidiDevice.Info
info)

Indicates whether the device provider supports the device represented by
the specified device info object.

**Parameters:**
- info

- an info object that describes the device for which support
is queried

**Returns:**
- true

if the specified device is supported, otherwise

false

**Throws:**
- NullPointerException

- if

info

is

null

---

#### public abstract
MidiDevice.Info
[] getDeviceInfo()

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

**Returns:**
- set of device info objects

---

#### public abstract
MidiDevice
getDevice​(
MidiDevice.Info
info)

Obtains an instance of the device represented by the info object.

**Parameters:**
- info

- an info object that describes the desired device

**Returns:**
- device instance

**Throws:**
- IllegalArgumentException

- if the info object specified does not
match the info object for a device supported by this

MidiDeviceProvider
- NullPointerException

- if

info

is

null

---

### Additional Sections

#### Class MidiDeviceProvider

java.lang.Object

- javax.sound.midi.spi.MidiDeviceProvider

javax.sound.midi.spi.MidiDeviceProvider

```java
public abstract class
MidiDeviceProvider

extends
Object
```

A

MidiDeviceProvider

is a factory or provider for a particular type
of MIDI device. This mechanism allows the implementation to determine how
resources are managed in the creation and management of a device.

public abstract class

MidiDeviceProvider

extends

Object

A

MidiDeviceProvider

is a factory or provider for a particular type
of MIDI device. This mechanism allows the implementation to determine how
resources are managed in the creation and management of a device.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MidiDeviceProvider

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

MidiDevice

getDevice

​(

MidiDevice.Info

info)

Obtains an instance of the device represented by the info object.

abstract

MidiDevice.Info

[]

getDeviceInfo

()

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

boolean

isDeviceSupported

​(

MidiDevice.Info

info)

Indicates whether the device provider supports the device represented by
the specified device info object.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

MidiDeviceProvider

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

MidiDevice

getDevice

​(

MidiDevice.Info

info)

Obtains an instance of the device represented by the info object.

abstract

MidiDevice.Info

[]

getDeviceInfo

()

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

boolean

isDeviceSupported

​(

MidiDevice.Info

info)

Indicates whether the device provider supports the device represented by
the specified device info object.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Obtains an instance of the device represented by the info object.

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

Indicates whether the device provider supports the device represented by
the specified device info object.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MidiDeviceProvider

```java
public MidiDeviceProvider()
```

============ METHOD DETAIL ==========

- Method Detail

- isDeviceSupported

```java
public boolean isDeviceSupported​(
MidiDevice.Info
info)
```

Indicates whether the device provider supports the device represented by
the specified device info object.

**Parameters:** info

- an info object that describes the device for which support
is queried
**Returns:** true

if the specified device is supported, otherwise

false
**Throws:** NullPointerException

- if

info

is

null

- getDeviceInfo

```java
public abstract
MidiDevice.Info
[] getDeviceInfo()
```

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

**Returns:** set of device info objects

- getDevice

```java
public abstract
MidiDevice
getDevice​(
MidiDevice.Info
info)
```

Obtains an instance of the device represented by the info object.

**Parameters:** info

- an info object that describes the desired device
**Returns:** device instance
**Throws:** IllegalArgumentException

- if the info object specified does not
match the info object for a device supported by this

MidiDeviceProvider
**Throws:** NullPointerException

- if

info

is

null

Constructor Detail

- MidiDeviceProvider

```java
public MidiDeviceProvider()
```

---

#### Constructor Detail

MidiDeviceProvider

```java
public MidiDeviceProvider()
```

---

#### MidiDeviceProvider

public MidiDeviceProvider()

Method Detail

- isDeviceSupported

```java
public boolean isDeviceSupported​(
MidiDevice.Info
info)
```

Indicates whether the device provider supports the device represented by
the specified device info object.

**Parameters:** info

- an info object that describes the device for which support
is queried
**Returns:** true

if the specified device is supported, otherwise

false
**Throws:** NullPointerException

- if

info

is

null

- getDeviceInfo

```java
public abstract
MidiDevice.Info
[] getDeviceInfo()
```

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

**Returns:** set of device info objects

- getDevice

```java
public abstract
MidiDevice
getDevice​(
MidiDevice.Info
info)
```

Obtains an instance of the device represented by the info object.

**Parameters:** info

- an info object that describes the desired device
**Returns:** device instance
**Throws:** IllegalArgumentException

- if the info object specified does not
match the info object for a device supported by this

MidiDeviceProvider
**Throws:** NullPointerException

- if

info

is

null

---

#### Method Detail

isDeviceSupported

```java
public boolean isDeviceSupported​(
MidiDevice.Info
info)
```

Indicates whether the device provider supports the device represented by
the specified device info object.

**Parameters:** info

- an info object that describes the device for which support
is queried
**Returns:** true

if the specified device is supported, otherwise

false
**Throws:** NullPointerException

- if

info

is

null

---

#### isDeviceSupported

public boolean isDeviceSupported​(

MidiDevice.Info

info)

Indicates whether the device provider supports the device represented by
the specified device info object.

getDeviceInfo

```java
public abstract
MidiDevice.Info
[] getDeviceInfo()
```

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

**Returns:** set of device info objects

---

#### getDeviceInfo

public abstract

MidiDevice.Info

[] getDeviceInfo()

Obtains the set of info objects representing the device or devices
provided by this

MidiDeviceProvider

.

getDevice

```java
public abstract
MidiDevice
getDevice​(
MidiDevice.Info
info)
```

Obtains an instance of the device represented by the info object.

**Parameters:** info

- an info object that describes the desired device
**Returns:** device instance
**Throws:** IllegalArgumentException

- if the info object specified does not
match the info object for a device supported by this

MidiDeviceProvider
**Throws:** NullPointerException

- if

info

is

null

---

#### getDevice

public abstract

MidiDevice

getDevice​(

MidiDevice.Info

info)

Obtains an instance of the device represented by the info object.

---

