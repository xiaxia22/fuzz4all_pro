# Class UnixNumericGroupPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\UnixNumericGroupPrincipal.html`

### Class Description

```java
public class
UnixNumericGroupPrincipal

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
and represents a user's Unix group identification number (GID).

Principals such as this

UnixNumericGroupPrincipal

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

#### public UnixNumericGroupPrincipal​(
String
name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

**Parameters:**
- name

- the user's group identification number (GID)
for this user.
- primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.

**Throws:**
- NullPointerException

- if the

name

is

null

.

---

#### public UnixNumericGroupPrincipal​(long name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

**Parameters:**
- name

- the user's group identification number (GID) for this user
represented as a long.
- primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.

---

### Method Details

#### public
String
getName()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the user's group identification number (GID) for this

UnixNumericGroupPrincipal

---

#### public long longValue()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

**Returns:**
- the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

---

#### public boolean isPrimaryGroup()

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

**Returns:**
- true if this group identification number (GID) represents
the primary group to which this user belongs,
or false otherwise.

---

#### public
String
toString()

Return a string representation of this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

UnixNumericGroupPrincipal

for equality. Returns true if the given object is also a

UnixNumericGroupPrincipal

and the two
UnixNumericGroupPrincipals
have the same group identification number (GID).

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

UnixNumericGroupPrincipal

.

**Returns:**
- true if the specified Object is equal to this

UnixNumericGroupPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class UnixNumericGroupPrincipal

java.lang.Object

- com.sun.security.auth.UnixNumericGroupPrincipal

com.sun.security.auth.UnixNumericGroupPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
UnixNumericGroupPrincipal

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
and represents a user's Unix group identification number (GID).

Principals such as this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

extends

Object

implements

Principal

,

Serializable

This class implements the

Principal

interface
and represents a user's Unix group identification number (GID).

Principals such as this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

​(long name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

UnixNumericGroupPrincipal

​(

String

name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

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

UnixNumericGroupPrincipal

for equality.

String

getName

()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

int

hashCode

()

Return a hash code for this

UnixNumericGroupPrincipal

.

boolean

isPrimaryGroup

()

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

long

longValue

()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

String

toString

()

Return a string representation of this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

​(long name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

UnixNumericGroupPrincipal

​(

String

name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

---

#### Constructor Summary

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

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

UnixNumericGroupPrincipal

for equality.

String

getName

()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

int

hashCode

()

Return a hash code for this

UnixNumericGroupPrincipal

.

boolean

isPrimaryGroup

()

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

long

longValue

()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

String

toString

()

Return a string representation of this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

for equality.

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

Return a hash code for this

UnixNumericGroupPrincipal

.

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

Return a string representation of this

UnixNumericGroupPrincipal

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

- UnixNumericGroupPrincipal

```java
public UnixNumericGroupPrincipal​(
String
name,
boolean primaryGroup)
```

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

**Parameters:** name

- the user's group identification number (GID)
for this user.
**Parameters:** primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.
**Throws:** NullPointerException

- if the

name

is

null

.

- UnixNumericGroupPrincipal

```java
public UnixNumericGroupPrincipal​(long name,
boolean primaryGroup)
```

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

**Parameters:** name

- the user's group identification number (GID) for this user
represented as a long.
**Parameters:** primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the user's group identification number (GID) for this

UnixNumericGroupPrincipal

- longValue

```java
public long longValue()
```

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

**Returns:** the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

- isPrimaryGroup

```java
public boolean isPrimaryGroup()
```

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

**Returns:** true if this group identification number (GID) represents
the primary group to which this user belongs,
or false otherwise.

- toString

```java
public
String
toString()
```

Return a string representation of this

UnixNumericGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixNumericGroupPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixNumericGroupPrincipal

for equality. Returns true if the given object is also a

UnixNumericGroupPrincipal

and the two
UnixNumericGroupPrincipals
have the same group identification number (GID).

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixNumericGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixNumericGroupPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixNumericGroupPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixNumericGroupPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- UnixNumericGroupPrincipal

```java
public UnixNumericGroupPrincipal​(
String
name,
boolean primaryGroup)
```

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

**Parameters:** name

- the user's group identification number (GID)
for this user.
**Parameters:** primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.
**Throws:** NullPointerException

- if the

name

is

null

.

- UnixNumericGroupPrincipal

```java
public UnixNumericGroupPrincipal​(long name,
boolean primaryGroup)
```

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

**Parameters:** name

- the user's group identification number (GID) for this user
represented as a long.
**Parameters:** primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.

---

#### Constructor Detail

UnixNumericGroupPrincipal

```java
public UnixNumericGroupPrincipal​(
String
name,
boolean primaryGroup)
```

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

**Parameters:** name

- the user's group identification number (GID)
for this user.
**Parameters:** primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### UnixNumericGroupPrincipal

public UnixNumericGroupPrincipal​(

String

name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a

String

representation of the user's
group identification number (GID).

UnixNumericGroupPrincipal

```java
public UnixNumericGroupPrincipal​(long name,
boolean primaryGroup)
```

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

**Parameters:** name

- the user's group identification number (GID) for this user
represented as a long.
**Parameters:** primaryGroup

- true if the specified GID represents the
primary group to which this user belongs.

---

#### UnixNumericGroupPrincipal

public UnixNumericGroupPrincipal​(long name,
boolean primaryGroup)

Create a

UnixNumericGroupPrincipal

using a
long representation of the user's group identification number (GID).

Method Detail

- getName

```java
public
String
getName()
```

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the user's group identification number (GID) for this

UnixNumericGroupPrincipal

- longValue

```java
public long longValue()
```

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

**Returns:** the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

- isPrimaryGroup

```java
public boolean isPrimaryGroup()
```

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

**Returns:** true if this group identification number (GID) represents
the primary group to which this user belongs,
or false otherwise.

- toString

```java
public
String
toString()
```

Return a string representation of this

UnixNumericGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixNumericGroupPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixNumericGroupPrincipal

for equality. Returns true if the given object is also a

UnixNumericGroupPrincipal

and the two
UnixNumericGroupPrincipals
have the same group identification number (GID).

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixNumericGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixNumericGroupPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixNumericGroupPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixNumericGroupPrincipal

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

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the user's group identification number (GID) for this

UnixNumericGroupPrincipal

---

#### getName

public

String

getName()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

.

longValue

```java
public long longValue()
```

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

**Returns:** the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

---

#### longValue

public long longValue()

Return the user's group identification number (GID) for this

UnixNumericGroupPrincipal

as a long.

isPrimaryGroup

```java
public boolean isPrimaryGroup()
```

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

**Returns:** true if this group identification number (GID) represents
the primary group to which this user belongs,
or false otherwise.

---

#### isPrimaryGroup

public boolean isPrimaryGroup()

Return whether this group identification number (GID) represents
the primary group to which this user belongs.

toString

```java
public
String
toString()
```

Return a string representation of this

UnixNumericGroupPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixNumericGroupPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

UnixNumericGroupPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixNumericGroupPrincipal

for equality. Returns true if the given object is also a

UnixNumericGroupPrincipal

and the two
UnixNumericGroupPrincipals
have the same group identification number (GID).

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixNumericGroupPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixNumericGroupPrincipal

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

UnixNumericGroupPrincipal

for equality. Returns true if the given object is also a

UnixNumericGroupPrincipal

and the two
UnixNumericGroupPrincipals
have the same group identification number (GID).

hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixNumericGroupPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixNumericGroupPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

UnixNumericGroupPrincipal

.

---

