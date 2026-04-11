# Class NTSidUserPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\NTSidUserPrincipal.html`

### Class Description

```java
public class
NTSidUserPrincipal

extends
NTSid
```

This class extends

NTSid

and represents a Windows NT user's SID.

Principals such as this

NTSidUserPrincipal

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

#### public NTSidUserPrincipal​(
String
name)

Create an

NTSidUserPrincipal

with a Windows NT SID.

**Parameters:**
- name

- a string version of the Windows NT SID for this user.

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

NTSidUserPrincipal

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

NTSidUserPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTSidUserPrincipal

for equality. Returns true if the given object is also a

NTSidUserPrincipal

and the two NTSidUserPrincipals
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

NTSidUserPrincipal

.

**Returns:**
- true if the specified Object is equal to this

NTSidUserPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class NTSidUserPrincipal

java.lang.Object

- com.sun.security.auth.NTSid
- - com.sun.security.auth.NTSidUserPrincipal

com.sun.security.auth.NTSid

- com.sun.security.auth.NTSidUserPrincipal

com.sun.security.auth.NTSidUserPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
NTSidUserPrincipal

extends
NTSid
```

This class extends

NTSid

and represents a Windows NT user's SID.

Principals such as this

NTSidUserPrincipal

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

NTSidUserPrincipal

extends

NTSid

This class extends

NTSid

and represents a Windows NT user's SID.

Principals such as this

NTSidUserPrincipal

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

NTSidUserPrincipal

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

NTSidUserPrincipal

​(

String

name)

Create an

NTSidUserPrincipal

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

NTSidUserPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidUserPrincipal

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

NTSidUserPrincipal

​(

String

name)

Create an

NTSidUserPrincipal

with a Windows NT SID.

---

#### Constructor Summary

Create an

NTSidUserPrincipal

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

NTSidUserPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidUserPrincipal

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

NTSidUserPrincipal

for equality.

Return a string representation of this

NTSidUserPrincipal

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

- NTSidUserPrincipal

```java
public NTSidUserPrincipal​(
String
name)
```

Create an

NTSidUserPrincipal

with a Windows NT SID.

**Parameters:** name

- a string version of the Windows NT SID for this user.
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

NTSidUserPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidUserPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidUserPrincipal

for equality. Returns true if the given object is also a

NTSidUserPrincipal

and the two NTSidUserPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidUserPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidUserPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- NTSidUserPrincipal

```java
public NTSidUserPrincipal​(
String
name)
```

Create an

NTSidUserPrincipal

with a Windows NT SID.

**Parameters:** name

- a string version of the Windows NT SID for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

NTSidUserPrincipal

```java
public NTSidUserPrincipal​(
String
name)
```

Create an

NTSidUserPrincipal

with a Windows NT SID.

**Parameters:** name

- a string version of the Windows NT SID for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### NTSidUserPrincipal

public NTSidUserPrincipal​(

String

name)

Create an

NTSidUserPrincipal

with a Windows NT SID.

Method Detail

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSidUserPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidUserPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidUserPrincipal

for equality. Returns true if the given object is also a

NTSidUserPrincipal

and the two NTSidUserPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidUserPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidUserPrincipal

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

NTSidUserPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidUserPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

NTSidUserPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidUserPrincipal

for equality. Returns true if the given object is also a

NTSidUserPrincipal

and the two NTSidUserPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidUserPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidUserPrincipal

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

NTSidUserPrincipal

for equality. Returns true if the given object is also a

NTSidUserPrincipal

and the two NTSidUserPrincipals
have the same SID.

---

