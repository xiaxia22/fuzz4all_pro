# Class RoleResult

**Source:** `java.management\javax\management\relation\RoleResult.html`

### Class Description

```java
public class
RoleResult

extends
Object

implements
Serializable
```

Represents the result of a multiple access to several roles of a relation
(either for reading or writing).

The

serialVersionUID

of this class is

-6304063118040985512L

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RoleResult​(
RoleList
list,

RoleUnresolvedList
unresolvedList)

Constructor.

**Parameters:**
- list

- list of roles successfully accessed.
- unresolvedList

- list of roles not accessed (with problem
descriptions).

---

### Method Details

#### public
RoleList
getRoles()

Retrieves list of roles successfully accessed.

**Returns:**
- a RoleList

**See Also:**
- setRoles(javax.management.relation.RoleList)

---

#### public
RoleUnresolvedList
getRolesUnresolved()

Retrieves list of roles unsuccessfully accessed.

**Returns:**
- a RoleUnresolvedList.

**See Also:**
- setRolesUnresolved(javax.management.relation.RoleUnresolvedList)

---

#### public void setRoles​(
RoleList
list)

Sets list of roles successfully accessed.

**Parameters:**
- list

- list of roles successfully accessed

**See Also:**
- getRoles()

---

#### public void setRolesUnresolved​(
RoleUnresolvedList
unresolvedList)

Sets list of roles unsuccessfully accessed.

**Parameters:**
- unresolvedList

- list of roles unsuccessfully accessed

**See Also:**
- getRolesUnresolved()

---

### Additional Sections

#### Class RoleResult

java.lang.Object

- javax.management.relation.RoleResult

javax.management.relation.RoleResult

**All Implemented Interfaces:** Serializable

```java
public class
RoleResult

extends
Object

implements
Serializable
```

Represents the result of a multiple access to several roles of a relation
(either for reading or writing).

The

serialVersionUID

of this class is

-6304063118040985512L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

RoleResult

extends

Object

implements

Serializable

Represents the result of a multiple access to several roles of a relation
(either for reading or writing).

The

serialVersionUID

of this class is

-6304063118040985512L

.

The

serialVersionUID

of this class is

-6304063118040985512L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RoleResult

​(

RoleList

list,

RoleUnresolvedList

unresolvedList)

Constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

RoleList

getRoles

()

Retrieves list of roles successfully accessed.

RoleUnresolvedList

getRolesUnresolved

()

Retrieves list of roles unsuccessfully accessed.

void

setRoles

​(

RoleList

list)

Sets list of roles successfully accessed.

void

setRolesUnresolved

​(

RoleUnresolvedList

unresolvedList)

Sets list of roles unsuccessfully accessed.

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

toString

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

RoleResult

​(

RoleList

list,

RoleUnresolvedList

unresolvedList)

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

RoleList

getRoles

()

Retrieves list of roles successfully accessed.

RoleUnresolvedList

getRolesUnresolved

()

Retrieves list of roles unsuccessfully accessed.

void

setRoles

​(

RoleList

list)

Sets list of roles successfully accessed.

void

setRolesUnresolved

​(

RoleUnresolvedList

unresolvedList)

Sets list of roles unsuccessfully accessed.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Retrieves list of roles successfully accessed.

Retrieves list of roles unsuccessfully accessed.

Sets list of roles successfully accessed.

Sets list of roles unsuccessfully accessed.

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

toString

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

- RoleResult

```java
public RoleResult​(
RoleList
list,

RoleUnresolvedList
unresolvedList)
```

Constructor.

**Parameters:** list

- list of roles successfully accessed.
**Parameters:** unresolvedList

- list of roles not accessed (with problem
descriptions).

============ METHOD DETAIL ==========

- Method Detail

- getRoles

```java
public
RoleList
getRoles()
```

Retrieves list of roles successfully accessed.

**Returns:** a RoleList
**See Also:** setRoles(javax.management.relation.RoleList)

- getRolesUnresolved

```java
public
RoleUnresolvedList
getRolesUnresolved()
```

Retrieves list of roles unsuccessfully accessed.

**Returns:** a RoleUnresolvedList.
**See Also:** setRolesUnresolved(javax.management.relation.RoleUnresolvedList)

- setRoles

```java
public void setRoles​(
RoleList
list)
```

Sets list of roles successfully accessed.

**Parameters:** list

- list of roles successfully accessed
**See Also:** getRoles()

- setRolesUnresolved

```java
public void setRolesUnresolved​(
RoleUnresolvedList
unresolvedList)
```

Sets list of roles unsuccessfully accessed.

**Parameters:** unresolvedList

- list of roles unsuccessfully accessed
**See Also:** getRolesUnresolved()

Constructor Detail

- RoleResult

```java
public RoleResult​(
RoleList
list,

RoleUnresolvedList
unresolvedList)
```

Constructor.

**Parameters:** list

- list of roles successfully accessed.
**Parameters:** unresolvedList

- list of roles not accessed (with problem
descriptions).

---

#### Constructor Detail

RoleResult

```java
public RoleResult​(
RoleList
list,

RoleUnresolvedList
unresolvedList)
```

Constructor.

**Parameters:** list

- list of roles successfully accessed.
**Parameters:** unresolvedList

- list of roles not accessed (with problem
descriptions).

---

#### RoleResult

public RoleResult​(

RoleList

list,

RoleUnresolvedList

unresolvedList)

Constructor.

Method Detail

- getRoles

```java
public
RoleList
getRoles()
```

Retrieves list of roles successfully accessed.

**Returns:** a RoleList
**See Also:** setRoles(javax.management.relation.RoleList)

- getRolesUnresolved

```java
public
RoleUnresolvedList
getRolesUnresolved()
```

Retrieves list of roles unsuccessfully accessed.

**Returns:** a RoleUnresolvedList.
**See Also:** setRolesUnresolved(javax.management.relation.RoleUnresolvedList)

- setRoles

```java
public void setRoles​(
RoleList
list)
```

Sets list of roles successfully accessed.

**Parameters:** list

- list of roles successfully accessed
**See Also:** getRoles()

- setRolesUnresolved

```java
public void setRolesUnresolved​(
RoleUnresolvedList
unresolvedList)
```

Sets list of roles unsuccessfully accessed.

**Parameters:** unresolvedList

- list of roles unsuccessfully accessed
**See Also:** getRolesUnresolved()

---

#### Method Detail

getRoles

```java
public
RoleList
getRoles()
```

Retrieves list of roles successfully accessed.

**Returns:** a RoleList
**See Also:** setRoles(javax.management.relation.RoleList)

---

#### getRoles

public

RoleList

getRoles()

Retrieves list of roles successfully accessed.

getRolesUnresolved

```java
public
RoleUnresolvedList
getRolesUnresolved()
```

Retrieves list of roles unsuccessfully accessed.

**Returns:** a RoleUnresolvedList.
**See Also:** setRolesUnresolved(javax.management.relation.RoleUnresolvedList)

---

#### getRolesUnresolved

public

RoleUnresolvedList

getRolesUnresolved()

Retrieves list of roles unsuccessfully accessed.

setRoles

```java
public void setRoles​(
RoleList
list)
```

Sets list of roles successfully accessed.

**Parameters:** list

- list of roles successfully accessed
**See Also:** getRoles()

---

#### setRoles

public void setRoles​(

RoleList

list)

Sets list of roles successfully accessed.

setRolesUnresolved

```java
public void setRolesUnresolved​(
RoleUnresolvedList
unresolvedList)
```

Sets list of roles unsuccessfully accessed.

**Parameters:** unresolvedList

- list of roles unsuccessfully accessed
**See Also:** getRolesUnresolved()

---

#### setRolesUnresolved

public void setRolesUnresolved​(

RoleUnresolvedList

unresolvedList)

Sets list of roles unsuccessfully accessed.

---

