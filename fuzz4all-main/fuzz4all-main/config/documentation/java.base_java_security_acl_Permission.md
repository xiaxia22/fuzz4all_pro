# Interface Permission

**Source:** `java.base\java\security\acl\Permission.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Permission
```

This interface represents a permission, such as that used to grant
a particular type of access to a resource.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean equals​(
Object
another)

Returns true if the object passed matches the permission represented
in this interface.

**Overrides:**
- equals

in class

Object

**Parameters:**
- another

- the Permission object to compare with.

**Returns:**
- true if the Permission objects are equal, false otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### String
toString()

Prints a string representation of this permission.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of the permission.

---

### Additional Sections

#### Interface Permission

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Permission
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.Policy

and related classes since 1.2.

This interface represents a permission, such as that used to grant
a particular type of access to a resource.

**Since:** 1.1

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Permission

This interface represents a permission, such as that used to grant
a particular type of access to a resource.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

another)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the object passed matches the permission represented
in this interface.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Prints a string representation of this permission.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

another)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the object passed matches the permission represented
in this interface.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Prints a string representation of this permission.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the object passed matches the permission represented
in this interface.

Prints a string representation of this permission.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
boolean equals​(
Object
another)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the object passed matches the permission represented
in this interface.

**Overrides:** equals

in class

Object
**Parameters:** another

- the Permission object to compare with.
**Returns:** true if the Permission objects are equal, false otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Prints a string representation of this permission.

**Overrides:** toString

in class

Object
**Returns:** the string representation of the permission.

Method Detail

- equals

```java
boolean equals​(
Object
another)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the object passed matches the permission represented
in this interface.

**Overrides:** equals

in class

Object
**Parameters:** another

- the Permission object to compare with.
**Returns:** true if the Permission objects are equal, false otherwise
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Prints a string representation of this permission.

**Overrides:** toString

in class

Object
**Returns:** the string representation of the permission.

---

#### Method Detail

equals

```java
boolean equals​(
Object
another)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the object passed matches the permission represented
in this interface.

**Overrides:** equals

in class

Object
**Parameters:** another

- the Permission object to compare with.
**Returns:** true if the Permission objects are equal, false otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

another)

Returns true if the object passed matches the permission represented
in this interface.

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Prints a string representation of this permission.

**Overrides:** toString

in class

Object
**Returns:** the string representation of the permission.

---

#### toString

String

toString()

Prints a string representation of this permission.

---

