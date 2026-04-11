# Class MBeanServerPermission

**Source:** `java.management\javax\management\MBeanServerPermission.html`

### Class Description

```java
public class
MBeanServerPermission

extends
BasicPermission
```

A Permission to perform actions related to MBeanServers.
The

name

of the permission specifies the operation requested
or granted by the permission. For a granted permission, it can be

*

to allow all of the MBeanServer operations specified below.
Otherwise, for a granted or requested permission, it must be one of the
following:

**createMBeanServer:** Create a new MBeanServer object using the method

MBeanServerFactory.createMBeanServer()

or

MBeanServerFactory.createMBeanServer(java.lang.String)

.

findMBeanServer

Find an MBeanServer with a given name, or all MBeanServers in this
JVM, using the method

MBeanServerFactory.findMBeanServer(java.lang.String)

.

newMBeanServer

Create a new MBeanServer object without keeping a reference to it,
using the method

MBeanServerFactory.newMBeanServer()

or

MBeanServerFactory.newMBeanServer(java.lang.String)

.

releaseMBeanServer

Remove the MBeanServerFactory's reference to an MBeanServer,
using the method

MBeanServerFactory.releaseMBeanServer(javax.management.MBeanServer)

.

The

name

of the permission can also denote a list of one or more
comma-separated operations. Spaces are allowed at the beginning and
end of the

name

and before and after commas.

MBeanServerPermission("createMBeanServer")

implies

MBeanServerPermission("newMBeanServer")

.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanServerPermission​(
String
name)

Create a new MBeanServerPermission with the given name.

This constructor is equivalent to

MBeanServerPermission(name,null)

.

**Parameters:**
- name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.

**Throws:**
- NullPointerException

- if the name is null.
- IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names.

---

#### public MBeanServerPermission​(
String
name,

String
actions)

Create a new MBeanServerPermission with the given name.

**Parameters:**
- name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
- actions

- the associated actions. This parameter is not
currently used and must be null or the empty string.

**Throws:**
- NullPointerException

- if the name is null.
- IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names, or if

actions

is a non-null
non-empty string.
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty or
if arguments are invalid.

---

### Method Details

#### public boolean implies​(
Permission
p)

Checks if this MBeanServerPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instance of MBeanServerPermission,
- p

's target names are a subset of this object's target
names

The

createMBeanServer

permission implies the

newMBeanServer

permission.

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

Checks two MBeanServerPermission objects for equality. Checks that

obj

is an MBeanServerPermission, and represents the same
list of allowable actions as this object.

**Overrides:**
- equals

in class

BasicPermission

**Parameters:**
- obj

- the object we are testing for equality with this object.

**Returns:**
- true if the objects are equal.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanServerPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - javax.management.MBeanServerPermission

java.security.Permission

- java.security.BasicPermission
- - javax.management.MBeanServerPermission

java.security.BasicPermission

- javax.management.MBeanServerPermission

javax.management.MBeanServerPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public class
MBeanServerPermission

extends
BasicPermission
```

A Permission to perform actions related to MBeanServers.
The

name

of the permission specifies the operation requested
or granted by the permission. For a granted permission, it can be

*

to allow all of the MBeanServer operations specified below.
Otherwise, for a granted or requested permission, it must be one of the
following:

**createMBeanServer:** Create a new MBeanServer object using the method

MBeanServerFactory.createMBeanServer()

or

MBeanServerFactory.createMBeanServer(java.lang.String)

.

findMBeanServer

Find an MBeanServer with a given name, or all MBeanServers in this
JVM, using the method

MBeanServerFactory.findMBeanServer(java.lang.String)

.

newMBeanServer

Create a new MBeanServer object without keeping a reference to it,
using the method

MBeanServerFactory.newMBeanServer()

or

MBeanServerFactory.newMBeanServer(java.lang.String)

.

releaseMBeanServer

Remove the MBeanServerFactory's reference to an MBeanServer,
using the method

MBeanServerFactory.releaseMBeanServer(javax.management.MBeanServer)

.

The

name

of the permission can also denote a list of one or more
comma-separated operations. Spaces are allowed at the beginning and
end of the

name

and before and after commas.

MBeanServerPermission("createMBeanServer")

implies

MBeanServerPermission("newMBeanServer")

.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanServerPermission

extends

BasicPermission

A Permission to perform actions related to MBeanServers.
The

name

of the permission specifies the operation requested
or granted by the permission. For a granted permission, it can be

*

to allow all of the MBeanServer operations specified below.
Otherwise, for a granted or requested permission, it must be one of the
following:

**createMBeanServer:** Create a new MBeanServer object using the method

MBeanServerFactory.createMBeanServer()

or

MBeanServerFactory.createMBeanServer(java.lang.String)

.

findMBeanServer

Find an MBeanServer with a given name, or all MBeanServers in this
JVM, using the method

MBeanServerFactory.findMBeanServer(java.lang.String)

.

newMBeanServer

Create a new MBeanServer object without keeping a reference to it,
using the method

MBeanServerFactory.newMBeanServer()

or

MBeanServerFactory.newMBeanServer(java.lang.String)

.

releaseMBeanServer

Remove the MBeanServerFactory's reference to an MBeanServer,
using the method

MBeanServerFactory.releaseMBeanServer(javax.management.MBeanServer)

.

The

name

of the permission can also denote a list of one or more
comma-separated operations. Spaces are allowed at the beginning and
end of the

name

and before and after commas.

MBeanServerPermission("createMBeanServer")

implies

MBeanServerPermission("newMBeanServer")

.

MBeanServerPermission("createMBeanServer")

implies

MBeanServerPermission("newMBeanServer")

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanServerPermission

​(

String

name)

Create a new MBeanServerPermission with the given name.

MBeanServerPermission

​(

String

name,

String

actions)

Create a new MBeanServerPermission with the given name.

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

Checks two MBeanServerPermission objects for equality.

boolean

implies

​(

Permission

p)

Checks if this MBeanServerPermission object "implies" the specified
permission.

- Methods declared in class java.security.

BasicPermission

getActions

,

hashCode

,

newPermissionCollection

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

MBeanServerPermission

​(

String

name)

Create a new MBeanServerPermission with the given name.

MBeanServerPermission

​(

String

name,

String

actions)

Create a new MBeanServerPermission with the given name.

---

#### Constructor Summary

Create a new MBeanServerPermission with the given name.

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

Checks two MBeanServerPermission objects for equality.

boolean

implies

​(

Permission

p)

Checks if this MBeanServerPermission object "implies" the specified
permission.

- Methods declared in class java.security.

BasicPermission

getActions

,

hashCode

,

newPermissionCollection

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

Checks two MBeanServerPermission objects for equality.

Checks if this MBeanServerPermission object "implies" the specified
permission.

Methods declared in class java.security.

BasicPermission

getActions

,

hashCode

,

newPermissionCollection

---

#### Methods declared in class java.security. BasicPermission

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

- MBeanServerPermission

```java
public MBeanServerPermission​(
String
name)
```

Create a new MBeanServerPermission with the given name.

This constructor is equivalent to

MBeanServerPermission(name,null)

.

**Parameters:** name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names.

- MBeanServerPermission

```java
public MBeanServerPermission​(
String
name,

String
actions)
```

Create a new MBeanServerPermission with the given name.

**Parameters:** name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
**Parameters:** actions

- the associated actions. This parameter is not
currently used and must be null or the empty string.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names, or if

actions

is a non-null
non-empty string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or
if arguments are invalid.

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this MBeanServerPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instance of MBeanServerPermission,
- p

's target names are a subset of this object's target
names

The

createMBeanServer

permission implies the

newMBeanServer

permission.

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

Checks two MBeanServerPermission objects for equality. Checks that

obj

is an MBeanServerPermission, and represents the same
list of allowable actions as this object.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if the objects are equal.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanServerPermission

```java
public MBeanServerPermission​(
String
name)
```

Create a new MBeanServerPermission with the given name.

This constructor is equivalent to

MBeanServerPermission(name,null)

.

**Parameters:** name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names.

- MBeanServerPermission

```java
public MBeanServerPermission​(
String
name,

String
actions)
```

Create a new MBeanServerPermission with the given name.

**Parameters:** name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
**Parameters:** actions

- the associated actions. This parameter is not
currently used and must be null or the empty string.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names, or if

actions

is a non-null
non-empty string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or
if arguments are invalid.

---

#### Constructor Detail

MBeanServerPermission

```java
public MBeanServerPermission​(
String
name)
```

Create a new MBeanServerPermission with the given name.

This constructor is equivalent to

MBeanServerPermission(name,null)

.

**Parameters:** name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names.

---

#### MBeanServerPermission

public MBeanServerPermission​(

String

name)

Create a new MBeanServerPermission with the given name.

This constructor is equivalent to

MBeanServerPermission(name,null)

.

Create a new MBeanServerPermission with the given name.

This constructor is equivalent to

MBeanServerPermission(name,null)

.

MBeanServerPermission

```java
public MBeanServerPermission​(
String
name,

String
actions)
```

Create a new MBeanServerPermission with the given name.

**Parameters:** name

- the name of the granted permission. It must
respect the constraints spelt out in the description of the

MBeanServerPermission

class.
**Parameters:** actions

- the associated actions. This parameter is not
currently used and must be null or the empty string.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is not

*

or one of the allowed names or a comma-separated
list of the allowed names, or if

actions

is a non-null
non-empty string.
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty or
if arguments are invalid.

---

#### MBeanServerPermission

public MBeanServerPermission​(

String

name,

String

actions)

Create a new MBeanServerPermission with the given name.

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this MBeanServerPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instance of MBeanServerPermission,
- p

's target names are a subset of this object's target
names

The

createMBeanServer

permission implies the

newMBeanServer

permission.

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

Checks two MBeanServerPermission objects for equality. Checks that

obj

is an MBeanServerPermission, and represents the same
list of allowable actions as this object.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if the objects are equal.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this MBeanServerPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instance of MBeanServerPermission,
- p

's target names are a subset of this object's target
names

The

createMBeanServer

permission implies the

newMBeanServer

permission.

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

Checks if this MBeanServerPermission object "implies" the specified
permission.

More specifically, this method returns true if:

- p

is an instance of MBeanServerPermission,
- p

's target names are a subset of this object's target
names

The

createMBeanServer

permission implies the

newMBeanServer

permission.

Checks if this MBeanServerPermission object "implies" the specified
permission.

More specifically, this method returns true if:

p

is an instance of MBeanServerPermission,

p

's target names are a subset of this object's target
names

The

createMBeanServer

permission implies the

newMBeanServer

permission.

equals

```java
public boolean equals​(
Object
obj)
```

Checks two MBeanServerPermission objects for equality. Checks that

obj

is an MBeanServerPermission, and represents the same
list of allowable actions as this object.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if the objects are equal.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two MBeanServerPermission objects for equality. Checks that

obj

is an MBeanServerPermission, and represents the same
list of allowable actions as this object.

---

