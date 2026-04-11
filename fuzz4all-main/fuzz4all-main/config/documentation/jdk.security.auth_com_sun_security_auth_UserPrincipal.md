# Class UserPrincipal

**Source:** `jdk.security.auth\com\sun\security\auth\UserPrincipal.html`

### Class Description

```java
public final class
UserPrincipal

extends
Object

implements
Principal
,
Serializable
```

A user principal identified by a username or account name.

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

#### public UserPrincipal​(
String
name)

Creates a principal.

**Parameters:**
- name

- The principal's string name.

**Throws:**
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

Returns a hash code for this principal.

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

Returns the name of this principal.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- The principal's name.

---

#### public
String
toString()

Returns a string representation of this principal.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Object

**Returns:**
- The principal's name.

---

### Additional Sections

#### Class UserPrincipal

java.lang.Object

- com.sun.security.auth.UserPrincipal

com.sun.security.auth.UserPrincipal

**All Implemented Interfaces:** Serializable

,

Principal

```java
public final class
UserPrincipal

extends
Object

implements
Principal
,
Serializable
```

A user principal identified by a username or account name.

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

UserPrincipal

extends

Object

implements

Principal

,

Serializable

A user principal identified by a username or account name.

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

UserPrincipal

​(

String

name)

Creates a principal.

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

Returns the name of this principal.

int

hashCode

()

Returns a hash code for this principal.

String

toString

()

Returns a string representation of this principal.

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

UserPrincipal

​(

String

name)

Creates a principal.

---

#### Constructor Summary

Creates a principal.

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

Returns the name of this principal.

int

hashCode

()

Returns a hash code for this principal.

String

toString

()

Returns a string representation of this principal.

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

Returns the name of this principal.

Returns a hash code for this principal.

Returns a string representation of this principal.

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

- UserPrincipal

```java
public UserPrincipal​(
String
name)
```

Creates a principal.

**Parameters:** name

- The principal's string name.
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

Returns a hash code for this principal.

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

Returns the name of this principal.

**Specified by:** getName

in interface

Principal
**Returns:** The principal's name.

- toString

```java
public
String
toString()
```

Returns a string representation of this principal.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** The principal's name.

Constructor Detail

- UserPrincipal

```java
public UserPrincipal​(
String
name)
```

Creates a principal.

**Parameters:** name

- The principal's string name.
**Throws:** NullPointerException

- If the

name

is

null

.

---

#### Constructor Detail

UserPrincipal

```java
public UserPrincipal​(
String
name)
```

Creates a principal.

**Parameters:** name

- The principal's string name.
**Throws:** NullPointerException

- If the

name

is

null

.

---

#### UserPrincipal

public UserPrincipal​(

String

name)

Creates a principal.

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

Returns a hash code for this principal.

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

Returns the name of this principal.

**Specified by:** getName

in interface

Principal
**Returns:** The principal's name.

- toString

```java
public
String
toString()
```

Returns a string representation of this principal.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** The principal's name.

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

Returns a hash code for this principal.

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

Returns a hash code for this principal.

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
**Returns:** The principal's name.

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

Returns a string representation of this principal.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** The principal's name.

---

#### toString

public

String

toString()

Returns a string representation of this principal.

---

