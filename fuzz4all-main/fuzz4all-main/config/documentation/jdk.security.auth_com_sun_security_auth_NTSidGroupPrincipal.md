# Class NTSidGroupPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\NTSidGroupPrincipal.html`

### Class Description

```java
public class
NTSidGroupPrincipal

extends
NTSid
```

This class extends

NTSid

and represents one of the groups to which a Windows NT user belongs.

Principals such as this

NTSidGroupPrincipal

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

#### public NTSidGroupPrincipal​(
String
name)

Create an

NTSidGroupPrincipal

with a Windows NT group name.

**Parameters:**
- name

- the Windows NT group SID for this user.

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

NTSidGroupPrincipal

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

NTSidGroupPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTSidGroupPrincipal

for equality. Returns true if the given object is also a

NTSidGroupPrincipal

and the two NTSidGroupPrincipals
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

NTSidGroupPrincipal

.

**Returns:**
- true if the specified Object is equal to this

NTSidGroupPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class NTSidGroupPrincipal

java.lang.Object

- com.sun.security.auth.NTSid
- - com.sun.security.auth.NTSidGroupPrincipal

com.sun.security.auth.NTSid

- com.sun.security.auth.NTSidGroupPrincipal

com.sun.security.auth.NTSidGroupPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
NTSidGroupPrincipal

extends
NTSid
```

This class extends

NTSid

and represents one of the groups to which a Windows NT user belongs.

Principals such as this

NTSidGroupPrincipal

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

NTSid

,

Serialized Form

public class

NTSidGroupPrincipal

extends

NTSid

This class extends

NTSid

and represents one of the groups to which a Windows NT user belongs.

Principals such as this

NTSidGroupPrincipal

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

NTSidGroupPrincipal

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

NTSidGroupPrincipal

​(

String

name)

Create an

NTSidGroupPrincipal

with a Windows NT group name.

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

NTSidGroupPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidGroupPrincipal

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

NTSidGroupPrincipal

​(

String

name)

Create an

NTSidGroupPrincipal

with a Windows NT group name.

---

#### Constructor Summary

Create an

NTSidGroupPrincipal

with a Windows NT group name.

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

NTSidGroupPrincipal

for equality.

String

toString

()

Return a string representation of this

NTSidGroupPrincipal

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

NTSidGroupPrincipal

for equality.

Return a string representation of this

NTSidGroupPrincipal

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

- NTSidGroupPrincipal

```java
public NTSidGroupPrincipal​(
String
name)
```

Create an

NTSidGroupPrincipal

with a Windows NT group name.

**Parameters:** name

- the Windows NT group SID for this user.
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

NTSidGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidGroupPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidGroupPrincipal

for equality. Returns true if the given object is also a

NTSidGroupPrincipal

and the two NTSidGroupPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidGroupPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- NTSidGroupPrincipal

```java
public NTSidGroupPrincipal​(
String
name)
```

Create an

NTSidGroupPrincipal

with a Windows NT group name.

**Parameters:** name

- the Windows NT group SID for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

NTSidGroupPrincipal

```java
public NTSidGroupPrincipal​(
String
name)
```

Create an

NTSidGroupPrincipal

with a Windows NT group name.

**Parameters:** name

- the Windows NT group SID for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### NTSidGroupPrincipal

public NTSidGroupPrincipal​(

String

name)

Create an

NTSidGroupPrincipal

with a Windows NT group name.

Method Detail

- toString

```java
public
String
toString()
```

Return a string representation of this

NTSidGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidGroupPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidGroupPrincipal

for equality. Returns true if the given object is also a

NTSidGroupPrincipal

and the two NTSidGroupPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidGroupPrincipal

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

NTSidGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

NTSid
**Returns:** a string representation of this

NTSidGroupPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

NTSidGroupPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTSidGroupPrincipal

for equality. Returns true if the given object is also a

NTSidGroupPrincipal

and the two NTSidGroupPrincipals
have the same SID.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

NTSid
**Parameters:** o

- Object to be compared for equality with this

NTSidGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

NTSidGroupPrincipal

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

NTSidGroupPrincipal

for equality. Returns true if the given object is also a

NTSidGroupPrincipal

and the two NTSidGroupPrincipals
have the same SID.

---

