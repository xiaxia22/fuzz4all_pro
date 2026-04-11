# Class RelationTypeSupport

**Source:** `java.management\javax\management\relation\RelationTypeSupport.html`

### Class Description

```java
public class
RelationTypeSupport

extends
Object

implements
RelationType
```

A RelationTypeSupport object implements the RelationType interface.

It represents a relation type, providing role information for each role
expected to be supported in every relation of that type.

A relation type includes a relation type name and a list of
role infos (represented by RoleInfo objects).

A relation type has to be declared in the Relation Service:

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

**All Implemented Interfaces:** Serializable

,

RelationType

---

### Field Details

*No entries found.*

### Constructor Details

#### public RelationTypeSupport​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException

Constructor where all role definitions are dynamically created and
passed as parameter.

**Parameters:**
- relationTypeName

- Name of relation type
- roleInfoArray

- List of role definitions (RoleInfo objects)

**Throws:**
- IllegalArgumentException

- if null parameter
- InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

---

#### protected RelationTypeSupport​(
String
relationTypeName)

Constructor to be used for subclasses.

**Parameters:**
- relationTypeName

- Name of relation type.

**Throws:**
- IllegalArgumentException

- if null parameter.

---

### Method Details

#### public
String
getRelationTypeName()

Returns the relation type name.

**Specified by:**
- getRelationTypeName

in interface

RelationType

**Returns:**
- the relation type name.

---

#### public
List
<
RoleInfo
> getRoleInfos()

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Specified by:**
- getRoleInfos

in interface

RelationType

**Returns:**
- an

ArrayList

of

RoleInfo

.

---

#### public
RoleInfo
getRoleInfo​(
String
roleInfoName)
throws
IllegalArgumentException
,

RoleInfoNotFoundException

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

**Specified by:**
- getRoleInfo

in interface

RelationType

**Parameters:**
- roleInfoName

- role info name

**Returns:**
- RoleInfo object providing role definition
does not exist

**Throws:**
- IllegalArgumentException

- if null parameter
- RoleInfoNotFoundException

- if no role info with that name in
relation type.

---

#### protected void addRoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
,

InvalidRelationTypeException

Add a role info.
This method of course should not be used after the creation of the
relation type, because updating it would invalidate that the relations
created associated to that type still conform to it.
Can throw a RuntimeException if trying to update a relation type
declared in the Relation Service.

**Parameters:**
- roleInfo

- role info to be added.

**Throws:**
- IllegalArgumentException

- if null parameter.
- InvalidRelationTypeException

- if there is already a role
info in current relation type with the same name.

---

### Additional Sections

#### Class RelationTypeSupport

java.lang.Object

- javax.management.relation.RelationTypeSupport

javax.management.relation.RelationTypeSupport

**All Implemented Interfaces:** Serializable

,

RelationType

```java
public class
RelationTypeSupport

extends
Object

implements
RelationType
```

A RelationTypeSupport object implements the RelationType interface.

It represents a relation type, providing role information for each role
expected to be supported in every relation of that type.

A relation type includes a relation type name and a list of
role infos (represented by RoleInfo objects).

A relation type has to be declared in the Relation Service:

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

RelationTypeSupport

extends

Object

implements

RelationType

A RelationTypeSupport object implements the RelationType interface.

It represents a relation type, providing role information for each role
expected to be supported in every relation of that type.

A relation type includes a relation type name and a list of
role infos (represented by RoleInfo objects).

A relation type has to be declared in the Relation Service:

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

It represents a relation type, providing role information for each role
expected to be supported in every relation of that type.

A relation type includes a relation type name and a list of
role infos (represented by RoleInfo objects).

A relation type has to be declared in the Relation Service:

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

A relation type includes a relation type name and a list of
role infos (represented by RoleInfo objects).

A relation type has to be declared in the Relation Service:

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

A relation type has to be declared in the Relation Service:

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

- either using the createRelationType() method, where a RelationTypeSupport
object will be created and kept in the Relation Service

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

- either using the addRelationType() method where the user has to create
an object implementing the RelationType interface, and this object will be
used as representing a relation type in the Relation Service.

The

serialVersionUID

of this class is

4611072955724144607L

.

The

serialVersionUID

of this class is

4611072955724144607L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RelationTypeSupport

​(

String

relationTypeName)

Constructor to be used for subclasses.

RelationTypeSupport

​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)

Constructor where all role definitions are dynamically created and
passed as parameter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addRoleInfo

​(

RoleInfo

roleInfo)

Add a role info.

String

getRelationTypeName

()

Returns the relation type name.

RoleInfo

getRoleInfo

​(

String

roleInfoName)

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

List

<

RoleInfo

>

getRoleInfos

()

Returns the list of role definitions (ArrayList of RoleInfo objects).

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

Modifier

Constructor

Description

protected

RelationTypeSupport

​(

String

relationTypeName)

Constructor to be used for subclasses.

RelationTypeSupport

​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)

Constructor where all role definitions are dynamically created and
passed as parameter.

---

#### Constructor Summary

Constructor to be used for subclasses.

Constructor where all role definitions are dynamically created and
passed as parameter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addRoleInfo

​(

RoleInfo

roleInfo)

Add a role info.

String

getRelationTypeName

()

Returns the relation type name.

RoleInfo

getRoleInfo

​(

String

roleInfoName)

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

List

<

RoleInfo

>

getRoleInfos

()

Returns the list of role definitions (ArrayList of RoleInfo objects).

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

Add a role info.

Returns the relation type name.

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

Returns the list of role definitions (ArrayList of RoleInfo objects).

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

- RelationTypeSupport

```java
public RelationTypeSupport​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Constructor where all role definitions are dynamically created and
passed as parameter.

**Parameters:** relationTypeName

- Name of relation type
**Parameters:** roleInfoArray

- List of role definitions (RoleInfo objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- RelationTypeSupport

```java
protected RelationTypeSupport​(
String
relationTypeName)
```

Constructor to be used for subclasses.

**Parameters:** relationTypeName

- Name of relation type.
**Throws:** IllegalArgumentException

- if null parameter.

============ METHOD DETAIL ==========

- Method Detail

- getRelationTypeName

```java
public
String
getRelationTypeName()
```

Returns the relation type name.

**Specified by:** getRelationTypeName

in interface

RelationType
**Returns:** the relation type name.

- getRoleInfos

```java
public
List
<
RoleInfo
> getRoleInfos()
```

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Specified by:** getRoleInfos

in interface

RelationType
**Returns:** an

ArrayList

of

RoleInfo

.

- getRoleInfo

```java
public
RoleInfo
getRoleInfo​(
String
roleInfoName)
throws
IllegalArgumentException
,

RoleInfoNotFoundException
```

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

**Specified by:** getRoleInfo

in interface

RelationType
**Parameters:** roleInfoName

- role info name
**Returns:** RoleInfo object providing role definition
does not exist
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleInfoNotFoundException

- if no role info with that name in
relation type.

- addRoleInfo

```java
protected void addRoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Add a role info.
This method of course should not be used after the creation of the
relation type, because updating it would invalidate that the relations
created associated to that type still conform to it.
Can throw a RuntimeException if trying to update a relation type
declared in the Relation Service.

**Parameters:** roleInfo

- role info to be added.
**Throws:** IllegalArgumentException

- if null parameter.
**Throws:** InvalidRelationTypeException

- if there is already a role
info in current relation type with the same name.

Constructor Detail

- RelationTypeSupport

```java
public RelationTypeSupport​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Constructor where all role definitions are dynamically created and
passed as parameter.

**Parameters:** relationTypeName

- Name of relation type
**Parameters:** roleInfoArray

- List of role definitions (RoleInfo objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- RelationTypeSupport

```java
protected RelationTypeSupport​(
String
relationTypeName)
```

Constructor to be used for subclasses.

**Parameters:** relationTypeName

- Name of relation type.
**Throws:** IllegalArgumentException

- if null parameter.

---

#### Constructor Detail

RelationTypeSupport

```java
public RelationTypeSupport​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Constructor where all role definitions are dynamically created and
passed as parameter.

**Parameters:** relationTypeName

- Name of relation type
**Parameters:** roleInfoArray

- List of role definitions (RoleInfo objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

---

#### RelationTypeSupport

public RelationTypeSupport​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)
throws

IllegalArgumentException

,

InvalidRelationTypeException

Constructor where all role definitions are dynamically created and
passed as parameter.

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- no role info provided

- one null role info provided

- one null role info provided

RelationTypeSupport

```java
protected RelationTypeSupport​(
String
relationTypeName)
```

Constructor to be used for subclasses.

**Parameters:** relationTypeName

- Name of relation type.
**Throws:** IllegalArgumentException

- if null parameter.

---

#### RelationTypeSupport

protected RelationTypeSupport​(

String

relationTypeName)

Constructor to be used for subclasses.

Method Detail

- getRelationTypeName

```java
public
String
getRelationTypeName()
```

Returns the relation type name.

**Specified by:** getRelationTypeName

in interface

RelationType
**Returns:** the relation type name.

- getRoleInfos

```java
public
List
<
RoleInfo
> getRoleInfos()
```

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Specified by:** getRoleInfos

in interface

RelationType
**Returns:** an

ArrayList

of

RoleInfo

.

- getRoleInfo

```java
public
RoleInfo
getRoleInfo​(
String
roleInfoName)
throws
IllegalArgumentException
,

RoleInfoNotFoundException
```

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

**Specified by:** getRoleInfo

in interface

RelationType
**Parameters:** roleInfoName

- role info name
**Returns:** RoleInfo object providing role definition
does not exist
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleInfoNotFoundException

- if no role info with that name in
relation type.

- addRoleInfo

```java
protected void addRoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Add a role info.
This method of course should not be used after the creation of the
relation type, because updating it would invalidate that the relations
created associated to that type still conform to it.
Can throw a RuntimeException if trying to update a relation type
declared in the Relation Service.

**Parameters:** roleInfo

- role info to be added.
**Throws:** IllegalArgumentException

- if null parameter.
**Throws:** InvalidRelationTypeException

- if there is already a role
info in current relation type with the same name.

---

#### Method Detail

getRelationTypeName

```java
public
String
getRelationTypeName()
```

Returns the relation type name.

**Specified by:** getRelationTypeName

in interface

RelationType
**Returns:** the relation type name.

---

#### getRelationTypeName

public

String

getRelationTypeName()

Returns the relation type name.

getRoleInfos

```java
public
List
<
RoleInfo
> getRoleInfos()
```

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Specified by:** getRoleInfos

in interface

RelationType
**Returns:** an

ArrayList

of

RoleInfo

.

---

#### getRoleInfos

public

List

<

RoleInfo

> getRoleInfos()

Returns the list of role definitions (ArrayList of RoleInfo objects).

getRoleInfo

```java
public
RoleInfo
getRoleInfo​(
String
roleInfoName)
throws
IllegalArgumentException
,

RoleInfoNotFoundException
```

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

**Specified by:** getRoleInfo

in interface

RelationType
**Parameters:** roleInfoName

- role info name
**Returns:** RoleInfo object providing role definition
does not exist
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleInfoNotFoundException

- if no role info with that name in
relation type.

---

#### getRoleInfo

public

RoleInfo

getRoleInfo​(

String

roleInfoName)
throws

IllegalArgumentException

,

RoleInfoNotFoundException

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

addRoleInfo

```java
protected void addRoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Add a role info.
This method of course should not be used after the creation of the
relation type, because updating it would invalidate that the relations
created associated to that type still conform to it.
Can throw a RuntimeException if trying to update a relation type
declared in the Relation Service.

**Parameters:** roleInfo

- role info to be added.
**Throws:** IllegalArgumentException

- if null parameter.
**Throws:** InvalidRelationTypeException

- if there is already a role
info in current relation type with the same name.

---

#### addRoleInfo

protected void addRoleInfo​(

RoleInfo

roleInfo)
throws

IllegalArgumentException

,

InvalidRelationTypeException

Add a role info.
This method of course should not be used after the creation of the
relation type, because updating it would invalidate that the relations
created associated to that type still conform to it.
Can throw a RuntimeException if trying to update a relation type
declared in the Relation Service.

---

