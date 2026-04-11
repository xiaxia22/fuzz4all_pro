# Class NTUserPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\NTUserPrincipal.html`

### Class Description

```java
public class
NTUserPrincipal

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
and represents a Windows NT user.

Principals such as this

NTUserPrincipal

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

#### public NTUserPrincipal​(
String
name)

Create an

NTUserPrincipal

with a Windows NT username.

**Parameters:**
- name

- the Windows NT username for this user.

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

Return the Windows NT username for this

NTPrincipal

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the Windows NT username for this

NTPrincipal

---

#### public
String
toString()

Return a string representation of this

NTPrincipal

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

NTPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

NTUserPrincipal

for equality. Returns true if the given object is also a

NTUserPrincipal

and the two NTUserPrincipals
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

NTPrincipal

.

**Returns:**
- true if the specified Object is equal to this

NTPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

NTUserPrincipal

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

NTUserPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class NTUserPrincipal

java.lang.Object

- com.sun.security.auth.NTUserPrincipal

com.sun.security.auth.NTUserPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
NTUserPrincipal

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
and represents a Windows NT user.

Principals such as this

NTUserPrincipal

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

NTUserPrincipal

extends

Object

implements

Principal

,

Serializable

This class implements the

Principal

interface
and represents a Windows NT user.

Principals such as this

NTUserPrincipal

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

NTUserPrincipal

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

NTUserPrincipal

​(

String

name)

Create an

NTUserPrincipal

with a Windows NT username.

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

NTUserPrincipal

for equality.

String

getName

()

Return the Windows NT username for this

NTPrincipal

.

int

hashCode

()

Return a hash code for this

NTUserPrincipal

.

String

toString

()

Return a string representation of this

NTPrincipal

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

NTUserPrincipal

​(

String

name)

Create an

NTUserPrincipal

with a Windows NT username.

---

#### Constructor Summary

Create an

NTUserPrincipal

with a Windows NT username.

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

NTUserPrincipal

for equality.

String

getName

()

Return the Windows NT username for this

NTPrincipal

.

int

hashCode

()

Return a hash code for this

NTUserPrincipal

.

String

toString

()

Return a string representation of this

NTPrincipal

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

NTUserPrincipal

for equality.

Return the Windows NT username for this

NTPrincipal

.

Return a hash code for this

NTUserPrincipal

.

Return a string representation of this

NTPrincipal

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

- NTUserPrincipal

```java
public NTUserPrincipal​(
String
name)
```

Create an

NTUserPrincipal

with a Windows NT username.

**Parameters:** name

- the Windows NT username for this user.
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

Return the Windows NT username for this

NTPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Windows NT username for this

NTPrincipal

- toString

```java
public
String
toString()
```

Return a string representation of this

NTPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTUserPrincipal

for equality. Returns true if the given object is also a

NTUserPrincipal

and the two NTUserPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTPrincipal

.
**Returns:** true if the specified Object is equal to this

NTPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTUserPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTUserPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- NTUserPrincipal

```java
public NTUserPrincipal​(
String
name)
```

Create an

NTUserPrincipal

with a Windows NT username.

**Parameters:** name

- the Windows NT username for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

NTUserPrincipal

```java
public NTUserPrincipal​(
String
name)
```

Create an

NTUserPrincipal

with a Windows NT username.

**Parameters:** name

- the Windows NT username for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### NTUserPrincipal

public NTUserPrincipal​(

String

name)

Create an

NTUserPrincipal

with a Windows NT username.

Method Detail

- getName

```java
public
String
getName()
```

Return the Windows NT username for this

NTPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Windows NT username for this

NTPrincipal

- toString

```java
public
String
toString()
```

Return a string representation of this

NTPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTUserPrincipal

for equality. Returns true if the given object is also a

NTUserPrincipal

and the two NTUserPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTPrincipal

.
**Returns:** true if the specified Object is equal to this

NTPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

NTUserPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTUserPrincipal

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

Return the Windows NT username for this

NTPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Windows NT username for this

NTPrincipal

---

#### getName

public

String

getName()

Return the Windows NT username for this

NTPrincipal

.

toString

```java
public
String
toString()
```

Return a string representation of this

NTPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

NTPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

NTPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

NTUserPrincipal

for equality. Returns true if the given object is also a

NTUserPrincipal

and the two NTUserPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

NTPrincipal

.
**Returns:** true if the specified Object is equal to this

NTPrincipal

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

NTUserPrincipal

for equality. Returns true if the given object is also a

NTUserPrincipal

and the two NTUserPrincipals
have the same name.

hashCode

```java
public int hashCode()
```

Return a hash code for this

NTUserPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

NTUserPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

NTUserPrincipal

.

---

