# Class RoleUnresolved

**Source:** `java.management\javax\management\relation\RoleUnresolved.html`

### Class Description

```java
public class
RoleUnresolved

extends
Object

implements
Serializable
```

Represents an unresolved role: a role not retrieved from a relation due
to a problem. It provides the role name, value (if problem when trying to
set the role) and an integer defining the problem (constants defined in
RoleStatus).

The

serialVersionUID

of this class is

-48350262537070138L

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RoleUnresolved​(
String
name,

List
<
ObjectName
> value,
int pbType)
throws
IllegalArgumentException

Constructor.

**Parameters:**
- name

- name of the role
- value

- value of the role (if problem when setting the
role)
- pbType

- type of problem (according to known problem types,
listed as static final members).

**Throws:**
- IllegalArgumentException

- if null parameter or incorrect
problem type

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
- an ArrayList of ObjectName objects, the one provided to be set
in given role. Null if the unresolved role is returned for a read
access.

**See Also:**
- setRoleValue(java.util.List<javax.management.ObjectName>)

---

#### public int getProblemType()

Retrieves problem type.

**Returns:**
- an integer corresponding to a problem, those being described as
static final members of current class.

**See Also:**
- setProblemType(int)

---

#### public void setRoleName​(
String
name)
throws
IllegalArgumentException

Sets role name.

**Parameters:**
- name

- the new role name.

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
> value)

Sets role value.

**Parameters:**
- value

- List of ObjectName objects for referenced
MBeans not set in role.

**See Also:**
- getRoleValue()

---

#### public void setProblemType​(int pbType)
throws
IllegalArgumentException

Sets problem type.

**Parameters:**
- pbType

- integer corresponding to a problem. Must be one of
those described as static final members of current class.

**Throws:**
- IllegalArgumentException

- if incorrect problem type

**See Also:**
- getProblemType()

---

#### public
Object
clone()

Clone this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- an independent clone.

**See Also:**
- Cloneable

---

#### public
String
toString()

Return a string describing this object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a description of this RoleUnresolved object.

---

### Additional Sections

#### Class RoleUnresolved

java.lang.Object

- javax.management.relation.RoleUnresolved

javax.management.relation.RoleUnresolved

**All Implemented Interfaces:** Serializable

```java
public class
RoleUnresolved

extends
Object

implements
Serializable
```

Represents an unresolved role: a role not retrieved from a relation due
to a problem. It provides the role name, value (if problem when trying to
set the role) and an integer defining the problem (constants defined in
RoleStatus).

The

serialVersionUID

of this class is

-48350262537070138L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

RoleUnresolved

extends

Object

implements

Serializable

Represents an unresolved role: a role not retrieved from a relation due
to a problem. It provides the role name, value (if problem when trying to
set the role) and an integer defining the problem (constants defined in
RoleStatus).

The

serialVersionUID

of this class is

-48350262537070138L

.

The

serialVersionUID

of this class is

-48350262537070138L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RoleUnresolved

​(

String

name,

List

<

ObjectName

> value,
int pbType)

Constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clone this object.

int

getProblemType

()

Retrieves problem type.

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

void

setProblemType

​(int pbType)

Sets problem type.

void

setRoleName

​(

String

name)

Sets role name.

void

setRoleValue

​(

List

<

ObjectName

> value)

Sets role value.

String

toString

()

Return a string describing this object.

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

RoleUnresolved

​(

String

name,

List

<

ObjectName

> value,
int pbType)

Constructor.

---

#### Constructor Summary

Constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Clone this object.

int

getProblemType

()

Retrieves problem type.

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

void

setProblemType

​(int pbType)

Sets problem type.

void

setRoleName

​(

String

name)

Sets role name.

void

setRoleValue

​(

List

<

ObjectName

> value)

Sets role value.

String

toString

()

Return a string describing this object.

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

Clone this object.

Retrieves problem type.

Retrieves role name.

Retrieves role value.

Sets problem type.

Sets role name.

Sets role value.

Return a string describing this object.

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

- RoleUnresolved

```java
public RoleUnresolved​(
String
name,

List
<
ObjectName
> value,
int pbType)
throws
IllegalArgumentException
```

Constructor.

**Parameters:** name

- name of the role
**Parameters:** value

- value of the role (if problem when setting the
role)
**Parameters:** pbType

- type of problem (according to known problem types,
listed as static final members).
**Throws:** IllegalArgumentException

- if null parameter or incorrect
problem type

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

**Returns:** an ArrayList of ObjectName objects, the one provided to be set
in given role. Null if the unresolved role is returned for a read
access.
**See Also:** setRoleValue(java.util.List<javax.management.ObjectName>)

- getProblemType

```java
public int getProblemType()
```

Retrieves problem type.

**Returns:** an integer corresponding to a problem, those being described as
static final members of current class.
**See Also:** setProblemType(int)

- setRoleName

```java
public void setRoleName​(
String
name)
throws
IllegalArgumentException
```

Sets role name.

**Parameters:** name

- the new role name.
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleName()

- setRoleValue

```java
public void setRoleValue​(
List
<
ObjectName
> value)
```

Sets role value.

**Parameters:** value

- List of ObjectName objects for referenced
MBeans not set in role.
**See Also:** getRoleValue()

- setProblemType

```java
public void setProblemType​(int pbType)
throws
IllegalArgumentException
```

Sets problem type.

**Parameters:** pbType

- integer corresponding to a problem. Must be one of
those described as static final members of current class.
**Throws:** IllegalArgumentException

- if incorrect problem type
**See Also:** getProblemType()

- clone

```java
public
Object
clone()
```

Clone this object.

**Overrides:** clone

in class

Object
**Returns:** an independent clone.
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Return a string describing this object.

**Overrides:** toString

in class

Object
**Returns:** a description of this RoleUnresolved object.

Constructor Detail

- RoleUnresolved

```java
public RoleUnresolved​(
String
name,

List
<
ObjectName
> value,
int pbType)
throws
IllegalArgumentException
```

Constructor.

**Parameters:** name

- name of the role
**Parameters:** value

- value of the role (if problem when setting the
role)
**Parameters:** pbType

- type of problem (according to known problem types,
listed as static final members).
**Throws:** IllegalArgumentException

- if null parameter or incorrect
problem type

---

#### Constructor Detail

RoleUnresolved

```java
public RoleUnresolved​(
String
name,

List
<
ObjectName
> value,
int pbType)
throws
IllegalArgumentException
```

Constructor.

**Parameters:** name

- name of the role
**Parameters:** value

- value of the role (if problem when setting the
role)
**Parameters:** pbType

- type of problem (according to known problem types,
listed as static final members).
**Throws:** IllegalArgumentException

- if null parameter or incorrect
problem type

---

#### RoleUnresolved

public RoleUnresolved​(

String

name,

List

<

ObjectName

> value,
int pbType)
throws

IllegalArgumentException

Constructor.

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

**Returns:** an ArrayList of ObjectName objects, the one provided to be set
in given role. Null if the unresolved role is returned for a read
access.
**See Also:** setRoleValue(java.util.List<javax.management.ObjectName>)

- getProblemType

```java
public int getProblemType()
```

Retrieves problem type.

**Returns:** an integer corresponding to a problem, those being described as
static final members of current class.
**See Also:** setProblemType(int)

- setRoleName

```java
public void setRoleName​(
String
name)
throws
IllegalArgumentException
```

Sets role name.

**Parameters:** name

- the new role name.
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleName()

- setRoleValue

```java
public void setRoleValue​(
List
<
ObjectName
> value)
```

Sets role value.

**Parameters:** value

- List of ObjectName objects for referenced
MBeans not set in role.
**See Also:** getRoleValue()

- setProblemType

```java
public void setProblemType​(int pbType)
throws
IllegalArgumentException
```

Sets problem type.

**Parameters:** pbType

- integer corresponding to a problem. Must be one of
those described as static final members of current class.
**Throws:** IllegalArgumentException

- if incorrect problem type
**See Also:** getProblemType()

- clone

```java
public
Object
clone()
```

Clone this object.

**Overrides:** clone

in class

Object
**Returns:** an independent clone.
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Return a string describing this object.

**Overrides:** toString

in class

Object
**Returns:** a description of this RoleUnresolved object.

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

**Returns:** an ArrayList of ObjectName objects, the one provided to be set
in given role. Null if the unresolved role is returned for a read
access.
**See Also:** setRoleValue(java.util.List<javax.management.ObjectName>)

---

#### getRoleValue

public

List

<

ObjectName

> getRoleValue()

Retrieves role value.

getProblemType

```java
public int getProblemType()
```

Retrieves problem type.

**Returns:** an integer corresponding to a problem, those being described as
static final members of current class.
**See Also:** setProblemType(int)

---

#### getProblemType

public int getProblemType()

Retrieves problem type.

setRoleName

```java
public void setRoleName​(
String
name)
throws
IllegalArgumentException
```

Sets role name.

**Parameters:** name

- the new role name.
**Throws:** IllegalArgumentException

- if null parameter
**See Also:** getRoleName()

---

#### setRoleName

public void setRoleName​(

String

name)
throws

IllegalArgumentException

Sets role name.

setRoleValue

```java
public void setRoleValue​(
List
<
ObjectName
> value)
```

Sets role value.

**Parameters:** value

- List of ObjectName objects for referenced
MBeans not set in role.
**See Also:** getRoleValue()

---

#### setRoleValue

public void setRoleValue​(

List

<

ObjectName

> value)

Sets role value.

setProblemType

```java
public void setProblemType​(int pbType)
throws
IllegalArgumentException
```

Sets problem type.

**Parameters:** pbType

- integer corresponding to a problem. Must be one of
those described as static final members of current class.
**Throws:** IllegalArgumentException

- if incorrect problem type
**See Also:** getProblemType()

---

#### setProblemType

public void setProblemType​(int pbType)
throws

IllegalArgumentException

Sets problem type.

clone

```java
public
Object
clone()
```

Clone this object.

**Overrides:** clone

in class

Object
**Returns:** an independent clone.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Clone this object.

toString

```java
public
String
toString()
```

Return a string describing this object.

**Overrides:** toString

in class

Object
**Returns:** a description of this RoleUnresolved object.

---

#### toString

public

String

toString()

Return a string describing this object.

---

