# Interface RelationType

**Source:** `java.management\javax\management\relation\RelationType.html`

### Class Description

```java
public interface
RelationType

extends
Serializable
```

The RelationType interface has to be implemented by any class expected to
represent a relation type.

**All Superinterfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getRelationTypeName()

Returns the relation type name.

**Returns:**
- the relation type name.

---

#### List
<
RoleInfo
> getRoleInfos()

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Returns:**
- an

ArrayList

of

RoleInfo

.

---

#### RoleInfo
getRoleInfo​(
String
roleInfoName)
throws
IllegalArgumentException
,

RoleInfoNotFoundException

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

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

### Additional Sections

#### Interface RelationType

**All Superinterfaces:** Serializable

**All Known Implementing Classes:** RelationTypeSupport

```java
public interface
RelationType

extends
Serializable
```

The RelationType interface has to be implemented by any class expected to
represent a relation type.

**Since:** 1.5

public interface

RelationType

extends

Serializable

The RelationType interface has to be implemented by any class expected to
represent a relation type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

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

---

#### Method Summary

Returns the relation type name.

Returns the role info (RoleInfo object) for the given role info name
(null if not found).

Returns the list of role definitions (ArrayList of RoleInfo objects).

============ METHOD DETAIL ==========

- Method Detail

- getRelationTypeName

```java
String
getRelationTypeName()
```

Returns the relation type name.

**Returns:** the relation type name.

- getRoleInfos

```java
List
<
RoleInfo
> getRoleInfos()
```

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Returns:** an

ArrayList

of

RoleInfo

.

- getRoleInfo

```java
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

**Parameters:** roleInfoName

- role info name
**Returns:** RoleInfo object providing role definition
does not exist
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleInfoNotFoundException

- if no role info with that name in
relation type.

Method Detail

- getRelationTypeName

```java
String
getRelationTypeName()
```

Returns the relation type name.

**Returns:** the relation type name.

- getRoleInfos

```java
List
<
RoleInfo
> getRoleInfos()
```

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Returns:** an

ArrayList

of

RoleInfo

.

- getRoleInfo

```java
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

#### Method Detail

getRelationTypeName

```java
String
getRelationTypeName()
```

Returns the relation type name.

**Returns:** the relation type name.

---

#### getRelationTypeName

String

getRelationTypeName()

Returns the relation type name.

getRoleInfos

```java
List
<
RoleInfo
> getRoleInfos()
```

Returns the list of role definitions (ArrayList of RoleInfo objects).

**Returns:** an

ArrayList

of

RoleInfo

.

---

#### getRoleInfos

List

<

RoleInfo

> getRoleInfos()

Returns the list of role definitions (ArrayList of RoleInfo objects).

getRoleInfo

```java
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

---

