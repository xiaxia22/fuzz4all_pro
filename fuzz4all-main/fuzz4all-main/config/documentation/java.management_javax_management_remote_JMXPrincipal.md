# Class JMXPrincipal

**Source:** `java.management\javax\management\remote\JMXPrincipal.html`

### Class Description

```java
public class
JMXPrincipal

extends
Object

implements
Principal
,
Serializable
```

The identity of a remote client of the JMX Remote API.

Principals such as this

JMXPrincipal

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information on how to achieve this.
Authorization decisions can then be based upon
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

#### public JMXPrincipal​(
String
name)

Creates a JMXPrincipal for a given identity.

**Parameters:**
- name

- the JMX Remote API name for this identity.

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

Returns the name of this principal.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the name of this

JMXPrincipal

.

---

#### public
String
toString()

Returns a string representation of this

JMXPrincipal

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

JMXPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

JMXPrincipal

for equality. Returns true if the given object is also a

JMXPrincipal

and the two JMXPrincipals
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

JMXPrincipal

.

**Returns:**
- true if the specified Object is equal to this

JMXPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code for this

JMXPrincipal

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

JMXPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class JMXPrincipal

java.lang.Object

- javax.management.remote.JMXPrincipal

javax.management.remote.JMXPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
JMXPrincipal

extends
Object

implements
Principal
,
Serializable
```

The identity of a remote client of the JMX Remote API.

Principals such as this

JMXPrincipal

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information on how to achieve this.
Authorization decisions can then be based upon
the Principals associated with a

Subject

.

**Since:** 1.5
**See Also:** Principal

,

Subject

,

Serialized Form

public class

JMXPrincipal

extends

Object

implements

Principal

,

Serializable

The identity of a remote client of the JMX Remote API.

Principals such as this

JMXPrincipal

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information on how to achieve this.
Authorization decisions can then be based upon
the Principals associated with a

Subject

.

The identity of a remote client of the JMX Remote API.

Principals such as this

JMXPrincipal

may be associated with a particular

Subject

to augment that

Subject

with an additional
identity. Refer to the

Subject

class for more information on how to achieve this.
Authorization decisions can then be based upon
the Principals associated with a

Subject

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JMXPrincipal

​(

String

name)

Creates a JMXPrincipal for a given identity.

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

JMXPrincipal

for equality.

String

getName

()

Returns the name of this principal.

int

hashCode

()

Returns a hash code for this

JMXPrincipal

.

String

toString

()

Returns a string representation of this

JMXPrincipal

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

JMXPrincipal

​(

String

name)

Creates a JMXPrincipal for a given identity.

---

#### Constructor Summary

Creates a JMXPrincipal for a given identity.

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

JMXPrincipal

for equality.

String

getName

()

Returns the name of this principal.

int

hashCode

()

Returns a hash code for this

JMXPrincipal

.

String

toString

()

Returns a string representation of this

JMXPrincipal

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

JMXPrincipal

for equality.

Returns the name of this principal.

Returns a hash code for this

JMXPrincipal

.

Returns a string representation of this

JMXPrincipal

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

- JMXPrincipal

```java
public JMXPrincipal​(
String
name)
```

Creates a JMXPrincipal for a given identity.

**Parameters:** name

- the JMX Remote API name for this identity.
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

Returns the name of this principal.

**Specified by:** getName

in interface

Principal
**Returns:** the name of this

JMXPrincipal

.

- toString

```java
public
String
toString()
```

Returns a string representation of this

JMXPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

JMXPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

JMXPrincipal

for equality. Returns true if the given object is also a

JMXPrincipal

and the two JMXPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

JMXPrincipal

.
**Returns:** true if the specified Object is equal to this

JMXPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

JMXPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

JMXPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- JMXPrincipal

```java
public JMXPrincipal​(
String
name)
```

Creates a JMXPrincipal for a given identity.

**Parameters:** name

- the JMX Remote API name for this identity.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### Constructor Detail

JMXPrincipal

```java
public JMXPrincipal​(
String
name)
```

Creates a JMXPrincipal for a given identity.

**Parameters:** name

- the JMX Remote API name for this identity.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### JMXPrincipal

public JMXPrincipal​(

String

name)

Creates a JMXPrincipal for a given identity.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this principal.

**Specified by:** getName

in interface

Principal
**Returns:** the name of this

JMXPrincipal

.

- toString

```java
public
String
toString()
```

Returns a string representation of this

JMXPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

JMXPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

JMXPrincipal

for equality. Returns true if the given object is also a

JMXPrincipal

and the two JMXPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

JMXPrincipal

.
**Returns:** true if the specified Object is equal to this

JMXPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

JMXPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

JMXPrincipal

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

Returns the name of this principal.

**Specified by:** getName

in interface

Principal
**Returns:** the name of this

JMXPrincipal

.

---

#### getName

public

String

getName()

Returns the name of this principal.

toString

```java
public
String
toString()
```

Returns a string representation of this

JMXPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

JMXPrincipal

.

---

#### toString

public

String

toString()

Returns a string representation of this

JMXPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

JMXPrincipal

for equality. Returns true if the given object is also a

JMXPrincipal

and the two JMXPrincipals
have the same name.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

JMXPrincipal

.
**Returns:** true if the specified Object is equal to this

JMXPrincipal

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

JMXPrincipal

for equality. Returns true if the given object is also a

JMXPrincipal

and the two JMXPrincipals
have the same name.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

JMXPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

JMXPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

JMXPrincipal

.

---

