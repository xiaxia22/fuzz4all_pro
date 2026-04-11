# Class AllPermission

**Source:** `java.base\java\security\AllPermission.html`

### Class Description

```java
public final class
AllPermission

extends
Permission
```

The AllPermission is a permission that implies all other permissions.

Note:

Granting AllPermission should be done with extreme care,
as it implies all other permissions. Thus, it grants code the ability
to run with security
disabled. Extreme caution should be taken before granting such
a permission to code. This permission should be used only during testing,
or in extremely rare cases where an application or applet is
completely trusted and adding the necessary permissions to the policy
is prohibitively cumbersome.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public AllPermission()

Creates a new AllPermission object.

---

#### public AllPermission​(
String
name,

String
actions)

Creates a new AllPermission object. This
constructor exists for use by the

Policy

object
to instantiate new Permission objects.

**Parameters:**
- name

- ignored
- actions

- ignored.

---

### Method Details

#### public boolean implies​(
Permission
p)

Checks if the specified permission is "implied" by
this object. This method always returns true.

**Specified by:**
- implies

in class

Permission

**Parameters:**
- p

- the permission to check against.

**Returns:**
- return

---

#### public boolean equals​(
Object
obj)

Checks two AllPermission objects for equality. Two AllPermission
objects are always equal.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object we are testing for equality with this object.

**Returns:**
- true if

obj

is an AllPermission, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
getActions()

Returns the canonical string representation of the actions.

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the actions.

---

#### public
PermissionCollection
newPermissionCollection()

Returns a new PermissionCollection object for storing AllPermission
objects.

**Overrides:**
- newPermissionCollection

in class

Permission

**Returns:**
- a new PermissionCollection object suitable for
storing AllPermissions.

---

### Additional Sections

#### Class AllPermission

java.lang.Object

- java.security.Permission
- - java.security.AllPermission

java.security.Permission

- java.security.AllPermission

java.security.AllPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
AllPermission

extends
Permission
```

The AllPermission is a permission that implies all other permissions.

Note:

Granting AllPermission should be done with extreme care,
as it implies all other permissions. Thus, it grants code the ability
to run with security
disabled. Extreme caution should be taken before granting such
a permission to code. This permission should be used only during testing,
or in extremely rare cases where an application or applet is
completely trusted and adding the necessary permissions to the policy
is prohibitively cumbersome.

**Since:** 1.2
**See Also:** Permission

,

AccessController

,

Permissions

,

PermissionCollection

,

SecurityManager

public final class

AllPermission

extends

Permission

The AllPermission is a permission that implies all other permissions.

Note:

Granting AllPermission should be done with extreme care,
as it implies all other permissions. Thus, it grants code the ability
to run with security
disabled. Extreme caution should be taken before granting such
a permission to code. This permission should be used only during testing,
or in extremely rare cases where an application or applet is
completely trusted and adding the necessary permissions to the policy
is prohibitively cumbersome.

Note:

Granting AllPermission should be done with extreme care,
as it implies all other permissions. Thus, it grants code the ability
to run with security
disabled. Extreme caution should be taken before granting such
a permission to code. This permission should be used only during testing,
or in extremely rare cases where an application or applet is
completely trusted and adding the necessary permissions to the policy
is prohibitively cumbersome.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AllPermission

()

Creates a new AllPermission object.

AllPermission

​(

String

name,

String

actions)

Creates a new AllPermission object.

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

obj)

Checks two AllPermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if the specified permission is "implied" by
this object.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing AllPermission
objects.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

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

Constructor Summary

Constructors

Constructor

Description

AllPermission

()

Creates a new AllPermission object.

AllPermission

​(

String

name,

String

actions)

Creates a new AllPermission object.

---

#### Constructor Summary

Creates a new AllPermission object.

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

obj)

Checks two AllPermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if the specified permission is "implied" by
this object.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing AllPermission
objects.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

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

---

#### Method Summary

Checks two AllPermission objects for equality.

Returns the canonical string representation of the actions.

Returns the hash code value for this object.

Checks if the specified permission is "implied" by
this object.

Returns a new PermissionCollection object for storing AllPermission
objects.

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AllPermission

```java
public AllPermission()
```

Creates a new AllPermission object.

- AllPermission

```java
public AllPermission​(
String
name,

String
actions)
```

Creates a new AllPermission object. This
constructor exists for use by the

Policy

object
to instantiate new Permission objects.

**Parameters:** name

- ignored
**Parameters:** actions

- ignored.

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if the specified permission is "implied" by
this object. This method always returns true.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** return

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two AllPermission objects for equality. Two AllPermission
objects are always equal.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if

obj

is an AllPermission, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.

**Specified by:** getActions

in class

Permission
**Returns:** the actions.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing AllPermission
objects.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for
storing AllPermissions.

Constructor Detail

- AllPermission

```java
public AllPermission()
```

Creates a new AllPermission object.

- AllPermission

```java
public AllPermission​(
String
name,

String
actions)
```

Creates a new AllPermission object. This
constructor exists for use by the

Policy

object
to instantiate new Permission objects.

**Parameters:** name

- ignored
**Parameters:** actions

- ignored.

---

#### Constructor Detail

AllPermission

```java
public AllPermission()
```

Creates a new AllPermission object.

---

#### AllPermission

public AllPermission()

Creates a new AllPermission object.

AllPermission

```java
public AllPermission​(
String
name,

String
actions)
```

Creates a new AllPermission object. This
constructor exists for use by the

Policy

object
to instantiate new Permission objects.

**Parameters:** name

- ignored
**Parameters:** actions

- ignored.

---

#### AllPermission

public AllPermission​(

String

name,

String

actions)

Creates a new AllPermission object. This
constructor exists for use by the

Policy

object
to instantiate new Permission objects.

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if the specified permission is "implied" by
this object. This method always returns true.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** return

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two AllPermission objects for equality. Two AllPermission
objects are always equal.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if

obj

is an AllPermission, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.

**Specified by:** getActions

in class

Permission
**Returns:** the actions.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing AllPermission
objects.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for
storing AllPermissions.

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if the specified permission is "implied" by
this object. This method always returns true.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** return

---

#### implies

public boolean implies​(

Permission

p)

Checks if the specified permission is "implied" by
this object. This method always returns true.

equals

```java
public boolean equals​(
Object
obj)
```

Checks two AllPermission objects for equality. Two AllPermission
objects are always equal.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if

obj

is an AllPermission, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two AllPermission objects for equality. Two AllPermission
objects are always equal.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.

getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.

**Specified by:** getActions

in class

Permission
**Returns:** the actions.

---

#### getActions

public

String

getActions()

Returns the canonical string representation of the actions.

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing AllPermission
objects.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for
storing AllPermissions.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Returns a new PermissionCollection object for storing AllPermission
objects.

---

