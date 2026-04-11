# Class MidiDevice.Info

**Source:** `java.desktop\javax\sound\midi\MidiDevice.Info.html`

### Class Description

```java
public static class
MidiDevice.Info

extends
Object
```

A

MidiDevice.Info

object contains assorted data about a

MidiDevice

, including its name, the company who created it, and
descriptive text.

**Enclosing interface:** MidiDevice

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Info​(
String
name,

String
vendor,

String
description,

String
version)

Constructs a device info object.

**Parameters:**
- name

- the name of the device
- vendor

- the name of the company who provides the device
- description

- a description of the device
- version

- version information for the device

---

### Method Details

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare

**Returns:**
- true

if the specified object is equal to this info
object;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this info object.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this info object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final
String
getName()

Obtains the name of the device.

**Returns:**
- a string containing the device's name

---

#### public final
String
getVendor()

Obtains the name of the company who supplies the device.

**Returns:**
- device the vendor's name

---

#### public final
String
getDescription()

Obtains the description of the device.

**Returns:**
- a description of the device

---

#### public final
String
getVersion()

Obtains the version of the device.

**Returns:**
- textual version information for the device

---

#### public final
String
toString()

Provides a string representation of the device information.

**Overrides:**
- toString

in class

Object

**Returns:**
- a description of the info object

---

### Additional Sections

#### Class MidiDevice.Info

java.lang.Object

- javax.sound.midi.MidiDevice.Info

javax.sound.midi.MidiDevice.Info

**Enclosing interface:** MidiDevice

```java
public static class
MidiDevice.Info

extends
Object
```

A

MidiDevice.Info

object contains assorted data about a

MidiDevice

, including its name, the company who created it, and
descriptive text.

**See Also:** MidiDevice.getDeviceInfo()

public static class

MidiDevice.Info

extends

Object

A

MidiDevice.Info

object contains assorted data about a

MidiDevice

, including its name, the company who created it, and
descriptive text.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Info

​(

String

name,

String

vendor,

String

description,

String

version)

Constructs a device info object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

String

getDescription

()

Obtains the description of the device.

String

getName

()

Obtains the name of the device.

String

getVendor

()

Obtains the name of the company who supplies the device.

String

getVersion

()

Obtains the version of the device.

int

hashCode

()

Returns a hash code value for this info object.

String

toString

()

Provides a string representation of the device information.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Info

​(

String

name,

String

vendor,

String

description,

String

version)

Constructs a device info object.

---

#### Constructor Summary

Constructs a device info object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

String

getDescription

()

Obtains the description of the device.

String

getName

()

Obtains the name of the device.

String

getVendor

()

Obtains the name of the company who supplies the device.

String

getVersion

()

Obtains the version of the device.

int

hashCode

()

Returns a hash code value for this info object.

String

toString

()

Provides a string representation of the device information.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

Obtains the description of the device.

Obtains the name of the device.

Obtains the name of the company who supplies the device.

Obtains the version of the device.

Returns a hash code value for this info object.

Provides a string representation of the device information.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- Info

```java
protected Info​(
String
name,

String
vendor,

String
description,

String
version)
```

Constructs a device info object.

**Parameters:** name

- the name of the device
**Parameters:** vendor

- the name of the company who provides the device
**Parameters:** description

- a description of the device
**Parameters:** version

- version information for the device

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this info
object;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this info object.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this info object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getName

```java
public final
String
getName()
```

Obtains the name of the device.

**Returns:** a string containing the device's name

- getVendor

```java
public final
String
getVendor()
```

Obtains the name of the company who supplies the device.

**Returns:** device the vendor's name

- getDescription

```java
public final
String
getDescription()
```

Obtains the description of the device.

**Returns:** a description of the device

- getVersion

```java
public final
String
getVersion()
```

Obtains the version of the device.

**Returns:** textual version information for the device

- toString

```java
public final
String
toString()
```

Provides a string representation of the device information.

**Overrides:** toString

in class

Object
**Returns:** a description of the info object

Constructor Detail

- Info

```java
protected Info​(
String
name,

String
vendor,

String
description,

String
version)
```

Constructs a device info object.

**Parameters:** name

- the name of the device
**Parameters:** vendor

- the name of the company who provides the device
**Parameters:** description

- a description of the device
**Parameters:** version

- version information for the device

---

#### Constructor Detail

Info

```java
protected Info​(
String
name,

String
vendor,

String
description,

String
version)
```

Constructs a device info object.

**Parameters:** name

- the name of the device
**Parameters:** vendor

- the name of the company who provides the device
**Parameters:** description

- a description of the device
**Parameters:** version

- version information for the device

---

#### Info

protected Info​(

String

name,

String

vendor,

String

description,

String

version)

Constructs a device info object.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this info
object;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this info object.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this info object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getName

```java
public final
String
getName()
```

Obtains the name of the device.

**Returns:** a string containing the device's name

- getVendor

```java
public final
String
getVendor()
```

Obtains the name of the company who supplies the device.

**Returns:** device the vendor's name

- getDescription

```java
public final
String
getDescription()
```

Obtains the description of the device.

**Returns:** a description of the device

- getVersion

```java
public final
String
getVersion()
```

Obtains the version of the device.

**Returns:** textual version information for the device

- toString

```java
public final
String
toString()
```

Provides a string representation of the device information.

**Overrides:** toString

in class

Object
**Returns:** a description of the info object

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this info
object;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this info object.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this info object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this info object.

getName

```java
public final
String
getName()
```

Obtains the name of the device.

**Returns:** a string containing the device's name

---

#### getName

public final

String

getName()

Obtains the name of the device.

getVendor

```java
public final
String
getVendor()
```

Obtains the name of the company who supplies the device.

**Returns:** device the vendor's name

---

#### getVendor

public final

String

getVendor()

Obtains the name of the company who supplies the device.

getDescription

```java
public final
String
getDescription()
```

Obtains the description of the device.

**Returns:** a description of the device

---

#### getDescription

public final

String

getDescription()

Obtains the description of the device.

getVersion

```java
public final
String
getVersion()
```

Obtains the version of the device.

**Returns:** textual version information for the device

---

#### getVersion

public final

String

getVersion()

Obtains the version of the device.

toString

```java
public final
String
toString()
```

Provides a string representation of the device information.

**Overrides:** toString

in class

Object
**Returns:** a description of the info object

---

#### toString

public final

String

toString()

Provides a string representation of the device information.

---

