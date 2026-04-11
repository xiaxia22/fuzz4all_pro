# Class NTSidDomainPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\NTSidDomainPrincipal.html`

### Class Description

```java
public class
NTSidDomainPrincipal

extends
NTSid
```

This class extends

NTSid

and represents a Windows NT user's domain SID.

An NT user only has a domain SID if in fact they are logged
into an NT domain. If the user is logged into a workgroup or
just a standalone configuration, they will NOT have a domain SID.

Principals such as this

NTSidDomainPrincipal

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

#### public NTSidDomainPrincipal​(
String
name)

Create an

NTSidDomainPrincipal

with a Windows NT SID.

**Parameters:**
- name

- a string version of the Windows NT SID for this
user's domain.

**Throws:**
- NullPointerException

- if the

name

is

null

.

---

### Method Details

#### public
String
toString()

Return a string representation of this

NTSidDomainPrincipal

.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

NTSid

**Returns:**
- a string representation of this

NTSidDomainPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTSidDomainPrincipal

for equality. Returns true if the given object is also a

NTSidDomainPrincipal

and the two NTSidDomainPrincipals
have the same SID.

**Specified by:**
- equals

in interface

Principal

**Overrides:**
- equals

in class

NTSid

**Parameters:**
- o

- Object to be compared for equality with this

NTSidDomainPrincipal

.

**Returns:**
- true if the specified Object is equal to this

NTSidDomainPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class NTSidDomainPrincipal

java.lang.Object

- com.sun.security.auth.NTSid
- - com.sun.security.auth.NTSidDomainPrincipal

com.sun.security.auth.NTSid

- com.sun.security.auth.NTSidDomainPrincipal

com.sun.security.auth.NTSidDomainPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
NTSidDomainPrincipal

extends
NTSid
```

This class extends

NTSid

and represents a Windows NT user's domain SID.

An NT user only has a domain SID if in fact they are logged
into an NT domain. If the user is logged into a workgroup or
just a standalone configuration, they will NOT have a domain SID.

Principals such as this

NTSidDomainPrincipal

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

NTSidDomainPrincipal

extends

NTSid

This class extends

NTSid

and represents a Windows NT user's domain SID.

An NT user only has a domain SID if in fact they are logged
into an NT domain. If the user is logged into a workgroup or
just a standalone configuration, they will NOT have a domain SID.

Principals such as this

NTSidDomainPrincipal

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

An NT user only has a domain SID if in fact they are logged
into an NT domain. If the user is logged into a workgroup or
just a standalone configuration, they will NOT have a domain SID.

Principals such as this

NTSidDomainPrincipal

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

NTSidDomainPrincipal

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

NTSidDomainPrincipal

​(

String

name)

Create an

NTSidDomainPrincipal

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

NTSidDomainPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidDomainPrincipal

.

- Methods declared in class com.sun.security.auth.

NTSid

getName

,

hashCode

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

NTSidDomainPrincipal

​(

String

name)

Create an

NTSidDomainPrincipal

with a Windows NT SID.

---

#### Constructor Summary

Create an

NTSidDomainPrincipal

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

NTSidDomainPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidDomainPrincipal

.

- Methods declared in class com.sun.security.auth.

NTSid

getName

,

hashCode

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

NTSidDomainPrincipal

for equality.

Return a string representation of this

NTSidDomainPrincipal

.

Methods declared in class com.sun.security.auth.

NTSid

getName

,

hashCode

---

#### Methods declared in class com.sun.security.auth. NTSid

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

- NTSidDomainPrincipal

```java
public NTSidDomainPrincipal​(
String
name)
```

Create an

NTSidDomainPrincipal

with a Windows NT SID.

**Parameters:** name

- a string version of the Windows NT SID for this
user's domain.
**Throws:** NullPointerException

- if the

name

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSidDomainPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidDomainPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidDomainPrincipal

for equality. Returns true if the given object is also a

NTSidDomainPrincipal

and the two NTSidDomainPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidDomainPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidDomainPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- NTSidDomainPrincipal

```java
public NTSidDomainPrincipal​(
String
name)
```

Create an

NTSidDomainPrincipal

with a Windows NT SID.

**Parameters:** name

- a string version of the Windows NT SID for this
user's domain.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

NTSidDomainPrincipal

```java
public NTSidDomainPrincipal​(
String
name)
```

Create an

NTSidDomainPrincipal

with a Windows NT SID.

**Parameters:** name

- a string version of the Windows NT SID for this
user's domain.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### NTSidDomainPrincipal

public NTSidDomainPrincipal​(

String

name)

Create an

NTSidDomainPrincipal

with a Windows NT SID.

Method Detail

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSidDomainPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidDomainPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidDomainPrincipal

for equality. Returns true if the given object is also a

NTSidDomainPrincipal

and the two NTSidDomainPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidDomainPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidDomainPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

toString

```java
public
String
toString()
```

Return a string representation of this

NTSidDomainPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidDomainPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

NTSidDomainPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidDomainPrincipal

for equality. Returns true if the given object is also a

NTSidDomainPrincipal

and the two NTSidDomainPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidDomainPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidDomainPrincipal

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

NTSidDomainPrincipal

for equality. Returns true if the given object is also a

NTSidDomainPrincipal

and the two NTSidDomainPrincipals
have the same SID.

---

