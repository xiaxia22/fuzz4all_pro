# Class LdapPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\LdapPrincipal.html`

### Class Description

```java
public final class
LdapPrincipal

extends
Object

implements
Principal
,
Serializable
```

A principal identified by a distinguished name as specified by

RFC 2253

.

After successful authentication, a user

Principal

can be associated with a particular

Subject

to augment that

Subject

with an additional identity.
Authorization decisions can then be based upon the

Principal

s that are associated with a

Subject

.

This class is immutable.

**All Implemented Interfaces:** Serializable

,

Principal

---

### Field Details

*No entries found.*

### Constructor Details

#### public LdapPrincipal​(
String
name)
throws
InvalidNameException

Creates an LDAP principal.

**Parameters:**
- name

- The principal's string distinguished name.

**Throws:**
- InvalidNameException

- If a syntax violation is detected.
- NullPointerException

- If the

name

is

null

.

---

### Method Details

#### public boolean equals​(
Object
object)

Compares this principal to the specified object.

**Specified by:**
- equals

in interface

Principal

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

- The object to compare this principal against.

**Returns:**
- true if they are equal; false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Computes the hash code for this principal.

**Specified by:**
- hashCode

in interface

Principal

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The principal's hash code.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
getName()

Returns the name originally used to create this principal.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- The principal's string name.

---

#### public
String
toString()

Creates a string representation of this principal's name in the format
defined by

RFC 2253

.
If the name has zero components an empty string is returned.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Object

**Returns:**
- The principal's string name.

---

### Additional Sections

#### Class LdapPrincipal

java.lang.Object

- com.sun.security.auth.LdapPrincipal

com.sun.security.auth.LdapPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public final class
LdapPrincipal

extends
Object

implements
Principal
,
Serializable
```

A principal identified by a distinguished name as specified by

RFC 2253

.

After successful authentication, a user

Principal

can be associated with a particular

Subject

to augment that

Subject

with an additional identity.
Authorization decisions can then be based upon the

Principal

s that are associated with a

Subject

.

This class is immutable.

**Since:** 1.6
**See Also:** Serialized Form

public final class

LdapPrincipal

extends

Object

implements

Principal

,

Serializable

A principal identified by a distinguished name as specified by

RFC 2253

.

After successful authentication, a user

Principal

can be associated with a particular

Subject

to augment that

Subject

with an additional identity.
Authorization decisions can then be based upon the

Principal

s that are associated with a

Subject

.

This class is immutable.

After successful authentication, a user

Principal

can be associated with a particular

Subject

to augment that

Subject

with an additional identity.
Authorization decisions can then be based upon the

Principal

s that are associated with a

Subject

.

This class is immutable.

This class is immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LdapPrincipal

​(

String

name)

Creates an LDAP principal.

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

object)

Compares this principal to the specified object.

String

getName

()

Returns the name originally used to create this principal.

int

hashCode

()

Computes the hash code for this principal.

String

toString

()

Creates a string representation of this principal's name in the format
defined by

RFC 2253

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

LdapPrincipal

​(

String

name)

Creates an LDAP principal.

---

#### Constructor Summary

Creates an LDAP principal.

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

object)

Compares this principal to the specified object.

String

getName

()

Returns the name originally used to create this principal.

int

hashCode

()

Computes the hash code for this principal.

String

toString

()

Creates a string representation of this principal's name in the format
defined by

RFC 2253

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

Compares this principal to the specified object.

Returns the name originally used to create this principal.

Computes the hash code for this principal.

Creates a string representation of this principal's name in the format
defined by

RFC 2253

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

- LdapPrincipal

```java
public LdapPrincipal​(
String
name)
throws
InvalidNameException
```

Creates an LDAP principal.

**Parameters:** name

- The principal's string distinguished name.
**Throws:** InvalidNameException

- If a syntax violation is detected.
**Throws:** NullPointerException

- If the

name

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Compares this principal to the specified object.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** object

- The object to compare this principal against.
**Returns:** true if they are equal; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes the hash code for this principal.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** The principal's hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getName

```java
public
String
getName()
```

Returns the name originally used to create this principal.

**Specified by:** getName

in interface

Principal
**Returns:** The principal's string name.

- toString

```java
public
String
toString()
```

Creates a string representation of this principal's name in the format
defined by

RFC 2253

.
If the name has zero components an empty string is returned.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** The principal's string name.

Constructor Detail

- LdapPrincipal

```java
public LdapPrincipal​(
String
name)
throws
InvalidNameException
```

Creates an LDAP principal.

**Parameters:** name

- The principal's string distinguished name.
**Throws:** InvalidNameException

- If a syntax violation is detected.
**Throws:** NullPointerException

- If the

name

is

null

.

---

#### Constructor Detail

LdapPrincipal

```java
public LdapPrincipal​(
String
name)
throws
InvalidNameException
```

Creates an LDAP principal.

**Parameters:** name

- The principal's string distinguished name.
**Throws:** InvalidNameException

- If a syntax violation is detected.
**Throws:** NullPointerException

- If the

name

is

null

.

---

#### LdapPrincipal

public LdapPrincipal​(

String

name)
throws

InvalidNameException

Creates an LDAP principal.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Compares this principal to the specified object.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** object

- The object to compare this principal against.
**Returns:** true if they are equal; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes the hash code for this principal.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** The principal's hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getName

```java
public
String
getName()
```

Returns the name originally used to create this principal.

**Specified by:** getName

in interface

Principal
**Returns:** The principal's string name.

- toString

```java
public
String
toString()
```

Creates a string representation of this principal's name in the format
defined by

RFC 2253

.
If the name has zero components an empty string is returned.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** The principal's string name.

---

#### Method Detail

equals

```java
public boolean equals​(
Object
object)
```

Compares this principal to the specified object.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** object

- The object to compare this principal against.
**Returns:** true if they are equal; false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Compares this principal to the specified object.

hashCode

```java
public int hashCode()
```

Computes the hash code for this principal.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** The principal's hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes the hash code for this principal.

getName

```java
public
String
getName()
```

Returns the name originally used to create this principal.

**Specified by:** getName

in interface

Principal
**Returns:** The principal's string name.

---

#### getName

public

String

getName()

Returns the name originally used to create this principal.

toString

```java
public
String
toString()
```

Creates a string representation of this principal's name in the format
defined by

RFC 2253

.
If the name has zero components an empty string is returned.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** The principal's string name.

---

#### toString

public

String

toString()

Creates a string representation of this principal's name in the format
defined by

RFC 2253

.
If the name has zero components an empty string is returned.

---

