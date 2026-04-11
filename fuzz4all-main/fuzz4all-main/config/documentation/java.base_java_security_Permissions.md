# Class Permissions

**Source:** `java.base\java\security\Permissions.html`

### Class Description

```java
public final class
Permissions

extends
PermissionCollection

implements
Serializable
```

This class represents a heterogeneous collection of Permissions. That is,
it contains different types of Permission objects, organized into
PermissionCollections. For example, if any

java.io.FilePermission

objects are added to an instance of
this class, they are all stored in a single
PermissionCollection. It is the PermissionCollection returned by a call to
the

newPermissionCollection

method in the FilePermission class.
Similarly, any

java.lang.RuntimePermission

objects are
stored in the PermissionCollection returned by a call to the

newPermissionCollection

method in the
RuntimePermission class. Thus, this class represents a collection of
PermissionCollections.

When the

add

method is called to add a Permission, the
Permission is stored in the appropriate PermissionCollection. If no such
collection exists yet, the Permission object's class is determined and the

newPermissionCollection

method is called on that class to create
the PermissionCollection and add it to the Permissions object. If

newPermissionCollection

returns null, then a default
PermissionCollection that uses a hashtable will be created and used. Each
hashtable entry stores a Permission object as both the key and the value.

Enumerations returned via the

elements

method are
not

fail-fast

. Modifications to a collection should not be
performed while enumerating over that collection.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Permissions()

Creates a new Permissions object containing no PermissionCollections.

---

### Method Details

#### public void add​(
Permission
permission)

Adds a permission object to the PermissionCollection for the class the
permission belongs to. For example, if

permission

is a
FilePermission, it is added to the FilePermissionCollection stored
in this Permissions object.

This method creates
a new PermissionCollection object (and adds the permission to it)
if an appropriate collection does not yet exist.

**Specified by:**
- add

in class

PermissionCollection

**Parameters:**
- permission

- the Permission object to add.

**Throws:**
- SecurityException

- if this Permissions object is
marked as readonly.

**See Also:**
- PermissionCollection.isReadOnly()

---

#### public boolean implies​(
Permission
permission)

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object. Returns true if the
combination of permissions in the appropriate PermissionCollection
(e.g., a FilePermissionCollection for a FilePermission) together
imply the specified permission.

For example, suppose there is a FilePermissionCollection in this
Permissions object, and it contains one FilePermission that specifies
"read" access for all files in all subdirectories of the "/tmp"
directory, and another FilePermission that specifies "write" access
for all files in the "/tmp/scratch/foo" directory.
Then if the

implies

method
is called with a permission specifying both "read" and "write" access
to files in the "/tmp/scratch/foo" directory,

true

is
returned.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

**Specified by:**
- implies

in class

PermissionCollection

**Parameters:**
- permission

- the Permission object to check.

**Returns:**
- true if "permission" is implied by the permissions in the
PermissionCollection it
belongs to, false if not.

---

#### public
Enumeration
<
Permission
> elements()

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

**Specified by:**
- elements

in class

PermissionCollection

**Returns:**
- an enumeration of all the Permissions.

**See Also:**
- PermissionCollection.elementsAsStream()

---

### Additional Sections

#### Class Permissions

java.lang.Object

- java.security.PermissionCollection
- - java.security.Permissions

java.security.PermissionCollection

- java.security.Permissions

java.security.Permissions

**All Implemented Interfaces:** Serializable

```java
public final class
Permissions

extends
PermissionCollection

implements
Serializable
```

This class represents a heterogeneous collection of Permissions. That is,
it contains different types of Permission objects, organized into
PermissionCollections. For example, if any

java.io.FilePermission

objects are added to an instance of
this class, they are all stored in a single
PermissionCollection. It is the PermissionCollection returned by a call to
the

newPermissionCollection

method in the FilePermission class.
Similarly, any

java.lang.RuntimePermission

objects are
stored in the PermissionCollection returned by a call to the

newPermissionCollection

method in the
RuntimePermission class. Thus, this class represents a collection of
PermissionCollections.

When the

add

method is called to add a Permission, the
Permission is stored in the appropriate PermissionCollection. If no such
collection exists yet, the Permission object's class is determined and the

newPermissionCollection

method is called on that class to create
the PermissionCollection and add it to the Permissions object. If

newPermissionCollection

returns null, then a default
PermissionCollection that uses a hashtable will be created and used. Each
hashtable entry stores a Permission object as both the key and the value.

Enumerations returned via the

elements

method are
not

fail-fast

. Modifications to a collection should not be
performed while enumerating over that collection.

**Since:** 1.2
**See Also:** Permission

,

PermissionCollection

,

AllPermission

public final class

Permissions

extends

PermissionCollection

implements

Serializable

This class represents a heterogeneous collection of Permissions. That is,
it contains different types of Permission objects, organized into
PermissionCollections. For example, if any

java.io.FilePermission

objects are added to an instance of
this class, they are all stored in a single
PermissionCollection. It is the PermissionCollection returned by a call to
the

newPermissionCollection

method in the FilePermission class.
Similarly, any

java.lang.RuntimePermission

objects are
stored in the PermissionCollection returned by a call to the

newPermissionCollection

method in the
RuntimePermission class. Thus, this class represents a collection of
PermissionCollections.

When the

add

method is called to add a Permission, the
Permission is stored in the appropriate PermissionCollection. If no such
collection exists yet, the Permission object's class is determined and the

newPermissionCollection

method is called on that class to create
the PermissionCollection and add it to the Permissions object. If

newPermissionCollection

returns null, then a default
PermissionCollection that uses a hashtable will be created and used. Each
hashtable entry stores a Permission object as both the key and the value.

Enumerations returned via the

elements

method are
not

fail-fast

. Modifications to a collection should not be
performed while enumerating over that collection.

When the

add

method is called to add a Permission, the
Permission is stored in the appropriate PermissionCollection. If no such
collection exists yet, the Permission object's class is determined and the

newPermissionCollection

method is called on that class to create
the PermissionCollection and add it to the Permissions object. If

newPermissionCollection

returns null, then a default
PermissionCollection that uses a hashtable will be created and used. Each
hashtable entry stores a Permission object as both the key and the value.

Enumerations returned via the

elements

method are
not

fail-fast

. Modifications to a collection should not be
performed while enumerating over that collection.

Enumerations returned via the

elements

method are
not

fail-fast

. Modifications to a collection should not be
performed while enumerating over that collection.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Permissions

()

Creates a new Permissions object containing no PermissionCollections.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

Permission

permission)

Adds a permission object to the PermissionCollection for the class the
permission belongs to.

Enumeration

<

Permission

>

elements

()

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

boolean

implies

​(

Permission

permission)

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object.

- Methods declared in class java.security.

PermissionCollection

elementsAsStream

,

isReadOnly

,

setReadOnly

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

Permissions

()

Creates a new Permissions object containing no PermissionCollections.

---

#### Constructor Summary

Creates a new Permissions object containing no PermissionCollections.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

add

​(

Permission

permission)

Adds a permission object to the PermissionCollection for the class the
permission belongs to.

Enumeration

<

Permission

>

elements

()

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

boolean

implies

​(

Permission

permission)

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object.

- Methods declared in class java.security.

PermissionCollection

elementsAsStream

,

isReadOnly

,

setReadOnly

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

Adds a permission object to the PermissionCollection for the class the
permission belongs to.

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object.

Methods declared in class java.security.

PermissionCollection

elementsAsStream

,

isReadOnly

,

setReadOnly

,

toString

---

#### Methods declared in class java.security. PermissionCollection

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

- Permissions

```java
public Permissions()
```

Creates a new Permissions object containing no PermissionCollections.

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public void add​(
Permission
permission)
```

Adds a permission object to the PermissionCollection for the class the
permission belongs to. For example, if

permission

is a
FilePermission, it is added to the FilePermissionCollection stored
in this Permissions object.

This method creates
a new PermissionCollection object (and adds the permission to it)
if an appropriate collection does not yet exist.

**Specified by:** add

in class

PermissionCollection
**Parameters:** permission

- the Permission object to add.
**Throws:** SecurityException

- if this Permissions object is
marked as readonly.
**See Also:** PermissionCollection.isReadOnly()

- implies

```java
public boolean implies​(
Permission
permission)
```

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object. Returns true if the
combination of permissions in the appropriate PermissionCollection
(e.g., a FilePermissionCollection for a FilePermission) together
imply the specified permission.

For example, suppose there is a FilePermissionCollection in this
Permissions object, and it contains one FilePermission that specifies
"read" access for all files in all subdirectories of the "/tmp"
directory, and another FilePermission that specifies "write" access
for all files in the "/tmp/scratch/foo" directory.
Then if the

implies

method
is called with a permission specifying both "read" and "write" access
to files in the "/tmp/scratch/foo" directory,

true

is
returned.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

**Specified by:** implies

in class

PermissionCollection
**Parameters:** permission

- the Permission object to check.
**Returns:** true if "permission" is implied by the permissions in the
PermissionCollection it
belongs to, false if not.

- elements

```java
public
Enumeration
<
Permission
> elements()
```

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

**Specified by:** elements

in class

PermissionCollection
**Returns:** an enumeration of all the Permissions.
**See Also:** PermissionCollection.elementsAsStream()

Constructor Detail

- Permissions

```java
public Permissions()
```

Creates a new Permissions object containing no PermissionCollections.

---

#### Constructor Detail

Permissions

```java
public Permissions()
```

Creates a new Permissions object containing no PermissionCollections.

---

#### Permissions

public Permissions()

Creates a new Permissions object containing no PermissionCollections.

Method Detail

- add

```java
public void add​(
Permission
permission)
```

Adds a permission object to the PermissionCollection for the class the
permission belongs to. For example, if

permission

is a
FilePermission, it is added to the FilePermissionCollection stored
in this Permissions object.

This method creates
a new PermissionCollection object (and adds the permission to it)
if an appropriate collection does not yet exist.

**Specified by:** add

in class

PermissionCollection
**Parameters:** permission

- the Permission object to add.
**Throws:** SecurityException

- if this Permissions object is
marked as readonly.
**See Also:** PermissionCollection.isReadOnly()

- implies

```java
public boolean implies​(
Permission
permission)
```

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object. Returns true if the
combination of permissions in the appropriate PermissionCollection
(e.g., a FilePermissionCollection for a FilePermission) together
imply the specified permission.

For example, suppose there is a FilePermissionCollection in this
Permissions object, and it contains one FilePermission that specifies
"read" access for all files in all subdirectories of the "/tmp"
directory, and another FilePermission that specifies "write" access
for all files in the "/tmp/scratch/foo" directory.
Then if the

implies

method
is called with a permission specifying both "read" and "write" access
to files in the "/tmp/scratch/foo" directory,

true

is
returned.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

**Specified by:** implies

in class

PermissionCollection
**Parameters:** permission

- the Permission object to check.
**Returns:** true if "permission" is implied by the permissions in the
PermissionCollection it
belongs to, false if not.

- elements

```java
public
Enumeration
<
Permission
> elements()
```

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

**Specified by:** elements

in class

PermissionCollection
**Returns:** an enumeration of all the Permissions.
**See Also:** PermissionCollection.elementsAsStream()

---

#### Method Detail

add

```java
public void add​(
Permission
permission)
```

Adds a permission object to the PermissionCollection for the class the
permission belongs to. For example, if

permission

is a
FilePermission, it is added to the FilePermissionCollection stored
in this Permissions object.

This method creates
a new PermissionCollection object (and adds the permission to it)
if an appropriate collection does not yet exist.

**Specified by:** add

in class

PermissionCollection
**Parameters:** permission

- the Permission object to add.
**Throws:** SecurityException

- if this Permissions object is
marked as readonly.
**See Also:** PermissionCollection.isReadOnly()

---

#### add

public void add​(

Permission

permission)

Adds a permission object to the PermissionCollection for the class the
permission belongs to. For example, if

permission

is a
FilePermission, it is added to the FilePermissionCollection stored
in this Permissions object.

This method creates
a new PermissionCollection object (and adds the permission to it)
if an appropriate collection does not yet exist.

implies

```java
public boolean implies​(
Permission
permission)
```

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object. Returns true if the
combination of permissions in the appropriate PermissionCollection
(e.g., a FilePermissionCollection for a FilePermission) together
imply the specified permission.

For example, suppose there is a FilePermissionCollection in this
Permissions object, and it contains one FilePermission that specifies
"read" access for all files in all subdirectories of the "/tmp"
directory, and another FilePermission that specifies "write" access
for all files in the "/tmp/scratch/foo" directory.
Then if the

implies

method
is called with a permission specifying both "read" and "write" access
to files in the "/tmp/scratch/foo" directory,

true

is
returned.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

**Specified by:** implies

in class

PermissionCollection
**Parameters:** permission

- the Permission object to check.
**Returns:** true if "permission" is implied by the permissions in the
PermissionCollection it
belongs to, false if not.

---

#### implies

public boolean implies​(

Permission

permission)

Checks to see if this object's PermissionCollection for permissions of
the specified permission's class implies the permissions
expressed in the

permission

object. Returns true if the
combination of permissions in the appropriate PermissionCollection
(e.g., a FilePermissionCollection for a FilePermission) together
imply the specified permission.

For example, suppose there is a FilePermissionCollection in this
Permissions object, and it contains one FilePermission that specifies
"read" access for all files in all subdirectories of the "/tmp"
directory, and another FilePermission that specifies "write" access
for all files in the "/tmp/scratch/foo" directory.
Then if the

implies

method
is called with a permission specifying both "read" and "write" access
to files in the "/tmp/scratch/foo" directory,

true

is
returned.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

For example, suppose there is a FilePermissionCollection in this
Permissions object, and it contains one FilePermission that specifies
"read" access for all files in all subdirectories of the "/tmp"
directory, and another FilePermission that specifies "write" access
for all files in the "/tmp/scratch/foo" directory.
Then if the

implies

method
is called with a permission specifying both "read" and "write" access
to files in the "/tmp/scratch/foo" directory,

true

is
returned.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

Additionally, if this PermissionCollection contains the
AllPermission, this method will always return true.

elements

```java
public
Enumeration
<
Permission
> elements()
```

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

**Specified by:** elements

in class

PermissionCollection
**Returns:** an enumeration of all the Permissions.
**See Also:** PermissionCollection.elementsAsStream()

---

#### elements

public

Enumeration

<

Permission

> elements()

Returns an enumeration of all the Permission objects in all the
PermissionCollections in this Permissions object.

---

