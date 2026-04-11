# Class NTSid

**Source:** `jdk.security.auth\com\sun\security\auth\NTSid.html`

### Class Description

```java
public class
NTSid

extends
Object

implements
Principal
,
Serializable
```

This class implements the

Principal

interface
and represents information about a Windows NT user, group or realm.

Windows NT chooses to represent users, groups and realms (or domains)
with not only common names, but also relatively unique numbers. These
numbers are called Security IDentifiers, or SIDs. Windows NT
also provides services that render these SIDs into string forms.
This class represents these string forms.

Principals such as this

NTSid

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information
on how to achieve this. Authorization decisions can then be based upon
the Principals associated with a

Subject

.

**All Implemented Interfaces:** Serializable

,

Principal

---

### Field Details

*No entries found.*

### Constructor Details

#### public NTSid​(
String
stringSid)

Create an

NTSid

with a Windows NT SID.

**Parameters:**
- stringSid

- the Windows NT SID.

**Throws:**
- NullPointerException

- if the

String

is

null

.
- IllegalArgumentException

- if the

String

has zero length.

---

### Method Details

#### public
String
getName()

Return a string version of this

NTSid

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- a string version of this

NTSid

---

#### public
String
toString()

Return a string representation of this

NTSid

.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

NTSid

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTSid

for equality. Returns true if the given object is also a

NTSid

and the two NTSids have the same String
representation.

**Specified by:**
- equals

in interface

Principal

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- Object to be compared for equality with this

NTSid

.

**Returns:**
- true if the specified Object is equal to this

NTSid

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

NTSid

.

**Specified by:**
- hashCode

in interface

Principal

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

NTSid

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class NTSid

java.lang.Object

- com.sun.security.auth.NTSid

com.sun.security.auth.NTSid

**All Implemented Interfaces:** Serializable

,

Principal

**Direct Known Subclasses:** NTSidDomainPrincipal

,

NTSidGroupPrincipal

,

NTSidPrimaryGroupPrincipal

,

NTSidUserPrincipal

```java
public class
NTSid

extends
Object

implements
Principal
,
Serializable
```

This class implements the

Principal

interface
and represents information about a Windows NT user, group or realm.

Windows NT chooses to represent users, groups and realms (or domains)
with not only common names, but also relatively unique numbers. These
numbers are called Security IDentifiers, or SIDs. Windows NT
also provides services that render these SIDs into string forms.
This class represents these string forms.

Principals such as this

NTSid

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information
on how to achieve this. Authorization decisions can then be based upon
the Principals associated with a

Subject

.

**See Also:** Principal

,

Subject

,

Serialized Form

public class

NTSid

extends

Object

implements

Principal

,

Serializable

This class implements the

Principal

interface
and represents information about a Windows NT user, group or realm.

Windows NT chooses to represent users, groups and realms (or domains)
with not only common names, but also relatively unique numbers. These
numbers are called Security IDentifiers, or SIDs. Windows NT
also provides services that render these SIDs into string forms.
This class represents these string forms.

Principals such as this

NTSid

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information
on how to achieve this. Authorization decisions can then be based upon
the Principals associated with a

Subject

.

Windows NT chooses to represent users, groups and realms (or domains)
with not only common names, but also relatively unique numbers. These
numbers are called Security IDentifiers, or SIDs. Windows NT
also provides services that render these SIDs into string forms.
This class represents these string forms.

Principals such as this

NTSid

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information
on how to achieve this. Authorization decisions can then be based upon
the Principals associated with a

Subject

.

Principals such as this

NTSid

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information
on how to achieve this. Authorization decisions can then be based upon
the Principals associated with a

Subject

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NTSid

​(

String

stringSid)

Create an

NTSid

with a Windows NT SID.

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

o)

Compares the specified Object with this

NTSid

for equality.

String

getName

()

Return a string version of this

NTSid

.

int

hashCode

()

Return a hash code for this

NTSid

.

String

toString

()

Return a string representation of this

NTSid

.

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

- Methods declared in interface java.security.

Principal

implies

Constructor Summary

Constructors

Constructor

Description

NTSid

​(

String

stringSid)

Create an

NTSid

with a Windows NT SID.

---

#### Constructor Summary

Create an

NTSid

with a Windows NT SID.

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

o)

Compares the specified Object with this

NTSid

for equality.

String

getName

()

Return a string version of this

NTSid

.

int

hashCode

()

Return a hash code for this

NTSid

.

String

toString

()

Return a string representation of this

NTSid

.

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

- Methods declared in interface java.security.

Principal

implies

---

#### Method Summary

Compares the specified Object with this

NTSid

for equality.

Return a string version of this

NTSid

.

Return a hash code for this

NTSid

.

Return a string representation of this

NTSid

.

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

Methods declared in interface java.security.

Principal

implies

---

#### Methods declared in interface java.security. Principal

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NTSid

```java
public NTSid​(
String
stringSid)
```

Create an

NTSid

with a Windows NT SID.

**Parameters:** stringSid

- the Windows NT SID.
**Throws:** NullPointerException

- if the

String

is

null

.
**Throws:** IllegalArgumentException

- if the

String

has zero length.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Return a string version of this

NTSid

.

**Specified by:** getName

in interface

Principal
**Returns:** a string version of this

NTSid

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSid

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTSid

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSid

for equality. Returns true if the given object is also a

NTSid

and the two NTSids have the same String
representation.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTSid

.
**Returns:** true if the specified Object is equal to this

NTSid

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTSid

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTSid

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- NTSid

```java
public NTSid​(
String
stringSid)
```

Create an

NTSid

with a Windows NT SID.

**Parameters:** stringSid

- the Windows NT SID.
**Throws:** NullPointerException

- if the

String

is

null

.
**Throws:** IllegalArgumentException

- if the

String

has zero length.

---

#### Constructor Detail

NTSid

```java
public NTSid​(
String
stringSid)
```

Create an

NTSid

with a Windows NT SID.

**Parameters:** stringSid

- the Windows NT SID.
**Throws:** NullPointerException

- if the

String

is

null

.
**Throws:** IllegalArgumentException

- if the

String

has zero length.

---

#### NTSid

public NTSid​(

String

stringSid)

Create an

NTSid

with a Windows NT SID.

Method Detail

- getName

```java
public
String
getName()
```

Return a string version of this

NTSid

.

**Specified by:** getName

in interface

Principal
**Returns:** a string version of this

NTSid

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSid

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTSid

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSid

for equality. Returns true if the given object is also a

NTSid

and the two NTSids have the same String
representation.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTSid

.
**Returns:** true if the specified Object is equal to this

NTSid

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTSid

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTSid

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getName

```java
public
String
getName()
```

Return a string version of this

NTSid

.

**Specified by:** getName

in interface

Principal
**Returns:** a string version of this

NTSid

---

#### getName

public

String

getName()

Return a string version of this

NTSid

.

toString

```java
public
String
toString()
```

Return a string representation of this

NTSid

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTSid

.

---

#### toString

public

String

toString()

Return a string representation of this

NTSid

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSid

for equality. Returns true if the given object is also a

NTSid

and the two NTSids have the same String
representation.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTSid

.
**Returns:** true if the specified Object is equal to this

NTSid

.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares the specified Object with this

NTSid

for equality. Returns true if the given object is also a

NTSid

and the two NTSids have the same String
representation.

hashCode

```java
public int hashCode()
```

Return a hash code for this

NTSid

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTSid

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

NTSid

.

---

