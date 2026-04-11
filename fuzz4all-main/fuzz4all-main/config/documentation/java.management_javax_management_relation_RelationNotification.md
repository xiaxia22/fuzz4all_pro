# Class RelationNotification

**Source:** `java.management\javax\management\relation\RelationNotification.html`

### Class Description

```java
public class
RelationNotification

extends
Notification
```

A notification of a change in the Relation Service.
A RelationNotification notification is sent when a relation is created via
the Relation Service, or an MBean is added as a relation in the Relation
Service, or a role is updated in a relation, or a relation is removed from
the Relation Service.

The

serialVersionUID

of this class is

-6871117877523310399L

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
String
RELATION_BASIC_CREATION

Type for the creation of an internal relation.

**See Also:**
- Constant Field Values

---

#### public static final
String
RELATION_MBEAN_CREATION

Type for the relation MBean added into the Relation Service.

**See Also:**
- Constant Field Values

---

#### public static final
String
RELATION_BASIC_UPDATE

Type for an update of an internal relation.

**See Also:**
- Constant Field Values

---

#### public static final
String
RELATION_MBEAN_UPDATE

Type for the update of a relation MBean.

**See Also:**
- Constant Field Values

---

#### public static final
String
RELATION_BASIC_REMOVAL

Type for the removal from the Relation Service of an internal relation.

**See Also:**
- Constant Field Values

---

#### public static final
String
RELATION_MBEAN_REMOVAL

Type for the removal from the Relation Service of a relation MBean.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

**Parameters:**
- notifType

- type of the notification; either:

- RELATION_BASIC_CREATION

- RELATION_MBEAN_CREATION

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL
- sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
- sequence

- sequence number to identify the notification
- timeStamp

- time stamp
- message

- human-readable message describing the notification
- id

- relation id identifying the relation in the Relation
Service
- typeName

- name of the relation type
- objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
- unregMBeanList

- list of ObjectNames of referenced MBeans
expected to be unregistered due to relation removal (only for removal,
due to CIM qualifiers, can be null)

**Throws:**
- IllegalArgumentException

- if:

- no value for the notification type

- the notification type is not RELATION_BASIC_CREATION,
RELATION_MBEAN_CREATION, RELATION_BASIC_REMOVAL or
RELATION_MBEAN_REMOVAL

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

---

#### public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

String
name,

List
<
ObjectName
> newValue,

List
<
ObjectName
> oldValue)
throws
IllegalArgumentException

Creates a notification for a role update in a relation.

**Parameters:**
- notifType

- type of the notification; either:

- RELATION_BASIC_UPDATE

- RELATION_MBEAN_UPDATE
- sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
- sequence

- sequence number to identify the notification
- timeStamp

- time stamp
- message

- human-readable message describing the notification
- id

- relation id identifying the relation in the Relation
Service
- typeName

- name of the relation type
- objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
- name

- name of the updated role
- newValue

- new role value (List of ObjectName objects)
- oldValue

- old role value (List of ObjectName objects)

**Throws:**
- IllegalArgumentException

- if null parameter

---

### Method Details

#### public
String
getRelationId()

Returns the relation identifier of created/removed/updated relation.

**Returns:**
- the relation id.

---

#### public
String
getRelationTypeName()

Returns the relation type name of created/removed/updated relation.

**Returns:**
- the relation type name.

---

#### public
ObjectName
getObjectName()

Returns the ObjectName of the
created/removed/updated relation.

**Returns:**
- the ObjectName if the relation is an MBean, otherwise null.

---

#### public
List
<
ObjectName
> getMBeansToUnregister()

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

**Returns:**
- a

List

of

ObjectName

.

---

#### public
String
getRoleName()

Returns name of updated role of updated relation (only for role update).

**Returns:**
- the name of the updated role.

---

#### public
List
<
ObjectName
> getOldRoleValue()

Returns old value of updated role (only for role update).

**Returns:**
- the old value of the updated role.

---

#### public
List
<
ObjectName
> getNewRoleValue()

Returns new value of updated role (only for role update).

**Returns:**
- the new value of the updated role.

---

### Additional Sections

#### Class RelationNotification

java.lang.Object

- java.util.EventObject
- - javax.management.Notification
- - javax.management.relation.RelationNotification

java.util.EventObject

- javax.management.Notification
- - javax.management.relation.RelationNotification

javax.management.Notification

- javax.management.relation.RelationNotification

javax.management.relation.RelationNotification

**All Implemented Interfaces:** Serializable

```java
public class
RelationNotification

extends
Notification
```

A notification of a change in the Relation Service.
A RelationNotification notification is sent when a relation is created via
the Relation Service, or an MBean is added as a relation in the Relation
Service, or a role is updated in a relation, or a relation is removed from
the Relation Service.

The

serialVersionUID

of this class is

-6871117877523310399L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

RelationNotification

extends

Notification

A notification of a change in the Relation Service.
A RelationNotification notification is sent when a relation is created via
the Relation Service, or an MBean is added as a relation in the Relation
Service, or a role is updated in a relation, or a relation is removed from
the Relation Service.

The

serialVersionUID

of this class is

-6871117877523310399L

.

The

serialVersionUID

of this class is

-6871117877523310399L

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

RELATION_BASIC_CREATION

Type for the creation of an internal relation.

static

String

RELATION_BASIC_REMOVAL

Type for the removal from the Relation Service of an internal relation.

static

String

RELATION_BASIC_UPDATE

Type for an update of an internal relation.

static

String

RELATION_MBEAN_CREATION

Type for the relation MBean added into the Relation Service.

static

String

RELATION_MBEAN_REMOVAL

Type for the removal from the Relation Service of a relation MBean.

static

String

RELATION_MBEAN_UPDATE

Type for the update of a relation MBean.

- Fields declared in class javax.management.

Notification

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RelationNotification

​(

String

notifType,

Object

sourceObj,
long sequence,
long timeStamp,

String

message,

String

id,

String

typeName,

ObjectName

objectName,

String

name,

List

<

ObjectName

> newValue,

List

<

ObjectName

> oldValue)

Creates a notification for a role update in a relation.

RelationNotification

​(

String

notifType,

Object

sourceObj,
long sequence,
long timeStamp,

String

message,

String

id,

String

typeName,

ObjectName

objectName,

List

<

ObjectName

> unregMBeanList)

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

ObjectName

>

getMBeansToUnregister

()

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

List

<

ObjectName

>

getNewRoleValue

()

Returns new value of updated role (only for role update).

ObjectName

getObjectName

()

Returns the ObjectName of the
created/removed/updated relation.

List

<

ObjectName

>

getOldRoleValue

()

Returns old value of updated role (only for role update).

String

getRelationId

()

Returns the relation identifier of created/removed/updated relation.

String

getRelationTypeName

()

Returns the relation type name of created/removed/updated relation.

String

getRoleName

()

Returns name of updated role of updated relation (only for role update).

- Methods declared in class javax.management.

Notification

getMessage

,

getSequenceNumber

,

getTimeStamp

,

getType

,

getUserData

,

setSequenceNumber

,

setSource

,

setTimeStamp

,

setUserData

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

RELATION_BASIC_CREATION

Type for the creation of an internal relation.

static

String

RELATION_BASIC_REMOVAL

Type for the removal from the Relation Service of an internal relation.

static

String

RELATION_BASIC_UPDATE

Type for an update of an internal relation.

static

String

RELATION_MBEAN_CREATION

Type for the relation MBean added into the Relation Service.

static

String

RELATION_MBEAN_REMOVAL

Type for the removal from the Relation Service of a relation MBean.

static

String

RELATION_MBEAN_UPDATE

Type for the update of a relation MBean.

- Fields declared in class javax.management.

Notification

source

---

#### Field Summary

Type for the creation of an internal relation.

Type for the removal from the Relation Service of an internal relation.

Type for an update of an internal relation.

Type for the relation MBean added into the Relation Service.

Type for the removal from the Relation Service of a relation MBean.

Type for the update of a relation MBean.

Fields declared in class javax.management.

Notification

source

---

#### Fields declared in class javax.management. Notification

Constructor Summary

Constructors

Constructor

Description

RelationNotification

​(

String

notifType,

Object

sourceObj,
long sequence,
long timeStamp,

String

message,

String

id,

String

typeName,

ObjectName

objectName,

String

name,

List

<

ObjectName

> newValue,

List

<

ObjectName

> oldValue)

Creates a notification for a role update in a relation.

RelationNotification

​(

String

notifType,

Object

sourceObj,
long sequence,
long timeStamp,

String

message,

String

id,

String

typeName,

ObjectName

objectName,

List

<

ObjectName

> unregMBeanList)

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

---

#### Constructor Summary

Creates a notification for a role update in a relation.

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

ObjectName

>

getMBeansToUnregister

()

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

List

<

ObjectName

>

getNewRoleValue

()

Returns new value of updated role (only for role update).

ObjectName

getObjectName

()

Returns the ObjectName of the
created/removed/updated relation.

List

<

ObjectName

>

getOldRoleValue

()

Returns old value of updated role (only for role update).

String

getRelationId

()

Returns the relation identifier of created/removed/updated relation.

String

getRelationTypeName

()

Returns the relation type name of created/removed/updated relation.

String

getRoleName

()

Returns name of updated role of updated relation (only for role update).

- Methods declared in class javax.management.

Notification

getMessage

,

getSequenceNumber

,

getTimeStamp

,

getType

,

getUserData

,

setSequenceNumber

,

setSource

,

setTimeStamp

,

setUserData

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

Returns new value of updated role (only for role update).

Returns the ObjectName of the
created/removed/updated relation.

Returns old value of updated role (only for role update).

Returns the relation identifier of created/removed/updated relation.

Returns the relation type name of created/removed/updated relation.

Returns name of updated role of updated relation (only for role update).

Methods declared in class javax.management.

Notification

getMessage

,

getSequenceNumber

,

getTimeStamp

,

getType

,

getUserData

,

setSequenceNumber

,

setSource

,

setTimeStamp

,

setUserData

,

toString

---

#### Methods declared in class javax.management. Notification

Methods declared in class java.util.

EventObject

getSource

---

#### Methods declared in class java.util. EventObject

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

============ FIELD DETAIL ===========

- Field Detail

- RELATION_BASIC_CREATION

```java
public static final
String
RELATION_BASIC_CREATION
```

Type for the creation of an internal relation.

**See Also:** Constant Field Values

- RELATION_MBEAN_CREATION

```java
public static final
String
RELATION_MBEAN_CREATION
```

Type for the relation MBean added into the Relation Service.

**See Also:** Constant Field Values

- RELATION_BASIC_UPDATE

```java
public static final
String
RELATION_BASIC_UPDATE
```

Type for an update of an internal relation.

**See Also:** Constant Field Values

- RELATION_MBEAN_UPDATE

```java
public static final
String
RELATION_MBEAN_UPDATE
```

Type for the update of a relation MBean.

**See Also:** Constant Field Values

- RELATION_BASIC_REMOVAL

```java
public static final
String
RELATION_BASIC_REMOVAL
```

Type for the removal from the Relation Service of an internal relation.

**See Also:** Constant Field Values

- RELATION_MBEAN_REMOVAL

```java
public static final
String
RELATION_MBEAN_REMOVAL
```

Type for the removal from the Relation Service of a relation MBean.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RelationNotification

```java
public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
```

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

**Parameters:** notifType

- type of the notification; either:

- RELATION_BASIC_CREATION

- RELATION_MBEAN_CREATION

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL
**Parameters:** sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
**Parameters:** sequence

- sequence number to identify the notification
**Parameters:** timeStamp

- time stamp
**Parameters:** message

- human-readable message describing the notification
**Parameters:** id

- relation id identifying the relation in the Relation
Service
**Parameters:** typeName

- name of the relation type
**Parameters:** objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
**Parameters:** unregMBeanList

- list of ObjectNames of referenced MBeans
expected to be unregistered due to relation removal (only for removal,
due to CIM qualifiers, can be null)
**Throws:** IllegalArgumentException

- if:

- no value for the notification type

- the notification type is not RELATION_BASIC_CREATION,
RELATION_MBEAN_CREATION, RELATION_BASIC_REMOVAL or
RELATION_MBEAN_REMOVAL

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

- RelationNotification

```java
public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

String
name,

List
<
ObjectName
> newValue,

List
<
ObjectName
> oldValue)
throws
IllegalArgumentException
```

Creates a notification for a role update in a relation.

**Parameters:** notifType

- type of the notification; either:

- RELATION_BASIC_UPDATE

- RELATION_MBEAN_UPDATE
**Parameters:** sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
**Parameters:** sequence

- sequence number to identify the notification
**Parameters:** timeStamp

- time stamp
**Parameters:** message

- human-readable message describing the notification
**Parameters:** id

- relation id identifying the relation in the Relation
Service
**Parameters:** typeName

- name of the relation type
**Parameters:** objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
**Parameters:** name

- name of the updated role
**Parameters:** newValue

- new role value (List of ObjectName objects)
**Parameters:** oldValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter

============ METHOD DETAIL ==========

- Method Detail

- getRelationId

```java
public
String
getRelationId()
```

Returns the relation identifier of created/removed/updated relation.

**Returns:** the relation id.

- getRelationTypeName

```java
public
String
getRelationTypeName()
```

Returns the relation type name of created/removed/updated relation.

**Returns:** the relation type name.

- getObjectName

```java
public
ObjectName
getObjectName()
```

Returns the ObjectName of the
created/removed/updated relation.

**Returns:** the ObjectName if the relation is an MBean, otherwise null.

- getMBeansToUnregister

```java
public
List
<
ObjectName
> getMBeansToUnregister()
```

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

**Returns:** a

List

of

ObjectName

.

- getRoleName

```java
public
String
getRoleName()
```

Returns name of updated role of updated relation (only for role update).

**Returns:** the name of the updated role.

- getOldRoleValue

```java
public
List
<
ObjectName
> getOldRoleValue()
```

Returns old value of updated role (only for role update).

**Returns:** the old value of the updated role.

- getNewRoleValue

```java
public
List
<
ObjectName
> getNewRoleValue()
```

Returns new value of updated role (only for role update).

**Returns:** the new value of the updated role.

Field Detail

- RELATION_BASIC_CREATION

```java
public static final
String
RELATION_BASIC_CREATION
```

Type for the creation of an internal relation.

**See Also:** Constant Field Values

- RELATION_MBEAN_CREATION

```java
public static final
String
RELATION_MBEAN_CREATION
```

Type for the relation MBean added into the Relation Service.

**See Also:** Constant Field Values

- RELATION_BASIC_UPDATE

```java
public static final
String
RELATION_BASIC_UPDATE
```

Type for an update of an internal relation.

**See Also:** Constant Field Values

- RELATION_MBEAN_UPDATE

```java
public static final
String
RELATION_MBEAN_UPDATE
```

Type for the update of a relation MBean.

**See Also:** Constant Field Values

- RELATION_BASIC_REMOVAL

```java
public static final
String
RELATION_BASIC_REMOVAL
```

Type for the removal from the Relation Service of an internal relation.

**See Also:** Constant Field Values

- RELATION_MBEAN_REMOVAL

```java
public static final
String
RELATION_MBEAN_REMOVAL
```

Type for the removal from the Relation Service of a relation MBean.

**See Also:** Constant Field Values

---

#### Field Detail

RELATION_BASIC_CREATION

```java
public static final
String
RELATION_BASIC_CREATION
```

Type for the creation of an internal relation.

**See Also:** Constant Field Values

---

#### RELATION_BASIC_CREATION

public static final

String

RELATION_BASIC_CREATION

Type for the creation of an internal relation.

RELATION_MBEAN_CREATION

```java
public static final
String
RELATION_MBEAN_CREATION
```

Type for the relation MBean added into the Relation Service.

**See Also:** Constant Field Values

---

#### RELATION_MBEAN_CREATION

public static final

String

RELATION_MBEAN_CREATION

Type for the relation MBean added into the Relation Service.

RELATION_BASIC_UPDATE

```java
public static final
String
RELATION_BASIC_UPDATE
```

Type for an update of an internal relation.

**See Also:** Constant Field Values

---

#### RELATION_BASIC_UPDATE

public static final

String

RELATION_BASIC_UPDATE

Type for an update of an internal relation.

RELATION_MBEAN_UPDATE

```java
public static final
String
RELATION_MBEAN_UPDATE
```

Type for the update of a relation MBean.

**See Also:** Constant Field Values

---

#### RELATION_MBEAN_UPDATE

public static final

String

RELATION_MBEAN_UPDATE

Type for the update of a relation MBean.

RELATION_BASIC_REMOVAL

```java
public static final
String
RELATION_BASIC_REMOVAL
```

Type for the removal from the Relation Service of an internal relation.

**See Also:** Constant Field Values

---

#### RELATION_BASIC_REMOVAL

public static final

String

RELATION_BASIC_REMOVAL

Type for the removal from the Relation Service of an internal relation.

RELATION_MBEAN_REMOVAL

```java
public static final
String
RELATION_MBEAN_REMOVAL
```

Type for the removal from the Relation Service of a relation MBean.

**See Also:** Constant Field Values

---

#### RELATION_MBEAN_REMOVAL

public static final

String

RELATION_MBEAN_REMOVAL

Type for the removal from the Relation Service of a relation MBean.

Constructor Detail

- RelationNotification

```java
public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
```

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

**Parameters:** notifType

- type of the notification; either:

- RELATION_BASIC_CREATION

- RELATION_MBEAN_CREATION

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL
**Parameters:** sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
**Parameters:** sequence

- sequence number to identify the notification
**Parameters:** timeStamp

- time stamp
**Parameters:** message

- human-readable message describing the notification
**Parameters:** id

- relation id identifying the relation in the Relation
Service
**Parameters:** typeName

- name of the relation type
**Parameters:** objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
**Parameters:** unregMBeanList

- list of ObjectNames of referenced MBeans
expected to be unregistered due to relation removal (only for removal,
due to CIM qualifiers, can be null)
**Throws:** IllegalArgumentException

- if:

- no value for the notification type

- the notification type is not RELATION_BASIC_CREATION,
RELATION_MBEAN_CREATION, RELATION_BASIC_REMOVAL or
RELATION_MBEAN_REMOVAL

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

- RelationNotification

```java
public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

String
name,

List
<
ObjectName
> newValue,

List
<
ObjectName
> oldValue)
throws
IllegalArgumentException
```

Creates a notification for a role update in a relation.

**Parameters:** notifType

- type of the notification; either:

- RELATION_BASIC_UPDATE

- RELATION_MBEAN_UPDATE
**Parameters:** sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
**Parameters:** sequence

- sequence number to identify the notification
**Parameters:** timeStamp

- time stamp
**Parameters:** message

- human-readable message describing the notification
**Parameters:** id

- relation id identifying the relation in the Relation
Service
**Parameters:** typeName

- name of the relation type
**Parameters:** objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
**Parameters:** name

- name of the updated role
**Parameters:** newValue

- new role value (List of ObjectName objects)
**Parameters:** oldValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter

---

#### Constructor Detail

RelationNotification

```java
public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
```

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

**Parameters:** notifType

- type of the notification; either:

- RELATION_BASIC_CREATION

- RELATION_MBEAN_CREATION

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL
**Parameters:** sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
**Parameters:** sequence

- sequence number to identify the notification
**Parameters:** timeStamp

- time stamp
**Parameters:** message

- human-readable message describing the notification
**Parameters:** id

- relation id identifying the relation in the Relation
Service
**Parameters:** typeName

- name of the relation type
**Parameters:** objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
**Parameters:** unregMBeanList

- list of ObjectNames of referenced MBeans
expected to be unregistered due to relation removal (only for removal,
due to CIM qualifiers, can be null)
**Throws:** IllegalArgumentException

- if:

- no value for the notification type

- the notification type is not RELATION_BASIC_CREATION,
RELATION_MBEAN_CREATION, RELATION_BASIC_REMOVAL or
RELATION_MBEAN_REMOVAL

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

---

#### RelationNotification

public RelationNotification​(

String

notifType,

Object

sourceObj,
long sequence,
long timeStamp,

String

message,

String

id,

String

typeName,

ObjectName

objectName,

List

<

ObjectName

> unregMBeanList)
throws

IllegalArgumentException

Creates a notification for either a relation creation (RelationSupport
object created internally in the Relation Service, or an MBean added as a
relation) or for a relation removal from the Relation Service.

- RELATION_BASIC_CREATION

- RELATION_MBEAN_CREATION

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL

- RELATION_MBEAN_CREATION

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL

- RELATION_BASIC_REMOVAL

- RELATION_MBEAN_REMOVAL

- RELATION_MBEAN_REMOVAL

- no value for the notification type

- the notification type is not RELATION_BASIC_CREATION,
RELATION_MBEAN_CREATION, RELATION_BASIC_REMOVAL or
RELATION_MBEAN_REMOVAL

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

- the notification type is not RELATION_BASIC_CREATION,
RELATION_MBEAN_CREATION, RELATION_BASIC_REMOVAL or
RELATION_MBEAN_REMOVAL

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

- no source object

- the source object is not a Relation Service

- no relation id

- no relation type name

- the source object is not a Relation Service

- no relation id

- no relation type name

- no relation id

- no relation type name

- no relation type name

RelationNotification

```java
public RelationNotification​(
String
notifType,

Object
sourceObj,
long sequence,
long timeStamp,

String
message,

String
id,

String
typeName,

ObjectName
objectName,

String
name,

List
<
ObjectName
> newValue,

List
<
ObjectName
> oldValue)
throws
IllegalArgumentException
```

Creates a notification for a role update in a relation.

**Parameters:** notifType

- type of the notification; either:

- RELATION_BASIC_UPDATE

- RELATION_MBEAN_UPDATE
**Parameters:** sourceObj

- source object, sending the notification. This is either
an ObjectName or a RelationService object. In the latter case it must be
the MBean emitting the notification; the MBean Server will rewrite the
source to be the ObjectName under which that MBean is registered.
**Parameters:** sequence

- sequence number to identify the notification
**Parameters:** timeStamp

- time stamp
**Parameters:** message

- human-readable message describing the notification
**Parameters:** id

- relation id identifying the relation in the Relation
Service
**Parameters:** typeName

- name of the relation type
**Parameters:** objectName

- ObjectName of the relation object if it is an MBean
(null for relations internally handled by the Relation Service)
**Parameters:** name

- name of the updated role
**Parameters:** newValue

- new role value (List of ObjectName objects)
**Parameters:** oldValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter

---

#### RelationNotification

public RelationNotification​(

String

notifType,

Object

sourceObj,
long sequence,
long timeStamp,

String

message,

String

id,

String

typeName,

ObjectName

objectName,

String

name,

List

<

ObjectName

> newValue,

List

<

ObjectName

> oldValue)
throws

IllegalArgumentException

Creates a notification for a role update in a relation.

- RELATION_BASIC_UPDATE

- RELATION_MBEAN_UPDATE

- RELATION_MBEAN_UPDATE

Method Detail

- getRelationId

```java
public
String
getRelationId()
```

Returns the relation identifier of created/removed/updated relation.

**Returns:** the relation id.

- getRelationTypeName

```java
public
String
getRelationTypeName()
```

Returns the relation type name of created/removed/updated relation.

**Returns:** the relation type name.

- getObjectName

```java
public
ObjectName
getObjectName()
```

Returns the ObjectName of the
created/removed/updated relation.

**Returns:** the ObjectName if the relation is an MBean, otherwise null.

- getMBeansToUnregister

```java
public
List
<
ObjectName
> getMBeansToUnregister()
```

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

**Returns:** a

List

of

ObjectName

.

- getRoleName

```java
public
String
getRoleName()
```

Returns name of updated role of updated relation (only for role update).

**Returns:** the name of the updated role.

- getOldRoleValue

```java
public
List
<
ObjectName
> getOldRoleValue()
```

Returns old value of updated role (only for role update).

**Returns:** the old value of the updated role.

- getNewRoleValue

```java
public
List
<
ObjectName
> getNewRoleValue()
```

Returns new value of updated role (only for role update).

**Returns:** the new value of the updated role.

---

#### Method Detail

getRelationId

```java
public
String
getRelationId()
```

Returns the relation identifier of created/removed/updated relation.

**Returns:** the relation id.

---

#### getRelationId

public

String

getRelationId()

Returns the relation identifier of created/removed/updated relation.

getRelationTypeName

```java
public
String
getRelationTypeName()
```

Returns the relation type name of created/removed/updated relation.

**Returns:** the relation type name.

---

#### getRelationTypeName

public

String

getRelationTypeName()

Returns the relation type name of created/removed/updated relation.

getObjectName

```java
public
ObjectName
getObjectName()
```

Returns the ObjectName of the
created/removed/updated relation.

**Returns:** the ObjectName if the relation is an MBean, otherwise null.

---

#### getObjectName

public

ObjectName

getObjectName()

Returns the ObjectName of the
created/removed/updated relation.

getMBeansToUnregister

```java
public
List
<
ObjectName
> getMBeansToUnregister()
```

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

**Returns:** a

List

of

ObjectName

.

---

#### getMBeansToUnregister

public

List

<

ObjectName

> getMBeansToUnregister()

Returns the list of ObjectNames of MBeans expected to be unregistered
due to a relation removal (only for relation removal).

getRoleName

```java
public
String
getRoleName()
```

Returns name of updated role of updated relation (only for role update).

**Returns:** the name of the updated role.

---

#### getRoleName

public

String

getRoleName()

Returns name of updated role of updated relation (only for role update).

getOldRoleValue

```java
public
List
<
ObjectName
> getOldRoleValue()
```

Returns old value of updated role (only for role update).

**Returns:** the old value of the updated role.

---

#### getOldRoleValue

public

List

<

ObjectName

> getOldRoleValue()

Returns old value of updated role (only for role update).

getNewRoleValue

```java
public
List
<
ObjectName
> getNewRoleValue()
```

Returns new value of updated role (only for role update).

**Returns:** the new value of the updated role.

---

#### getNewRoleValue

public

List

<

ObjectName

> getNewRoleValue()

Returns new value of updated role (only for role update).

---

