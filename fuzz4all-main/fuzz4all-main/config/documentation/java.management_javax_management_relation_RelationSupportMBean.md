# Interface RelationSupportMBean

**Source:** `java.management\javax\management\relation\RelationSupportMBean.html`

### Class Description

```java
public interface
RelationSupportMBean

extends
Relation
```

A RelationSupport object is used internally by the Relation Service to
represent simple relations (only roles, no properties or methods), with an
unlimited number of roles, of any relation type. As internal representation,
it is not exposed to the user.

RelationSupport class conforms to the design patterns of standard MBean. So
the user can decide to instantiate a RelationSupport object himself as
a MBean (as it follows the MBean design patterns), to register it in the
MBean Server, and then to add it in the Relation Service.

The user can also, when creating his own MBean relation class, have it
extending RelationSupport, to retrieve the implementations of required
interfaces (see below).

It is also possible to have in a user relation MBean class a member
being a RelationSupport object, and to implement the required interfaces by
delegating all to this member.

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

**All Superinterfaces:** Relation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Boolean
isInRelationService()

Returns an internal flag specifying if the object is still handled by
the Relation Service.

**Returns:**
- a Boolean equal to

Boolean.TRUE

if the object
is still handled by the Relation Service and

Boolean.FALSE

otherwise.

---

#### void setRelationServiceManagementFlag​(
Boolean
flag)
throws
IllegalArgumentException

Specifies whether this relation is handled by the Relation
Service.

BEWARE, this method has to be exposed as the Relation Service will
access the relation through its management interface. It is RECOMMENDED
NOT to use this method. Using it does not affect the registration of the
relation object in the Relation Service, but will provide wrong
information about it!

**Parameters:**
- flag

- whether the relation is handled by the Relation Service.

**Throws:**
- IllegalArgumentException

- if null parameter

---

### Additional Sections

#### Interface RelationSupportMBean

**All Superinterfaces:** Relation

**All Known Implementing Classes:** RelationSupport

```java
public interface
RelationSupportMBean

extends
Relation
```

A RelationSupport object is used internally by the Relation Service to
represent simple relations (only roles, no properties or methods), with an
unlimited number of roles, of any relation type. As internal representation,
it is not exposed to the user.

RelationSupport class conforms to the design patterns of standard MBean. So
the user can decide to instantiate a RelationSupport object himself as
a MBean (as it follows the MBean design patterns), to register it in the
MBean Server, and then to add it in the Relation Service.

The user can also, when creating his own MBean relation class, have it
extending RelationSupport, to retrieve the implementations of required
interfaces (see below).

It is also possible to have in a user relation MBean class a member
being a RelationSupport object, and to implement the required interfaces by
delegating all to this member.

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

**Since:** 1.5

public interface

RelationSupportMBean

extends

Relation

A RelationSupport object is used internally by the Relation Service to
represent simple relations (only roles, no properties or methods), with an
unlimited number of roles, of any relation type. As internal representation,
it is not exposed to the user.

RelationSupport class conforms to the design patterns of standard MBean. So
the user can decide to instantiate a RelationSupport object himself as
a MBean (as it follows the MBean design patterns), to register it in the
MBean Server, and then to add it in the Relation Service.

The user can also, when creating his own MBean relation class, have it
extending RelationSupport, to retrieve the implementations of required
interfaces (see below).

It is also possible to have in a user relation MBean class a member
being a RelationSupport object, and to implement the required interfaces by
delegating all to this member.

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

RelationSupport class conforms to the design patterns of standard MBean. So
the user can decide to instantiate a RelationSupport object himself as
a MBean (as it follows the MBean design patterns), to register it in the
MBean Server, and then to add it in the Relation Service.

The user can also, when creating his own MBean relation class, have it
extending RelationSupport, to retrieve the implementations of required
interfaces (see below).

It is also possible to have in a user relation MBean class a member
being a RelationSupport object, and to implement the required interfaces by
delegating all to this member.

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

The user can also, when creating his own MBean relation class, have it
extending RelationSupport, to retrieve the implementations of required
interfaces (see below).

It is also possible to have in a user relation MBean class a member
being a RelationSupport object, and to implement the required interfaces by
delegating all to this member.

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

It is also possible to have in a user relation MBean class a member
being a RelationSupport object, and to implement the required interfaces by
delegating all to this member.

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

RelationSupport implements the Relation interface (to be handled by the
Relation Service).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Boolean

isInRelationService

()

Returns an internal flag specifying if the object is still handled by
the Relation Service.

void

setRelationServiceManagementFlag

​(

Boolean

flag)

Specifies whether this relation is handled by the Relation
Service.

- Methods declared in interface javax.management.relation.

Relation

getAllRoles

,

getReferencedMBeans

,

getRelationId

,

getRelationServiceName

,

getRelationTypeName

,

getRole

,

getRoleCardinality

,

getRoles

,

handleMBeanUnregistration

,

retrieveAllRoles

,

setRole

,

setRoles

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Boolean

isInRelationService

()

Returns an internal flag specifying if the object is still handled by
the Relation Service.

void

setRelationServiceManagementFlag

​(

Boolean

flag)

Specifies whether this relation is handled by the Relation
Service.

- Methods declared in interface javax.management.relation.

Relation

getAllRoles

,

getReferencedMBeans

,

getRelationId

,

getRelationServiceName

,

getRelationTypeName

,

getRole

,

getRoleCardinality

,

getRoles

,

handleMBeanUnregistration

,

retrieveAllRoles

,

setRole

,

setRoles

---

#### Method Summary

Returns an internal flag specifying if the object is still handled by
the Relation Service.

Specifies whether this relation is handled by the Relation
Service.

Methods declared in interface javax.management.relation.

Relation

getAllRoles

,

getReferencedMBeans

,

getRelationId

,

getRelationServiceName

,

getRelationTypeName

,

getRole

,

getRoleCardinality

,

getRoles

,

handleMBeanUnregistration

,

retrieveAllRoles

,

setRole

,

setRoles

---

#### Methods declared in interface javax.management.relation. Relation

============ METHOD DETAIL ==========

- Method Detail

- isInRelationService

```java
Boolean
isInRelationService()
```

Returns an internal flag specifying if the object is still handled by
the Relation Service.

**Returns:** a Boolean equal to

Boolean.TRUE

if the object
is still handled by the Relation Service and

Boolean.FALSE

otherwise.

- setRelationServiceManagementFlag

```java
void setRelationServiceManagementFlag​(
Boolean
flag)
throws
IllegalArgumentException
```

Specifies whether this relation is handled by the Relation
Service.

BEWARE, this method has to be exposed as the Relation Service will
access the relation through its management interface. It is RECOMMENDED
NOT to use this method. Using it does not affect the registration of the
relation object in the Relation Service, but will provide wrong
information about it!

**Parameters:** flag

- whether the relation is handled by the Relation Service.
**Throws:** IllegalArgumentException

- if null parameter

Method Detail

- isInRelationService

```java
Boolean
isInRelationService()
```

Returns an internal flag specifying if the object is still handled by
the Relation Service.

**Returns:** a Boolean equal to

Boolean.TRUE

if the object
is still handled by the Relation Service and

Boolean.FALSE

otherwise.

- setRelationServiceManagementFlag

```java
void setRelationServiceManagementFlag​(
Boolean
flag)
throws
IllegalArgumentException
```

Specifies whether this relation is handled by the Relation
Service.

BEWARE, this method has to be exposed as the Relation Service will
access the relation through its management interface. It is RECOMMENDED
NOT to use this method. Using it does not affect the registration of the
relation object in the Relation Service, but will provide wrong
information about it!

**Parameters:** flag

- whether the relation is handled by the Relation Service.
**Throws:** IllegalArgumentException

- if null parameter

---

#### Method Detail

isInRelationService

```java
Boolean
isInRelationService()
```

Returns an internal flag specifying if the object is still handled by
the Relation Service.

**Returns:** a Boolean equal to

Boolean.TRUE

if the object
is still handled by the Relation Service and

Boolean.FALSE

otherwise.

---

#### isInRelationService

Boolean

isInRelationService()

Returns an internal flag specifying if the object is still handled by
the Relation Service.

setRelationServiceManagementFlag

```java
void setRelationServiceManagementFlag​(
Boolean
flag)
throws
IllegalArgumentException
```

Specifies whether this relation is handled by the Relation
Service.

BEWARE, this method has to be exposed as the Relation Service will
access the relation through its management interface. It is RECOMMENDED
NOT to use this method. Using it does not affect the registration of the
relation object in the Relation Service, but will provide wrong
information about it!

**Parameters:** flag

- whether the relation is handled by the Relation Service.
**Throws:** IllegalArgumentException

- if null parameter

---

#### setRelationServiceManagementFlag

void setRelationServiceManagementFlag​(

Boolean

flag)
throws

IllegalArgumentException

Specifies whether this relation is handled by the Relation
Service.

BEWARE, this method has to be exposed as the Relation Service will
access the relation through its management interface. It is RECOMMENDED
NOT to use this method. Using it does not affect the registration of the
relation object in the Relation Service, but will provide wrong
information about it!

Specifies whether this relation is handled by the Relation
Service.

BEWARE, this method has to be exposed as the Relation Service will
access the relation through its management interface. It is RECOMMENDED
NOT to use this method. Using it does not affect the registration of the
relation object in the Relation Service, but will provide wrong
information about it!

---

