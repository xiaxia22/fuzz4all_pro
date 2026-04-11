# Class UnixPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\UnixPrincipal.html`

### Class Description

```java
public class
UnixPrincipal

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
and represents a Unix user.

Principals such as this

UnixPrincipal

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

#### public UnixPrincipal​(
String
name)

Create a UnixPrincipal with a Unix username.

**Parameters:**
- name

- the Unix username for this user.

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

Return the Unix username for this

UnixPrincipal

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the Unix username for this

UnixPrincipal

---

#### public
String
toString()

Return a string representation of this

UnixPrincipal

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

UnixPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

UnixPrincipal

for equality. Returns true if the given object is also a

UnixPrincipal

and the two UnixPrincipals
have the same username.

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

UnixPrincipal

.

**Returns:**
- true if the specified Object is equal to this

UnixPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

UnixPrincipal

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

UnixPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class UnixPrincipal

java.lang.Object

- com.sun.security.auth.UnixPrincipal

com.sun.security.auth.UnixPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
UnixPrincipal

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
and represents a Unix user.

Principals such as this

UnixPrincipal

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

UnixPrincipal

extends

Object

implements

Principal

,

Serializable

This class implements the

Principal

interface
and represents a Unix user.

Principals such as this

UnixPrincipal

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

UnixPrincipal

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

UnixPrincipal

​(

String

name)

Create a UnixPrincipal with a Unix username.

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

UnixPrincipal

for equality.

String

getName

()

Return the Unix username for this

UnixPrincipal

.

int

hashCode

()

Return a hash code for this

UnixPrincipal

.

String

toString

()

Return a string representation of this

UnixPrincipal

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

UnixPrincipal

​(

String

name)

Create a UnixPrincipal with a Unix username.

---

#### Constructor Summary

Create a UnixPrincipal with a Unix username.

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

UnixPrincipal

for equality.

String

getName

()

Return the Unix username for this

UnixPrincipal

.

int

hashCode

()

Return a hash code for this

UnixPrincipal

.

String

toString

()

Return a string representation of this

UnixPrincipal

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

UnixPrincipal

for equality.

Return the Unix username for this

UnixPrincipal

.

Return a hash code for this

UnixPrincipal

.

Return a string representation of this

UnixPrincipal

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

- UnixPrincipal

```java
public UnixPrincipal​(
String
name)
```

Create a UnixPrincipal with a Unix username.

**Parameters:** name

- the Unix username for this user.
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

Return the Unix username for this

UnixPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Unix username for this

UnixPrincipal

- toString

```java
public
String
toString()
```

Return a string representation of this

UnixPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixPrincipal

for equality. Returns true if the given object is also a

UnixPrincipal

and the two UnixPrincipals
have the same username.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- UnixPrincipal

```java
public UnixPrincipal​(
String
name)
```

Create a UnixPrincipal with a Unix username.

**Parameters:** name

- the Unix username for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

UnixPrincipal

```java
public UnixPrincipal​(
String
name)
```

Create a UnixPrincipal with a Unix username.

**Parameters:** name

- the Unix username for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### UnixPrincipal

public UnixPrincipal​(

String

name)

Create a UnixPrincipal with a Unix username.

Method Detail

- getName

```java
public
String
getName()
```

Return the Unix username for this

UnixPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Unix username for this

UnixPrincipal

- toString

```java
public
String
toString()
```

Return a string representation of this

UnixPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixPrincipal

for equality. Returns true if the given object is also a

UnixPrincipal

and the two UnixPrincipals
have the same username.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixPrincipal

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

Return the Unix username for this

UnixPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the Unix username for this

UnixPrincipal

---

#### getName

public

String

getName()

Return the Unix username for this

UnixPrincipal

.

toString

```java
public
String
toString()
```

Return a string representation of this

UnixPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

UnixPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixPrincipal

for equality. Returns true if the given object is also a

UnixPrincipal

and the two UnixPrincipals
have the same username.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixPrincipal

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

UnixPrincipal

for equality. Returns true if the given object is also a

UnixPrincipal

and the two UnixPrincipals
have the same username.

hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

UnixPrincipal

.

---

