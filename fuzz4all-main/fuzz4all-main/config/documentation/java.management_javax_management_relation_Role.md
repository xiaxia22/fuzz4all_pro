# Class Role

**Source:** `java.management\javax\management\relation\Role.html`

### Class Description

```java
public class
Role

extends
Object

implements
Serializable
```

Represents a role: includes a role name and referenced MBeans (via their
ObjectNames). The role value is always represented as an ArrayList
collection (of ObjectNames) to homogenize the access.

The

serialVersionUID

of this class is

-279985518429862552L

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Role​(
String
roleName,

List
<
ObjectName
> roleValue)
throws
IllegalArgumentException

Make a new Role object.
No check is made that the ObjectNames in the role value exist in
an MBean server. That check will be made when the role is set
in a relation.

**Parameters:**
- roleName

- role name
- roleValue

- role value (List of ObjectName objects)

**Throws:**
- IllegalArgumentException

- if null parameter

---

### Method Details

#### public
String
getRoleName()

Retrieves role name.

**Returns:**
- the role name.

**See Also:**
- setRoleName(java.lang.String)

---

#### public
List
<
ObjectName
> getRoleValue()

Retrieves role value.

**Returns:**
- ArrayList of ObjectName objects for referenced MBeans.

**See Also:**
- setRoleValue(java.util.List<javax.management.ObjectName>)

---

#### public void setRoleName​(
String
roleName)
throws
IllegalArgumentException

Sets role name.

**Parameters:**
- roleName

- role name

**Throws:**
- IllegalArgumentException

- if null parameter

**See Also:**
- getRoleName()

---

#### public void setRoleValue​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException

Sets role value.

**Parameters:**
- roleValue

- List of ObjectName objects for referenced
MBeans.

**Throws:**
- IllegalArgumentException

- if null parameter

**See Also:**
- getRoleValue()

---

#### public
String
toString()

Returns a string describing the role.

**Overrides:**
- toString

in class

Object

**Returns:**
- the description of the role.

---

#### public
Object
clone()

Clone the role object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a Role that is an independent copy of the current Role object.

**See Also:**
- Cloneable

---

#### public static
String
roleValueToString​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException

Returns a string for the given role value.

**Parameters:**
- roleValue

- List of ObjectName objects

**Returns:**
- A String consisting of the ObjectNames separated by
newlines (\n).

**Throws:**
- IllegalArgumentException

- if null parameter

---

### Additional Sections

#### Class Role

java.lang.Object

- javax.management.relation.Role

javax.management.relation.Role

**All Implemented Interfaces:** Serializable

```java
public class
Role

extends
Object

implements
Serializable
```

Represents a role: includes a role name and referenced MBeans (via their
ObjectNames). The role value is always represented as an ArrayList
collection (of ObjectNames) to homogenize the access.

The

serialVersionUID

of this class is

-279985518429862552L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

Role

extends

Object

implements

Serializable

Represents a role: includes a role name and referenced MBeans (via their
ObjectNames). The role value is always represented as an ArrayList
collection (of ObjectNames) to homogenize the access.

The

serialVersionUID

of this class is

-279985518429862552L

.

The

serialVersionUID

of this class is

-279985518429862552L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Role

​(

String

roleName,

List

<

ObjectName

> roleValue)

Make a new Role object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clone the role object.

String

getRoleName

()

Retrieves role name.

List

<

ObjectName

>

getRoleValue

()

Retrieves role value.

static

String

roleValueToString

​(

List

<

ObjectName

> roleValue)

Returns a string for the given role value.

void

setRoleName

​(

String

roleName)

Sets role name.

void

setRoleValue

​(

List

<

ObjectName

> roleValue)

Sets role value.

String

toString

()

Returns a string describing the role.

- Methods declared in class java.lang.

Object

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

Role

​(

String

roleName,

List

<

ObjectName

> roleValue)

Make a new Role object.

---

#### Constructor Summary

Make a new Role object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clone the role object.

String

getRoleName

()

Retrieves role name.

List

<

ObjectName

>

getRoleValue

()

Retrieves role value.

static

String

roleValueToString

​(

List

<

ObjectName

> roleValue)

Returns a string for the given role value.

void

setRoleName

​(

String

roleName)

Sets role name.

void

setRoleValue

​(

List

<

ObjectName

> roleValue)

Sets role value.

String

toString

()

Returns a string describing the role.

- Methods declared in class java.lang.

Object

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

Clone the role object.

Retrieves role name.

Retrieves role value.

Returns a string for the given role value.

Sets role name.

Sets role value.

Returns a string describing the role.

Methods declared in class java.lang.

Object

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

- Role

```java
public Role​(
String
roleName,

List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Make a new Role object.
No check is made that the ObjectNames in the role value exist in
an MBean server. That check will be made when the role is set
in a relation.

**Parameters:** roleName

- role name
**Parameters:** roleValue

- role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter

============ METHOD DETAIL ==========

- Method Detail

- getRoleName

```java
public
String
getRoleName()
```

Retrieves role name.

**Returns:** the role name.
**See Also:** setRoleName(java.lang.String)

- getRoleValue

```java
public
List
<
ObjectName
> getRoleValue()
```

Retrieves role value.

**Returns:** ArrayList of ObjectName objects for referenced MBeans.
**See Also:** setRoleValue(java.util.List<javax.management.ObjectName>)

- setRoleName

```java
public void setRoleName​(
String
roleName)
throws
IllegalArgumentException
```

Sets role name.

**Parameters:** roleName

- role name
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleName()

- setRoleValue

```java
public void setRoleValue​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Sets role value.

**Parameters:** roleValue

- List of ObjectName objects for referenced
MBeans.
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleValue()

- toString

```java
public
String
toString()
```

Returns a string describing the role.

**Overrides:** toString

in class

Object
**Returns:** the description of the role.

- clone

```java
public
Object
clone()
```

Clone the role object.

**Overrides:** clone

in class

Object
**Returns:** a Role that is an independent copy of the current Role object.
**See Also:** Cloneable

- roleValueToString

```java
public static
String
roleValueToString​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Returns a string for the given role value.

**Parameters:** roleValue

- List of ObjectName objects
**Returns:** A String consisting of the ObjectNames separated by
newlines (\n).
**Throws:** IllegalArgumentException

- if null parameter

Constructor Detail

- Role

```java
public Role​(
String
roleName,

List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Make a new Role object.
No check is made that the ObjectNames in the role value exist in
an MBean server. That check will be made when the role is set
in a relation.

**Parameters:** roleName

- role name
**Parameters:** roleValue

- role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter

---

#### Constructor Detail

Role

```java
public Role​(
String
roleName,

List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Make a new Role object.
No check is made that the ObjectNames in the role value exist in
an MBean server. That check will be made when the role is set
in a relation.

**Parameters:** roleName

- role name
**Parameters:** roleValue

- role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter

---

#### Role

public Role​(

String

roleName,

List

<

ObjectName

> roleValue)
throws

IllegalArgumentException

Make a new Role object.
No check is made that the ObjectNames in the role value exist in
an MBean server. That check will be made when the role is set
in a relation.

Method Detail

- getRoleName

```java
public
String
getRoleName()
```

Retrieves role name.

**Returns:** the role name.
**See Also:** setRoleName(java.lang.String)

- getRoleValue

```java
public
List
<
ObjectName
> getRoleValue()
```

Retrieves role value.

**Returns:** ArrayList of ObjectName objects for referenced MBeans.
**See Also:** setRoleValue(java.util.List<javax.management.ObjectName>)

- setRoleName

```java
public void setRoleName​(
String
roleName)
throws
IllegalArgumentException
```

Sets role name.

**Parameters:** roleName

- role name
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleName()

- setRoleValue

```java
public void setRoleValue​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Sets role value.

**Parameters:** roleValue

- List of ObjectName objects for referenced
MBeans.
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleValue()

- toString

```java
public
String
toString()
```

Returns a string describing the role.

**Overrides:** toString

in class

Object
**Returns:** the description of the role.

- clone

```java
public
Object
clone()
```

Clone the role object.

**Overrides:** clone

in class

Object
**Returns:** a Role that is an independent copy of the current Role object.
**See Also:** Cloneable

- roleValueToString

```java
public static
String
roleValueToString​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Returns a string for the given role value.

**Parameters:** roleValue

- List of ObjectName objects
**Returns:** A String consisting of the ObjectNames separated by
newlines (\n).
**Throws:** IllegalArgumentException

- if null parameter

---

#### Method Detail

getRoleName

```java
public
String
getRoleName()
```

Retrieves role name.

**Returns:** the role name.
**See Also:** setRoleName(java.lang.String)

---

#### getRoleName

public

String

getRoleName()

Retrieves role name.

getRoleValue

```java
public
List
<
ObjectName
> getRoleValue()
```

Retrieves role value.

**Returns:** ArrayList of ObjectName objects for referenced MBeans.
**See Also:** setRoleValue(java.util.List<javax.management.ObjectName>)

---

#### getRoleValue

public

List

<

ObjectName

> getRoleValue()

Retrieves role value.

setRoleName

```java
public void setRoleName​(
String
roleName)
throws
IllegalArgumentException
```

Sets role name.

**Parameters:** roleName

- role name
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleName()

---

#### setRoleName

public void setRoleName​(

String

roleName)
throws

IllegalArgumentException

Sets role name.

setRoleValue

```java
public void setRoleValue​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Sets role value.

**Parameters:** roleValue

- List of ObjectName objects for referenced
MBeans.
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleValue()

---

#### setRoleValue

public void setRoleValue​(

List

<

ObjectName

> roleValue)
throws

IllegalArgumentException

Sets role value.

toString

```java
public
String
toString()
```

Returns a string describing the role.

**Overrides:** toString

in class

Object
**Returns:** the description of the role.

---

#### toString

public

String

toString()

Returns a string describing the role.

clone

```java
public
Object
clone()
```

Clone the role object.

**Overrides:** clone

in class

Object
**Returns:** a Role that is an independent copy of the current Role object.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Clone the role object.

roleValueToString

```java
public static
String
roleValueToString​(
List
<
ObjectName
> roleValue)
throws
IllegalArgumentException
```

Returns a string for the given role value.

**Parameters:** roleValue

- List of ObjectName objects
**Returns:** A String consisting of the ObjectNames separated by
newlines (\n).
**Throws:** IllegalArgumentException

- if null parameter

---

#### roleValueToString

public static

String

roleValueToString​(

List

<

ObjectName

> roleValue)
throws

IllegalArgumentException

Returns a string for the given role value.

---

