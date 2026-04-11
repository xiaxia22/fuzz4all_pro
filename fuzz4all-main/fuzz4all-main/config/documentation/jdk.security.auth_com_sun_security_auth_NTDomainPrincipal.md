# Class NTDomainPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\NTDomainPrincipal.html`

### Class Description

```java
public class
NTDomainPrincipal

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
and represents the name of the Windows NT domain into which the
user authenticated. This will be a domain name if the user logged
into a Windows NT domain, a workgroup name if the user logged into
a workgroup, or a machine name if the user logged into a standalone
configuration.

Principals such as this

NTDomainPrincipal

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

#### public NTDomainPrincipal​(
String
name)

Create an

NTDomainPrincipal

with a Windows NT domain name.

**Parameters:**
- name

- the Windows NT domain name for this user.

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
getName()

Return the Windows NT domain name for this

NTDomainPrincipal

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the Windows NT domain name for this

NTDomainPrincipal

---

#### public
String
toString()

Return a string representation of this

NTDomainPrincipal

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

NTDomainPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTDomainPrincipal

for equality. Returns true if the given object is also a

NTDomainPrincipal

and the two NTDomainPrincipals
have the same name.

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

NTDomainPrincipal

.

**Returns:**
- true if the specified Object is equal to this

NTDomainPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

NTDomainPrincipal

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

NTDomainPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class NTDomainPrincipal

java.lang.Object

- com.sun.security.auth.NTDomainPrincipal

com.sun.security.auth.NTDomainPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
NTDomainPrincipal

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
and represents the name of the Windows NT domain into which the
user authenticated. This will be a domain name if the user logged
into a Windows NT domain, a workgroup name if the user logged into
a workgroup, or a machine name if the user logged into a standalone
configuration.

Principals such as this

NTDomainPrincipal

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

NTDomainPrincipal

extends

Object

implements

Principal

,

Serializable

This class implements the

Principal

interface
and represents the name of the Windows NT domain into which the
user authenticated. This will be a domain name if the user logged
into a Windows NT domain, a workgroup name if the user logged into
a workgroup, or a machine name if the user logged into a standalone
configuration.

Principals such as this

NTDomainPrincipal

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

NTDomainPrincipal

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

NTDomainPrincipal

​(

String

name)

Create an

NTDomainPrincipal

with a Windows NT domain name.

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

NTDomainPrincipal

for equality.

String

getName

()

Return the Windows NT domain name for this

NTDomainPrincipal

.

int

hashCode

()

Return a hash code for this

NTDomainPrincipal

.

String

toString

()

Return a string representation of this

NTDomainPrincipal

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

NTDomainPrincipal

​(

String

name)

Create an

NTDomainPrincipal

with a Windows NT domain name.

---

#### Constructor Summary

Create an

NTDomainPrincipal

with a Windows NT domain name.

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

NTDomainPrincipal

for equality.

String

getName

()

Return the Windows NT domain name for this

NTDomainPrincipal

.

int

hashCode

()

Return a hash code for this

NTDomainPrincipal

.

String

toString

()

Return a string representation of this

NTDomainPrincipal

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

NTDomainPrincipal

for equality.

Return the Windows NT domain name for this

NTDomainPrincipal

.

Return a hash code for this

NTDomainPrincipal

.

Return a string representation of this

NTDomainPrincipal

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

- NTDomainPrincipal

```java
public NTDomainPrincipal​(
String
name)
```

Create an

NTDomainPrincipal

with a Windows NT domain name.

**Parameters:** name

- the Windows NT domain name for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Return the Windows NT domain name for this

NTDomainPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Windows NT domain name for this

NTDomainPrincipal

- toString

```java
public
String
toString()
```

Return a string representation of this

NTDomainPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTDomainPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTDomainPrincipal

for equality. Returns true if the given object is also a

NTDomainPrincipal

and the two NTDomainPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTDomainPrincipal

.
**Returns:** true if the specified Object is equal to this

NTDomainPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTDomainPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTDomainPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- NTDomainPrincipal

```java
public NTDomainPrincipal​(
String
name)
```

Create an

NTDomainPrincipal

with a Windows NT domain name.

**Parameters:** name

- the Windows NT domain name for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

NTDomainPrincipal

```java
public NTDomainPrincipal​(
String
name)
```

Create an

NTDomainPrincipal

with a Windows NT domain name.

**Parameters:** name

- the Windows NT domain name for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### NTDomainPrincipal

public NTDomainPrincipal​(

String

name)

Create an

NTDomainPrincipal

with a Windows NT domain name.

Method Detail

- getName

```java
public
String
getName()
```

Return the Windows NT domain name for this

NTDomainPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Windows NT domain name for this

NTDomainPrincipal

- toString

```java
public
String
toString()
```

Return a string representation of this

NTDomainPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTDomainPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTDomainPrincipal

for equality. Returns true if the given object is also a

NTDomainPrincipal

and the two NTDomainPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTDomainPrincipal

.
**Returns:** true if the specified Object is equal to this

NTDomainPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTDomainPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTDomainPrincipal

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

Return the Windows NT domain name for this

NTDomainPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Windows NT domain name for this

NTDomainPrincipal

---

#### getName

public

String

getName()

Return the Windows NT domain name for this

NTDomainPrincipal

.

toString

```java
public
String
toString()
```

Return a string representation of this

NTDomainPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTDomainPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

NTDomainPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTDomainPrincipal

for equality. Returns true if the given object is also a

NTDomainPrincipal

and the two NTDomainPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTDomainPrincipal

.
**Returns:** true if the specified Object is equal to this

NTDomainPrincipal

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

NTDomainPrincipal

for equality. Returns true if the given object is also a

NTDomainPrincipal

and the two NTDomainPrincipals
have the same name.

hashCode

```java
public int hashCode()
```

Return a hash code for this

NTDomainPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTDomainPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

NTDomainPrincipal

.

---

