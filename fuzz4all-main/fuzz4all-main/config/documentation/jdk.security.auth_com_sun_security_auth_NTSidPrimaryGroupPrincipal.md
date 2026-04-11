# Class NTSidPrimaryGroupPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\NTSidPrimaryGroupPrincipal.html`

### Class Description

```java
public class
NTSidPrimaryGroupPrincipal

extends
NTSid
```

This class extends

NTSid

and represents a Windows NT user's primary group SID.

Principals such as this

NTSidPrimaryGroupPrincipal

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

#### public NTSidPrimaryGroupPrincipal​(
String
name)

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

**Parameters:**
- name

- the primary Windows NT group SID for this user.

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

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTSidPrimaryGroupPrincipal

for equality. Returns true if the given object is also a

NTSidPrimaryGroupPrincipal

and the two
NTSidPrimaryGroupPrincipals have the same SID.

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

NTSidPrimaryGroupPrincipal

.

**Returns:**
- true if the specified Object is equal to this

NTSidPrimaryGroupPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class NTSidPrimaryGroupPrincipal

java.lang.Object

- com.sun.security.auth.NTSid
- - com.sun.security.auth.NTSidPrimaryGroupPrincipal

com.sun.security.auth.NTSid

- com.sun.security.auth.NTSidPrimaryGroupPrincipal

com.sun.security.auth.NTSidPrimaryGroupPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
NTSidPrimaryGroupPrincipal

extends
NTSid
```

This class extends

NTSid

and represents a Windows NT user's primary group SID.

Principals such as this

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

extends

NTSid

This class extends

NTSid

and represents a Windows NT user's primary group SID.

Principals such as this

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

​(

String

name)

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

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

NTSidPrimaryGroupPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

​(

String

name)

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

---

#### Constructor Summary

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

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

NTSidPrimaryGroupPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

for equality.

Return a string representation of this

NTSidPrimaryGroupPrincipal

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

- NTSidPrimaryGroupPrincipal

```java
public NTSidPrimaryGroupPrincipal​(
String
name)
```

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

**Parameters:** name

- the primary Windows NT group SID for this user.
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

NTSidPrimaryGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidPrimaryGroupPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidPrimaryGroupPrincipal

for equality. Returns true if the given object is also a

NTSidPrimaryGroupPrincipal

and the two
NTSidPrimaryGroupPrincipals have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidPrimaryGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidPrimaryGroupPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- NTSidPrimaryGroupPrincipal

```java
public NTSidPrimaryGroupPrincipal​(
String
name)
```

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

**Parameters:** name

- the primary Windows NT group SID for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

NTSidPrimaryGroupPrincipal

```java
public NTSidPrimaryGroupPrincipal​(
String
name)
```

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

**Parameters:** name

- the primary Windows NT group SID for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### NTSidPrimaryGroupPrincipal

public NTSidPrimaryGroupPrincipal​(

String

name)

Create an

NTSidPrimaryGroupPrincipal

with a Windows NT
group SID.

Method Detail

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSidPrimaryGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidPrimaryGroupPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidPrimaryGroupPrincipal

for equality. Returns true if the given object is also a

NTSidPrimaryGroupPrincipal

and the two
NTSidPrimaryGroupPrincipals have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidPrimaryGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidPrimaryGroupPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

NTSidPrimaryGroupPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidPrimaryGroupPrincipal

for equality. Returns true if the given object is also a

NTSidPrimaryGroupPrincipal

and the two
NTSidPrimaryGroupPrincipals have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidPrimaryGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidPrimaryGroupPrincipal

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

NTSidPrimaryGroupPrincipal

for equality. Returns true if the given object is also a

NTSidPrimaryGroupPrincipal

and the two
NTSidPrimaryGroupPrincipals have the same SID.

---

