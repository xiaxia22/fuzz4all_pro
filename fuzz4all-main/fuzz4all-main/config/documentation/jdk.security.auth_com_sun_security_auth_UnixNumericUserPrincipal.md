# Class UnixNumericUserPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\UnixNumericUserPrincipal.html`

### Class Description

```java
public class
UnixNumericUserPrincipal

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
and represents a user's Unix identification number (UID).

Principals such as this

UnixNumericUserPrincipal

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

#### public UnixNumericUserPrincipal​(
String
name)

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

**Parameters:**
- name

- the user identification number (UID) for this user.

**Throws:**
- NullPointerException

- if the

name

is

null

.

---

#### public UnixNumericUserPrincipal​(long name)

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

**Parameters:**
- name

- the user identification number (UID) for this user
represented as a long.

---

### Method Details

#### public
String
getName()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the user identification number (UID) for this

UnixNumericUserPrincipal

---

#### public long longValue()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

**Returns:**
- the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

---

#### public
String
toString()

Return a string representation of this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

.

---

#### public boolean equals​(
Object
o)

Compares the specified Object with this

UnixNumericUserPrincipal

for equality. Returns true if the given object is also a

UnixNumericUserPrincipal

and the two
UnixNumericUserPrincipals
have the same user identification number (UID).

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

UnixNumericUserPrincipal

.

**Returns:**
- true if the specified Object is equal to this

UnixNumericUserPrincipal

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Return a hash code for this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class UnixNumericUserPrincipal

java.lang.Object

- com.sun.security.auth.UnixNumericUserPrincipal

com.sun.security.auth.UnixNumericUserPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public class
UnixNumericUserPrincipal

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
and represents a user's Unix identification number (UID).

Principals such as this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

extends

Object

implements

Principal

,

Serializable

This class implements the

Principal

interface
and represents a user's Unix identification number (UID).

Principals such as this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

​(long name)

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

UnixNumericUserPrincipal

​(

String

name)

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

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

UnixNumericUserPrincipal

for equality.

String

getName

()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

int

hashCode

()

Return a hash code for this

UnixNumericUserPrincipal

.

long

longValue

()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

String

toString

()

Return a string representation of this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

​(long name)

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

UnixNumericUserPrincipal

​(

String

name)

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

---

#### Constructor Summary

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

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

UnixNumericUserPrincipal

for equality.

String

getName

()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

int

hashCode

()

Return a hash code for this

UnixNumericUserPrincipal

.

long

longValue

()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

String

toString

()

Return a string representation of this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

for equality.

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

Return a hash code for this

UnixNumericUserPrincipal

.

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

Return a string representation of this

UnixNumericUserPrincipal

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

- UnixNumericUserPrincipal

```java
public UnixNumericUserPrincipal​(
String
name)
```

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

**Parameters:** name

- the user identification number (UID) for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

- UnixNumericUserPrincipal

```java
public UnixNumericUserPrincipal​(long name)
```

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

**Parameters:** name

- the user identification number (UID) for this user
represented as a long.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the user identification number (UID) for this

UnixNumericUserPrincipal

- longValue

```java
public long longValue()
```

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

**Returns:** the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

- toString

```java
public
String
toString()
```

Return a string representation of this

UnixNumericUserPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixNumericUserPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixNumericUserPrincipal

for equality. Returns true if the given object is also a

UnixNumericUserPrincipal

and the two
UnixNumericUserPrincipals
have the same user identification number (UID).

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixNumericUserPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixNumericUserPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixNumericUserPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixNumericUserPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- UnixNumericUserPrincipal

```java
public UnixNumericUserPrincipal​(
String
name)
```

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

**Parameters:** name

- the user identification number (UID) for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

- UnixNumericUserPrincipal

```java
public UnixNumericUserPrincipal​(long name)
```

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

**Parameters:** name

- the user identification number (UID) for this user
represented as a long.

---

#### Constructor Detail

UnixNumericUserPrincipal

```java
public UnixNumericUserPrincipal​(
String
name)
```

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

**Parameters:** name

- the user identification number (UID) for this user.
**Throws:** NullPointerException

- if the

name

is

null

.

---

#### UnixNumericUserPrincipal

public UnixNumericUserPrincipal​(

String

name)

Create a

UnixNumericUserPrincipal

using a

String

representation of the
user's identification number (UID).

UnixNumericUserPrincipal

```java
public UnixNumericUserPrincipal​(long name)
```

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

**Parameters:** name

- the user identification number (UID) for this user
represented as a long.

---

#### UnixNumericUserPrincipal

public UnixNumericUserPrincipal​(long name)

Create a

UnixNumericUserPrincipal

using a
long representation of the user's identification number (UID).

Method Detail

- getName

```java
public
String
getName()
```

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the user identification number (UID) for this

UnixNumericUserPrincipal

- longValue

```java
public long longValue()
```

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

**Returns:** the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

- toString

```java
public
String
toString()
```

Return a string representation of this

UnixNumericUserPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixNumericUserPrincipal

.

- equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixNumericUserPrincipal

for equality. Returns true if the given object is also a

UnixNumericUserPrincipal

and the two
UnixNumericUserPrincipals
have the same user identification number (UID).

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixNumericUserPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixNumericUserPrincipal

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixNumericUserPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixNumericUserPrincipal

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

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

**Specified by:** getName

in interface

Principal
**Returns:** the user identification number (UID) for this

UnixNumericUserPrincipal

---

#### getName

public

String

getName()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

.

longValue

```java
public long longValue()
```

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

**Returns:** the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

---

#### longValue

public long longValue()

Return the user identification number (UID) for this

UnixNumericUserPrincipal

as a long.

toString

```java
public
String
toString()
```

Return a string representation of this

UnixNumericUserPrincipal

.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** a string representation of this

UnixNumericUserPrincipal

.

---

#### toString

public

String

toString()

Return a string representation of this

UnixNumericUserPrincipal

.

equals

```java
public boolean equals​(
Object
o)
```

Compares the specified Object with this

UnixNumericUserPrincipal

for equality. Returns true if the given object is also a

UnixNumericUserPrincipal

and the two
UnixNumericUserPrincipals
have the same user identification number (UID).

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** o

- Object to be compared for equality with this

UnixNumericUserPrincipal

.
**Returns:** true if the specified Object is equal to this

UnixNumericUserPrincipal

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

UnixNumericUserPrincipal

for equality. Returns true if the given object is also a

UnixNumericUserPrincipal

and the two
UnixNumericUserPrincipals
have the same user identification number (UID).

hashCode

```java
public int hashCode()
```

Return a hash code for this

UnixNumericUserPrincipal

.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

UnixNumericUserPrincipal

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Return a hash code for this

UnixNumericUserPrincipal

.

---

