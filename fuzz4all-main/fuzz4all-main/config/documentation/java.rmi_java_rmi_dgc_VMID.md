# Class VMID

**Source:** `java.rmi\java\rmi\dgc\VMID.html`

### Class Description

```java
public final class
VMID

extends
Object

implements
Serializable
```

A VMID is a identifier that is unique across all Java virtual
machines. VMIDs are used by the distributed garbage collector
to identify client VMs.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public VMID()

Create a new VMID. Each new VMID returned from this constructor
is unique for all Java virtual machines under the following
conditions: a) the conditions for uniqueness for objects of
the class

java.rmi.server.UID

are satisfied, and b) an
address can be obtained for this host that is unique and constant
for the lifetime of this object.

---

### Method Details

#### @Deprecated

public static boolean isUnique()

Return true if an accurate address can be determined for this
host. If false, reliable VMID cannot be generated from this host

**Returns:**
- true if host address can be determined, false otherwise

---

#### public int hashCode()

Compute hash code for this VMID.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compare this VMID to another, and return true if they are the
same identifier.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Return string representation of this VMID.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class VMID

java.lang.Object

- java.rmi.dgc.VMID

java.rmi.dgc.VMID

**All Implemented Interfaces:** Serializable

```java
public final class
VMID

extends
Object

implements
Serializable
```

A VMID is a identifier that is unique across all Java virtual
machines. VMIDs are used by the distributed garbage collector
to identify client VMs.

**See Also:** Serialized Form

public final class

VMID

extends

Object

implements

Serializable

A VMID is a identifier that is unique across all Java virtual
machines. VMIDs are used by the distributed garbage collector
to identify client VMs.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VMID

()

Create a new VMID.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compare this VMID to another, and return true if they are the
same identifier.

int

hashCode

()

Compute hash code for this VMID.

static boolean

isUnique

()

Deprecated.

String

toString

()

Return string representation of this VMID.

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

Constructor

Description

VMID

()

Create a new VMID.

---

#### Constructor Summary

Create a new VMID.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compare this VMID to another, and return true if they are the
same identifier.

int

hashCode

()

Compute hash code for this VMID.

static boolean

isUnique

()

Deprecated.

String

toString

()

Return string representation of this VMID.

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

Compare this VMID to another, and return true if they are the
same identifier.

Compute hash code for this VMID.

Deprecated.

Return string representation of this VMID.

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

- VMID

```java
public VMID()
```

Create a new VMID. Each new VMID returned from this constructor
is unique for all Java virtual machines under the following
conditions: a) the conditions for uniqueness for objects of
the class

java.rmi.server.UID

are satisfied, and b) an
address can be obtained for this host that is unique and constant
for the lifetime of this object.

============ METHOD DETAIL ==========

- Method Detail

- isUnique

```java
@Deprecated

public static boolean isUnique()
```

Deprecated.

Return true if an accurate address can be determined for this
host. If false, reliable VMID cannot be generated from this host

**Returns:** true if host address can be determined, false otherwise

- hashCode

```java
public int hashCode()
```

Compute hash code for this VMID.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compare this VMID to another, and return true if they are the
same identifier.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Return string representation of this VMID.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- VMID

```java
public VMID()
```

Create a new VMID. Each new VMID returned from this constructor
is unique for all Java virtual machines under the following
conditions: a) the conditions for uniqueness for objects of
the class

java.rmi.server.UID

are satisfied, and b) an
address can be obtained for this host that is unique and constant
for the lifetime of this object.

---

#### Constructor Detail

VMID

```java
public VMID()
```

Create a new VMID. Each new VMID returned from this constructor
is unique for all Java virtual machines under the following
conditions: a) the conditions for uniqueness for objects of
the class

java.rmi.server.UID

are satisfied, and b) an
address can be obtained for this host that is unique and constant
for the lifetime of this object.

---

#### VMID

public VMID()

Create a new VMID. Each new VMID returned from this constructor
is unique for all Java virtual machines under the following
conditions: a) the conditions for uniqueness for objects of
the class

java.rmi.server.UID

are satisfied, and b) an
address can be obtained for this host that is unique and constant
for the lifetime of this object.

Method Detail

- isUnique

```java
@Deprecated

public static boolean isUnique()
```

Deprecated.

Return true if an accurate address can be determined for this
host. If false, reliable VMID cannot be generated from this host

**Returns:** true if host address can be determined, false otherwise

- hashCode

```java
public int hashCode()
```

Compute hash code for this VMID.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compare this VMID to another, and return true if they are the
same identifier.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Return string representation of this VMID.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

isUnique

```java
@Deprecated

public static boolean isUnique()
```

Deprecated.

Return true if an accurate address can be determined for this
host. If false, reliable VMID cannot be generated from this host

**Returns:** true if host address can be determined, false otherwise

---

#### isUnique

@Deprecated

public static boolean isUnique()

Return true if an accurate address can be determined for this
host. If false, reliable VMID cannot be generated from this host

hashCode

```java
public int hashCode()
```

Compute hash code for this VMID.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Compute hash code for this VMID.

equals

```java
public boolean equals​(
Object
obj)
```

Compare this VMID to another, and return true if they are the
same identifier.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compare this VMID to another, and return true if they are the
same identifier.

toString

```java
public
String
toString()
```

Return string representation of this VMID.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Return string representation of this VMID.

---

