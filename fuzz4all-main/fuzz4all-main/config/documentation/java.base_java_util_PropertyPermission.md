# Class PropertyPermission

**Source:** `java.base\java\util\PropertyPermission.html`

### Class Description

```java
public final class
PropertyPermission

extends
BasicPermission
```

This class is for property permissions.

The name is the name of the property ("java.home",
"os.name", etc). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "java.*" and "*" signify a wildcard
match, while "*java" and "a*b" do not.

The actions to be granted are passed to the constructor in a string containing
a list of one or more comma-separated keywords. The possible keywords are
"read" and "write". Their meaning is defined as follows:

The actions string is converted to lowercase before processing.

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public PropertyPermission​(
String
name,

String
actions)

Creates a new PropertyPermission object with the specified name.
The name is the name of the system property, and

actions

contains a comma-separated list of the
desired actions granted on the property. Possible actions are
"read" and "write".

**Parameters:**
- name

- the name of the PropertyPermission.
- actions

- the actions string.

**Throws:**
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty or if

actions

is invalid.

---

### Method Details

#### public boolean implies​(
Permission
p)

Checks if this PropertyPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

**Overrides:**
- implies

in class

BasicPermission

**Parameters:**
- p

- the permission to check against.

**Returns:**
- true if the specified permission is implied by this object,
false if not.

---

#### public boolean equals​(
Object
obj)

Checks two PropertyPermission objects for equality. Checks that

obj

is
a PropertyPermission, and has the same name and actions as this object.

**Overrides:**
- equals

in class

BasicPermission

**Parameters:**
- obj

- the object we are testing for equality with this object.

**Returns:**
- true if obj is a PropertyPermission, and has the same name and
actions as this PropertyPermission object.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.
The hash code used is the hash code of this permissions name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Overrides:**
- hashCode

in class

BasicPermission

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

Returns the "canonical string representation" of the actions.
That is, this method always returns present actions in the following order:
read, write. For example, if this PropertyPermission object
allows both write and read actions, a call to

getActions

will return the string "read,write".

**Overrides:**
- getActions

in class

BasicPermission

**Returns:**
- the canonical string representation of the actions.

---

#### public
PermissionCollection
newPermissionCollection()

Returns a new PermissionCollection object for storing
PropertyPermission objects.

**Overrides:**
- newPermissionCollection

in class

BasicPermission

**Returns:**
- a new PermissionCollection object suitable for storing
PropertyPermissions.

---

### Additional Sections

#### Class PropertyPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.util.PropertyPermission

java.security.Permission

- java.security.BasicPermission
- - java.util.PropertyPermission

java.security.BasicPermission

- java.util.PropertyPermission

java.util.PropertyPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
PropertyPermission

extends
BasicPermission
```

This class is for property permissions.

The name is the name of the property ("java.home",
"os.name", etc). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "java.*" and "*" signify a wildcard
match, while "*java" and "a*b" do not.

The actions to be granted are passed to the constructor in a string containing
a list of one or more comma-separated keywords. The possible keywords are
"read" and "write". Their meaning is defined as follows:

The actions string is converted to lowercase before processing.

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

**Since:** 1.2
**See Also:** BasicPermission

,

Permission

,

Permissions

,

PermissionCollection

,

SecurityManager

public final class

PropertyPermission

extends

BasicPermission

This class is for property permissions.

The name is the name of the property ("java.home",
"os.name", etc). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "java.*" and "*" signify a wildcard
match, while "*java" and "a*b" do not.

The actions to be granted are passed to the constructor in a string containing
a list of one or more comma-separated keywords. The possible keywords are
"read" and "write". Their meaning is defined as follows:

The actions string is converted to lowercase before processing.

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

The name is the name of the property ("java.home",
"os.name", etc). The naming
convention follows the hierarchical property naming convention.
Also, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example: "java.*" and "*" signify a wildcard
match, while "*java" and "a*b" do not.

The actions to be granted are passed to the constructor in a string containing
a list of one or more comma-separated keywords. The possible keywords are
"read" and "write". Their meaning is defined as follows:

The actions string is converted to lowercase before processing.

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

The actions to be granted are passed to the constructor in a string containing
a list of one or more comma-separated keywords. The possible keywords are
"read" and "write". Their meaning is defined as follows:

The actions string is converted to lowercase before processing.

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

The actions string is converted to lowercase before processing.

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

Care should be taken before granting code permission to access
certain system properties. For example, granting permission to
access the "java.home" system property gives potentially malevolent
code sensitive information about the system environment (the Java
installation directory). Also, granting permission to access
the "user.name" and "user.home" system properties gives potentially
malevolent code sensitive information about the user environment
(the user's account name and home directory).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PropertyPermission

​(

String

name,

String

actions)

Creates a new PropertyPermission object with the specified name.

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

Checks two PropertyPermission objects for equality.

String

getActions

()

Returns the "canonical string representation" of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this PropertyPermission object "implies" the specified
permission.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing
PropertyPermission objects.

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

PropertyPermission

​(

String

name,

String

actions)

Creates a new PropertyPermission object with the specified name.

---

#### Constructor Summary

Creates a new PropertyPermission object with the specified name.

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

Checks two PropertyPermission objects for equality.

String

getActions

()

Returns the "canonical string representation" of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this PropertyPermission object "implies" the specified
permission.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing
PropertyPermission objects.

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

Checks two PropertyPermission objects for equality.

Returns the "canonical string representation" of the actions.

Returns the hash code value for this object.

Checks if this PropertyPermission object "implies" the specified
permission.

Returns a new PermissionCollection object for storing
PropertyPermission objects.

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

- PropertyPermission

```java
public PropertyPermission​(
String
name,

String
actions)
```

Creates a new PropertyPermission object with the specified name.
The name is the name of the system property, and

actions

contains a comma-separated list of the
desired actions granted on the property. Possible actions are
"read" and "write".

**Parameters:** name

- the name of the PropertyPermission.
**Parameters:** actions

- the actions string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or if

actions

is invalid.

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this PropertyPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

**Overrides:** implies

in class

BasicPermission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two PropertyPermission objects for equality. Checks that

obj

is
a PropertyPermission, and has the same name and actions as this object.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is a PropertyPermission, and has the same name and
actions as this PropertyPermission object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.
The hash code used is the hash code of this permissions name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Overrides:** hashCode

in class

BasicPermission
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

Returns the "canonical string representation" of the actions.
That is, this method always returns present actions in the following order:
read, write. For example, if this PropertyPermission object
allows both write and read actions, a call to

getActions

will return the string "read,write".

**Overrides:** getActions

in class

BasicPermission
**Returns:** the canonical string representation of the actions.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing
PropertyPermission objects.

**Overrides:** newPermissionCollection

in class

BasicPermission
**Returns:** a new PermissionCollection object suitable for storing
PropertyPermissions.

Constructor Detail

- PropertyPermission

```java
public PropertyPermission​(
String
name,

String
actions)
```

Creates a new PropertyPermission object with the specified name.
The name is the name of the system property, and

actions

contains a comma-separated list of the
desired actions granted on the property. Possible actions are
"read" and "write".

**Parameters:** name

- the name of the PropertyPermission.
**Parameters:** actions

- the actions string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or if

actions

is invalid.

---

#### Constructor Detail

PropertyPermission

```java
public PropertyPermission​(
String
name,

String
actions)
```

Creates a new PropertyPermission object with the specified name.
The name is the name of the system property, and

actions

contains a comma-separated list of the
desired actions granted on the property. Possible actions are
"read" and "write".

**Parameters:** name

- the name of the PropertyPermission.
**Parameters:** actions

- the actions string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or if

actions

is invalid.

---

#### PropertyPermission

public PropertyPermission​(

String

name,

String

actions)

Creates a new PropertyPermission object with the specified name.
The name is the name of the system property, and

actions

contains a comma-separated list of the
desired actions granted on the property. Possible actions are
"read" and "write".

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this PropertyPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

**Overrides:** implies

in class

BasicPermission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two PropertyPermission objects for equality. Checks that

obj

is
a PropertyPermission, and has the same name and actions as this object.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is a PropertyPermission, and has the same name and
actions as this PropertyPermission object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.
The hash code used is the hash code of this permissions name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Overrides:** hashCode

in class

BasicPermission
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

Returns the "canonical string representation" of the actions.
That is, this method always returns present actions in the following order:
read, write. For example, if this PropertyPermission object
allows both write and read actions, a call to

getActions

will return the string "read,write".

**Overrides:** getActions

in class

BasicPermission
**Returns:** the canonical string representation of the actions.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing
PropertyPermission objects.

**Overrides:** newPermissionCollection

in class

BasicPermission
**Returns:** a new PermissionCollection object suitable for storing
PropertyPermissions.

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this PropertyPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

**Overrides:** implies

in class

BasicPermission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

---

#### implies

public boolean implies​(

Permission

p)

Checks if this PropertyPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

More specifically, this method returns true if:

- p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

p

is an instanceof PropertyPermission,

p

's actions are a subset of this
object's actions, and

p

's name is implied by this object's
name. For example, "java.*" implies "java.home".

equals

```java
public boolean equals​(
Object
obj)
```

Checks two PropertyPermission objects for equality. Checks that

obj

is
a PropertyPermission, and has the same name and actions as this object.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is a PropertyPermission, and has the same name and
actions as this PropertyPermission object.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two PropertyPermission objects for equality. Checks that

obj

is
a PropertyPermission, and has the same name and actions as this object.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.
The hash code used is the hash code of this permissions name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

**Overrides:** hashCode

in class

BasicPermission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.
The hash code used is the hash code of this permissions name, that is,

getName().hashCode()

, where

getName

is
from the Permission superclass.

getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions.
That is, this method always returns present actions in the following order:
read, write. For example, if this PropertyPermission object
allows both write and read actions, a call to

getActions

will return the string "read,write".

**Overrides:** getActions

in class

BasicPermission
**Returns:** the canonical string representation of the actions.

---

#### getActions

public

String

getActions()

Returns the "canonical string representation" of the actions.
That is, this method always returns present actions in the following order:
read, write. For example, if this PropertyPermission object
allows both write and read actions, a call to

getActions

will return the string "read,write".

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing
PropertyPermission objects.

**Overrides:** newPermissionCollection

in class

BasicPermission
**Returns:** a new PermissionCollection object suitable for storing
PropertyPermissions.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Returns a new PermissionCollection object for storing
PropertyPermission objects.

---

