# Class Mixer.Info

**Source:** `java.desktop\javax\sound\sampled\Mixer.Info.html`

### Class Description

```java
public static class
Mixer.Info

extends
Object
```

The

Mixer.Info

class represents information about an audio mixer,
including the product's name, version, and vendor, along with a textual
description. This information may be retrieved through the

getMixerInfo

method of the

Mixer

interface.

**Enclosing interface:** Mixer

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

Constructs a mixer's info object, passing it the given textual
information.

**Parameters:**
- name

- the name of the mixer
- vendor

- the company who manufactures or creates the hardware
or software mixer
- description

- descriptive text about the mixer
- version

- version information for the mixer

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

Obtains the name of the mixer.

**Returns:**
- a string that names the mixer

---

#### public final
String
getVendor()

Obtains the vendor of the mixer.

**Returns:**
- a string that names the mixer's vendor

---

#### public final
String
getDescription()

Obtains the description of the mixer.

**Returns:**
- a textual description of the mixer

---

#### public final
String
getVersion()

Obtains the version of the mixer.

**Returns:**
- textual version information for the mixer

---

#### public final
String
toString()

Provides a string representation of the mixer info.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string describing the info object

---

### Additional Sections

#### Class Mixer.Info

java.lang.Object

- javax.sound.sampled.Mixer.Info

javax.sound.sampled.Mixer.Info

**Enclosing interface:** Mixer

```java
public static class
Mixer.Info

extends
Object
```

The

Mixer.Info

class represents information about an audio mixer,
including the product's name, version, and vendor, along with a textual
description. This information may be retrieved through the

getMixerInfo

method of the

Mixer

interface.

**Since:** 1.3

public static class

Mixer.Info

extends

Object

The

Mixer.Info

class represents information about an audio mixer,
including the product's name, version, and vendor, along with a textual
description. This information may be retrieved through the

getMixerInfo

method of the

Mixer

interface.

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

Constructs a mixer's info object, passing it the given textual
information.

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

Obtains the description of the mixer.

String

getName

()

Obtains the name of the mixer.

String

getVendor

()

Obtains the vendor of the mixer.

String

getVersion

()

Obtains the version of the mixer.

int

hashCode

()

Returns a hash code value for this info object.

String

toString

()

Provides a string representation of the mixer info.

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

Constructs a mixer's info object, passing it the given textual
information.

---

#### Constructor Summary

Constructs a mixer's info object, passing it the given textual
information.

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

Obtains the description of the mixer.

String

getName

()

Obtains the name of the mixer.

String

getVendor

()

Obtains the vendor of the mixer.

String

getVersion

()

Obtains the version of the mixer.

int

hashCode

()

Returns a hash code value for this info object.

String

toString

()

Provides a string representation of the mixer info.

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

Obtains the description of the mixer.

Obtains the name of the mixer.

Obtains the vendor of the mixer.

Obtains the version of the mixer.

Returns a hash code value for this info object.

Provides a string representation of the mixer info.

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

Constructs a mixer's info object, passing it the given textual
information.

**Parameters:** name

- the name of the mixer
**Parameters:** vendor

- the company who manufactures or creates the hardware
or software mixer
**Parameters:** description

- descriptive text about the mixer
**Parameters:** version

- version information for the mixer

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

Obtains the name of the mixer.

**Returns:** a string that names the mixer

- getVendor

```java
public final
String
getVendor()
```

Obtains the vendor of the mixer.

**Returns:** a string that names the mixer's vendor

- getDescription

```java
public final
String
getDescription()
```

Obtains the description of the mixer.

**Returns:** a textual description of the mixer

- getVersion

```java
public final
String
getVersion()
```

Obtains the version of the mixer.

**Returns:** textual version information for the mixer

- toString

```java
public final
String
toString()
```

Provides a string representation of the mixer info.

**Overrides:** toString

in class

Object
**Returns:** a string describing the info object

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

Constructs a mixer's info object, passing it the given textual
information.

**Parameters:** name

- the name of the mixer
**Parameters:** vendor

- the company who manufactures or creates the hardware
or software mixer
**Parameters:** description

- descriptive text about the mixer
**Parameters:** version

- version information for the mixer

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

Constructs a mixer's info object, passing it the given textual
information.

**Parameters:** name

- the name of the mixer
**Parameters:** vendor

- the company who manufactures or creates the hardware
or software mixer
**Parameters:** description

- descriptive text about the mixer
**Parameters:** version

- version information for the mixer

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

Constructs a mixer's info object, passing it the given textual
information.

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

Obtains the name of the mixer.

**Returns:** a string that names the mixer

- getVendor

```java
public final
String
getVendor()
```

Obtains the vendor of the mixer.

**Returns:** a string that names the mixer's vendor

- getDescription

```java
public final
String
getDescription()
```

Obtains the description of the mixer.

**Returns:** a textual description of the mixer

- getVersion

```java
public final
String
getVersion()
```

Obtains the version of the mixer.

**Returns:** textual version information for the mixer

- toString

```java
public final
String
toString()
```

Provides a string representation of the mixer info.

**Overrides:** toString

in class

Object
**Returns:** a string describing the info object

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

Obtains the name of the mixer.

**Returns:** a string that names the mixer

---

#### getName

public final

String

getName()

Obtains the name of the mixer.

getVendor

```java
public final
String
getVendor()
```

Obtains the vendor of the mixer.

**Returns:** a string that names the mixer's vendor

---

#### getVendor

public final

String

getVendor()

Obtains the vendor of the mixer.

getDescription

```java
public final
String
getDescription()
```

Obtains the description of the mixer.

**Returns:** a textual description of the mixer

---

#### getDescription

public final

String

getDescription()

Obtains the description of the mixer.

getVersion

```java
public final
String
getVersion()
```

Obtains the version of the mixer.

**Returns:** textual version information for the mixer

---

#### getVersion

public final

String

getVersion()

Obtains the version of the mixer.

toString

```java
public final
String
toString()
```

Provides a string representation of the mixer info.

**Overrides:** toString

in class

Object
**Returns:** a string describing the info object

---

#### toString

public final

String

toString()

Provides a string representation of the mixer info.

---

