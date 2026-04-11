# Interface RelationServiceMBean

**Source:** `java.management\javax\management\relation\RelationServiceMBean.html`

### Class Description

```java
public interface
RelationServiceMBean
```

The Relation Service is in charge of creating and deleting relation types
and relations, of handling the consistency and of providing query
mechanisms.

**All Known Implementing Classes:** RelationService

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void isActive()
throws
RelationServiceNotRegisteredException

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Throws:**
- RelationServiceNotRegisteredException

- if it is not
registered

---

#### boolean getPurgeFlag()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Returns:**
- true if purges are immediate.

**See Also:**
- setPurgeFlag(boolean)

---

#### void setPurgeFlag​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Parameters:**
- purgeFlag

- flag

**See Also:**
- getPurgeFlag()

---

#### void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Parameters:**
- relationTypeName

- name of the relation type
- roleInfoArray

- array of role infos

**Throws:**
- IllegalArgumentException

- if null parameter
- InvalidRelationTypeException

- If:

- there is already a relation type with that name

- the same name has been used for two different role infos

- no role info provided

- one null role info provided

---

#### void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Parameters:**
- relationTypeObj

- relation type object (implementing the
RelationType interface)

**Throws:**
- IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
- InvalidRelationTypeException

- if there is already a relation
type with that name

---

#### List
<
String
> getAllRelationTypeNames()

Retrieves names of all known relation types.

**Returns:**
- ArrayList of relation type names (Strings)

---

#### List
<
RoleInfo
> getRoleInfos​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

**Parameters:**
- relationTypeName

- name of relation type

**Returns:**
- ArrayList of RoleInfo.

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationTypeNotFoundException

- if there is no relation type
with that name.

---

#### RoleInfo
getRoleInfo​(
String
relationTypeName,

String
roleInfoName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
,

RoleInfoNotFoundException

Retrieves role info for given role of a given relation type.

**Parameters:**
- relationTypeName

- name of relation type
- roleInfoName

- name of role

**Returns:**
- RoleInfo object.

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service
- RoleInfoNotFoundException

- if the role is not part of the
relation type.

---

#### void removeRelationType​(
String
relationTypeName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationTypeNotFoundException

Removes given relation type from Relation Service.

The relation objects of that type will be removed from the
Relation Service.

**Parameters:**
- relationTypeName

- name of the relation type to be removed

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- IllegalArgumentException

- if null parameter
- RelationTypeNotFoundException

- If there is no relation type
with that name

---

#### void createRelation​(
String
relationId,

String
relationTypeName,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RoleNotFoundException
,

InvalidRelationIdException
,

RelationTypeNotFoundException
,

InvalidRoleValueException

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Roles are initialized according to the role list provided in
parameter. The ones not initialized in this way are set to an empty
ArrayList of ObjectNames.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

**Parameters:**
- relationId

- relation identifier, to identify uniquely the relation
inside the Relation Service
- relationTypeName

- name of the relation type (has to be created
in the Relation Service)
- roleList

- role list to initialize roles of the relation (can
be null).

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- IllegalArgumentException

- if null parameter
- RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type
- InvalidRelationIdException

- if relation id already used
- RelationTypeNotFoundException

- if relation type not known in
Relation Service
- InvalidRoleValueException

- if:

- the same role name is used for two different roles

- the number of referenced MBeans in given value is less than
expected minimum degree

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

---

#### void addRelation​(
ObjectName
relationObjectName)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

NoSuchMethodException
,

InvalidRelationIdException
,

InstanceNotFoundException
,

InvalidRelationServiceException
,

RelationTypeNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Parameters:**
- relationObjectName

- ObjectName of the relation MBean to be added.

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- NoSuchMethodException

- If the MBean does not implement the
Relation interface
- InvalidRelationIdException

- if:

- no relation identifier in MBean

- the relation identifier is already used in the Relation Service
- InstanceNotFoundException

- if the MBean for given ObjectName
has not been registered
- InvalidRelationServiceException

- if:

- no Relation Service name in MBean

- the Relation Service name in the MBean is not the one of the
current Relation Service
- RelationTypeNotFoundException

- if:

- no relation type name in MBean

- the relation type name in MBean does not correspond to a relation
type created in the Relation Service
- InvalidRoleValueException

- if:

- the number of referenced MBeans in a role is less than
expected minimum degree

- the number of referenced MBeans in a role exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist
- RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type

---

#### ObjectName
isRelationMBean​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

**Parameters:**
- relationId

- relation id identifying the relation

**Returns:**
- ObjectName of the corresponding relation MBean, or null if
the relation is not an MBean.

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- there is no relation associated
to that id

---

#### String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Parameters:**
- objectName

- ObjectName of supposed relation

**Returns:**
- relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)

**Throws:**
- IllegalArgumentException

- if null parameter

---

#### Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException

Checks if there is a relation identified in Relation Service with given
relation id.

**Parameters:**
- relationId

- relation id identifying the relation

**Returns:**
- boolean: true if there is a relation, false else

**Throws:**
- IllegalArgumentException

- if null parameter

---

#### List
<
String
> getAllRelationIds()

Returns all the relation ids for all the relations handled by the
Relation Service.

**Returns:**
- ArrayList of String

---

#### Integer
checkRoleReading​(
String
roleName,

String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException

Checks if given Role can be read in a relation of the given type.

**Parameters:**
- roleName

- name of role to be checked
- relationTypeName

- name of the relation type

**Returns:**
- an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be read

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer corresponding to RoleStatus.ROLE_NOT_READABLE

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service

---

#### Integer
checkRoleWriting​(
Role
role,

String
relationTypeName,

Boolean
initFlag)
throws
IllegalArgumentException
,

RelationTypeNotFoundException

Checks if given Role can be set in a relation of given type.

**Parameters:**
- role

- role to be checked
- relationTypeName

- name of relation type
- initFlag

- flag to specify that the checking is done for the
initialization of a role, write access shall not be verified.

**Returns:**
- an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be set

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationTypeNotFoundException

- if unknown relation type

---

#### void sendRelationCreationNotification​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException

Sends a notification (RelationNotification) for a relation creation.
The notification type is:

- RelationNotification.RELATION_BASIC_CREATION if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

**Parameters:**
- relationId

- relation identifier of the updated relation

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if there is no relation for given
relation id

---

#### void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationNotFoundException

Sends a notification (RelationNotification) for a role update in the
given relation. The notification type is:

- RelationNotification.RELATION_BASIC_UPDATE if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

**Parameters:**
- relationId

- relation identifier of the updated relation
- newRole

- new role (name and new value)
- oldRoleValue

- old role value (List of ObjectName objects)

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if there is no relation for given
relation id

---

#### void sendRelationRemovalNotification​(
String
relationId,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
,

RelationNotFoundException

Sends a notification (RelationNotification) for a relation removal.
The notification type is:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

**Parameters:**
- relationId

- relation identifier of the updated relation
- unregMBeanList

- List of ObjectNames of MBeans expected
to be unregistered due to relation removal (can be null)

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if there is no relation for given
relation id

---

#### void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

RelationNotFoundException

Handles update of the Relation Service role map for the update of given
role in given relation.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

**Parameters:**
- relationId

- relation identifier of the updated relation
- newRole

- new role (name and new value)
- oldRoleValue

- old role value (List of ObjectName objects)

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- RelationNotFoundException

- if no relation for given id.

---

#### void removeRelation​(
String
relationId)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException

Removes given relation from the Relation Service.

A RelationNotification notification is sent, its type being:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

**Parameters:**
- relationId

- relation id of the relation to be removed

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation corresponding to
given relation id

---

#### void purgeRelations()
throws
RelationServiceNotRegisteredException

Purges the relations.

Depending on the purgeFlag value, this method is either called
automatically when a notification is received for the unregistration of
an MBean referenced in a relation (if the flag is set to true), or not
(if the flag is set to false).

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

---

#### Map
<
String
,​
List
<
String
>> findReferencingRelations​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException

Retrieves the relations where a given MBean is referenced.

This corresponds to the CIM "References" and "ReferenceNames"
operations.

**Parameters:**
- mbeanName

- ObjectName of MBean
- relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all relation types
are considered.
- roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be returned. Else all
roles are considered.

**Returns:**
- an HashMap, where the keys are the relation ids of the relations
where the MBean is referenced, and the value is, for each key,
an ArrayList of role names (as an MBean can be referenced in several
roles in the same relation).

**Throws:**
- IllegalArgumentException

- if null parameter

---

#### Map
<
ObjectName
,​
List
<
String
>> findAssociatedMBeans​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException

Retrieves the MBeans associated to given one in a relation.

This corresponds to CIM Associators and AssociatorNames operations.

**Parameters:**
- mbeanName

- ObjectName of MBean
- relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all
relation types are considered.
- roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be considered. Else all
roles are considered.

**Returns:**
- an HashMap, where the keys are the ObjectNames of the MBeans
associated to given MBean, and the value is, for each key, an ArrayList
of the relation ids of the relations where the key MBean is
associated to given one (as they can be associated in several different
relations).

**Throws:**
- IllegalArgumentException

- if null parameter

---

#### List
<
String
> findRelationsOfType​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException

Returns the relation ids for relations of the given type.

**Parameters:**
- relationTypeName

- relation type name

**Returns:**
- an ArrayList of relation ids.

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationTypeNotFoundException

- if there is no relation type
with that name.

---

#### List
<
ObjectName
> getRole​(
String
relationId,

String
roleName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException

Retrieves role value for given role name in given relation.

**Parameters:**
- relationId

- relation id
- roleName

- name of role

**Returns:**
- the ArrayList of ObjectName objects being the role value

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation with given id
- RoleNotFoundException

- if:

- there is no role with given name

or

- the role is not readable.

**See Also:**
- setRole(java.lang.String, javax.management.relation.Role)

---

#### RoleResult
getRoles​(
String
relationId,

String
[] roleNameArray)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException

Retrieves values of roles with given names in given relation.

**Parameters:**
- relationId

- relation id
- roleNameArray

- array of names of roles to be retrieved

**Returns:**
- a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
retrieved).

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation with given id

**See Also:**
- setRoles(java.lang.String, javax.management.relation.RoleList)

---

#### RoleResult
getAllRoles​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RelationServiceNotRegisteredException

Returns all roles present in the relation.

**Parameters:**
- relationId

- relation id

**Returns:**
- a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
readable).

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation for given id
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server

---

#### Integer
getRoleCardinality​(
String
relationId,

String
roleName)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException

Retrieves the number of MBeans currently referenced in the
given role.

**Parameters:**
- relationId

- relation id
- roleName

- name of role

**Returns:**
- the number of currently referenced MBeans in that role

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation with given id
- RoleNotFoundException

- if there is no role with given name

---

#### void setRole​(
String
relationId,

Role
role)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
,

RelationTypeNotFoundException

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:**
- relationId

- relation id
- role

- role to be set (name and new value)

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation with given id
- RoleNotFoundException

- if:

- internal relation

and

- the role does not exist or is not writable
- InvalidRoleValueException

- if internal relation and value
provided for role is not valid:

- the number of referenced MBeans in given value is less than
expected minimum degree

or

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist
- RelationTypeNotFoundException

- if unknown relation type

**See Also:**
- getRole(java.lang.String, java.lang.String)

---

#### RoleResult
setRoles​(
String
relationId,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException

Sets the given roles in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:**
- relationId

- relation id
- roleList

- list of roles to be set

**Returns:**
- a RoleResult object, including a RoleList (for roles
successfully set) and a RoleUnresolvedList (for roles not
set).

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation with given id

**See Also:**
- getRoles(java.lang.String, java.lang.String[])

---

#### Map
<
ObjectName
,​
List
<
String
>> getReferencedMBeans​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException

Retrieves MBeans referenced in the various roles of the relation.

**Parameters:**
- relationId

- relation id

**Returns:**
- a HashMap mapping:

ObjectName -> ArrayList of String (role
names)

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation for given
relation id

---

#### String
getRelationTypeName​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException

Returns name of associated relation type for given relation.

**Parameters:**
- relationId

- relation id

**Returns:**
- the name of the associated relation type.

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation for given
relation id

---

### Additional Sections

#### Interface RelationServiceMBean

**All Known Implementing Classes:** RelationService

```java
public interface
RelationServiceMBean
```

The Relation Service is in charge of creating and deleting relation types
and relations, of handling the consistency and of providing query
mechanisms.

**Since:** 1.5

public interface

RelationServiceMBean

The Relation Service is in charge of creating and deleting relation types
and relations, of handling the consistency and of providing query
mechanisms.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addRelation

​(

ObjectName

relationObjectName)

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

void

addRelationType

​(

RelationType

relationTypeObj)

Adds given object as a relation type.

Integer

checkRoleReading

​(

String

roleName,

String

relationTypeName)

Checks if given Role can be read in a relation of the given type.

Integer

checkRoleWriting

​(

Role

role,

String

relationTypeName,

Boolean

initFlag)

Checks if given Role can be set in a relation of given type.

void

createRelation

​(

String

relationId,

String

relationTypeName,

RoleList

roleList)

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

void

createRelationType

​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

Map

<

ObjectName

,​

List

<

String

>>

findAssociatedMBeans

​(

ObjectName

mbeanName,

String

relationTypeName,

String

roleName)

Retrieves the MBeans associated to given one in a relation.

Map

<

String

,​

List

<

String

>>

findReferencingRelations

​(

ObjectName

mbeanName,

String

relationTypeName,

String

roleName)

Retrieves the relations where a given MBean is referenced.

List

<

String

>

findRelationsOfType

​(

String

relationTypeName)

Returns the relation ids for relations of the given type.

List

<

String

>

getAllRelationIds

()

Returns all the relation ids for all the relations handled by the
Relation Service.

List

<

String

>

getAllRelationTypeNames

()

Retrieves names of all known relation types.

RoleResult

getAllRoles

​(

String

relationId)

Returns all roles present in the relation.

boolean

getPurgeFlag

()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

Map

<

ObjectName

,​

List

<

String

>>

getReferencedMBeans

​(

String

relationId)

Retrieves MBeans referenced in the various roles of the relation.

String

getRelationTypeName

​(

String

relationId)

Returns name of associated relation type for given relation.

List

<

ObjectName

>

getRole

​(

String

relationId,

String

roleName)

Retrieves role value for given role name in given relation.

Integer

getRoleCardinality

​(

String

relationId,

String

roleName)

Retrieves the number of MBeans currently referenced in the
given role.

RoleInfo

getRoleInfo

​(

String

relationTypeName,

String

roleInfoName)

Retrieves role info for given role of a given relation type.

List

<

RoleInfo

>

getRoleInfos

​(

String

relationTypeName)

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

RoleResult

getRoles

​(

String

relationId,

String

[] roleNameArray)

Retrieves values of roles with given names in given relation.

Boolean

hasRelation

​(

String

relationId)

Checks if there is a relation identified in Relation Service with given
relation id.

void

isActive

()

Checks if the Relation Service is active.

String

isRelation

​(

ObjectName

objectName)

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

ObjectName

isRelationMBean

​(

String

relationId)

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

void

purgeRelations

()

Purges the relations.

void

removeRelation

​(

String

relationId)

Removes given relation from the Relation Service.

void

removeRelationType

​(

String

relationTypeName)

Removes given relation type from Relation Service.

void

sendRelationCreationNotification

​(

String

relationId)

Sends a notification (RelationNotification) for a relation creation.

void

sendRelationRemovalNotification

​(

String

relationId,

List

<

ObjectName

> unregMBeanList)

Sends a notification (RelationNotification) for a relation removal.

void

sendRoleUpdateNotification

​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldRoleValue)

Sends a notification (RelationNotification) for a role update in the
given relation.

void

setPurgeFlag

​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

void

setRole

​(

String

relationId,

Role

role)

Sets the given role in given relation.

RoleResult

setRoles

​(

String

relationId,

RoleList

roleList)

Sets the given roles in given relation.

void

updateRoleMap

​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldRoleValue)

Handles update of the Relation Service role map for the update of given
role in given relation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addRelation

​(

ObjectName

relationObjectName)

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

void

addRelationType

​(

RelationType

relationTypeObj)

Adds given object as a relation type.

Integer

checkRoleReading

​(

String

roleName,

String

relationTypeName)

Checks if given Role can be read in a relation of the given type.

Integer

checkRoleWriting

​(

Role

role,

String

relationTypeName,

Boolean

initFlag)

Checks if given Role can be set in a relation of given type.

void

createRelation

​(

String

relationId,

String

relationTypeName,

RoleList

roleList)

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

void

createRelationType

​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

Map

<

ObjectName

,​

List

<

String

>>

findAssociatedMBeans

​(

ObjectName

mbeanName,

String

relationTypeName,

String

roleName)

Retrieves the MBeans associated to given one in a relation.

Map

<

String

,​

List

<

String

>>

findReferencingRelations

​(

ObjectName

mbeanName,

String

relationTypeName,

String

roleName)

Retrieves the relations where a given MBean is referenced.

List

<

String

>

findRelationsOfType

​(

String

relationTypeName)

Returns the relation ids for relations of the given type.

List

<

String

>

getAllRelationIds

()

Returns all the relation ids for all the relations handled by the
Relation Service.

List

<

String

>

getAllRelationTypeNames

()

Retrieves names of all known relation types.

RoleResult

getAllRoles

​(

String

relationId)

Returns all roles present in the relation.

boolean

getPurgeFlag

()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

Map

<

ObjectName

,​

List

<

String

>>

getReferencedMBeans

​(

String

relationId)

Retrieves MBeans referenced in the various roles of the relation.

String

getRelationTypeName

​(

String

relationId)

Returns name of associated relation type for given relation.

List

<

ObjectName

>

getRole

​(

String

relationId,

String

roleName)

Retrieves role value for given role name in given relation.

Integer

getRoleCardinality

​(

String

relationId,

String

roleName)

Retrieves the number of MBeans currently referenced in the
given role.

RoleInfo

getRoleInfo

​(

String

relationTypeName,

String

roleInfoName)

Retrieves role info for given role of a given relation type.

List

<

RoleInfo

>

getRoleInfos

​(

String

relationTypeName)

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

RoleResult

getRoles

​(

String

relationId,

String

[] roleNameArray)

Retrieves values of roles with given names in given relation.

Boolean

hasRelation

​(

String

relationId)

Checks if there is a relation identified in Relation Service with given
relation id.

void

isActive

()

Checks if the Relation Service is active.

String

isRelation

​(

ObjectName

objectName)

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

ObjectName

isRelationMBean

​(

String

relationId)

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

void

purgeRelations

()

Purges the relations.

void

removeRelation

​(

String

relationId)

Removes given relation from the Relation Service.

void

removeRelationType

​(

String

relationTypeName)

Removes given relation type from Relation Service.

void

sendRelationCreationNotification

​(

String

relationId)

Sends a notification (RelationNotification) for a relation creation.

void

sendRelationRemovalNotification

​(

String

relationId,

List

<

ObjectName

> unregMBeanList)

Sends a notification (RelationNotification) for a relation removal.

void

sendRoleUpdateNotification

​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldRoleValue)

Sends a notification (RelationNotification) for a role update in the
given relation.

void

setPurgeFlag

​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

void

setRole

​(

String

relationId,

Role

role)

Sets the given role in given relation.

RoleResult

setRoles

​(

String

relationId,

RoleList

roleList)

Sets the given roles in given relation.

void

updateRoleMap

​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldRoleValue)

Handles update of the Relation Service role map for the update of given
role in given relation.

---

#### Method Summary

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

Adds given object as a relation type.

Checks if given Role can be read in a relation of the given type.

Checks if given Role can be set in a relation of given type.

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

Retrieves the MBeans associated to given one in a relation.

Retrieves the relations where a given MBean is referenced.

Returns the relation ids for relations of the given type.

Returns all the relation ids for all the relations handled by the
Relation Service.

Retrieves names of all known relation types.

Returns all roles present in the relation.

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

Retrieves MBeans referenced in the various roles of the relation.

Returns name of associated relation type for given relation.

Retrieves role value for given role name in given relation.

Retrieves the number of MBeans currently referenced in the
given role.

Retrieves role info for given role of a given relation type.

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

Retrieves values of roles with given names in given relation.

Checks if there is a relation identified in Relation Service with given
relation id.

Checks if the Relation Service is active.

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

Purges the relations.

Removes given relation from the Relation Service.

Removes given relation type from Relation Service.

Sends a notification (RelationNotification) for a relation creation.

Sends a notification (RelationNotification) for a relation removal.

Sends a notification (RelationNotification) for a role update in the
given relation.

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

Sets the given role in given relation.

Sets the given roles in given relation.

Handles update of the Relation Service role map for the update of given
role in given relation.

============ METHOD DETAIL ==========

- Method Detail

- isActive

```java
void isActive()
throws
RelationServiceNotRegisteredException
```

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Throws:** RelationServiceNotRegisteredException

- if it is not
registered

- getPurgeFlag

```java
boolean getPurgeFlag()
```

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Returns:** true if purges are immediate.
**See Also:** setPurgeFlag(boolean)

- setPurgeFlag

```java
void setPurgeFlag​(boolean purgeFlag)
```

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Parameters:** purgeFlag

- flag
**See Also:** getPurgeFlag()

- createRelationType

```java
void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Parameters:** relationTypeName

- name of the relation type
**Parameters:** roleInfoArray

- array of role infos
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRelationTypeException

- If:

- there is already a relation type with that name

- the same name has been used for two different role infos

- no role info provided

- one null role info provided

- addRelationType

```java
void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Parameters:** relationTypeObj

- relation type object (implementing the
RelationType interface)
**Throws:** IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
**Throws:** InvalidRelationTypeException

- if there is already a relation
type with that name

- getAllRelationTypeNames

```java
List
<
String
> getAllRelationTypeNames()
```

Retrieves names of all known relation types.

**Returns:** ArrayList of relation type names (Strings)

- getRoleInfos

```java
List
<
RoleInfo
> getRoleInfos​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

**Parameters:** relationTypeName

- name of relation type
**Returns:** ArrayList of RoleInfo.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if there is no relation type
with that name.

- getRoleInfo

```java
RoleInfo
getRoleInfo​(
String
relationTypeName,

String
roleInfoName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
,

RoleInfoNotFoundException
```

Retrieves role info for given role of a given relation type.

**Parameters:** relationTypeName

- name of relation type
**Parameters:** roleInfoName

- name of role
**Returns:** RoleInfo object.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service
**Throws:** RoleInfoNotFoundException

- if the role is not part of the
relation type.

- removeRelationType

```java
void removeRelationType​(
String
relationTypeName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationTypeNotFoundException
```

Removes given relation type from Relation Service.

The relation objects of that type will be removed from the
Relation Service.

**Parameters:** relationTypeName

- name of the relation type to be removed
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- If there is no relation type
with that name

- createRelation

```java
void createRelation​(
String
relationId,

String
relationTypeName,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RoleNotFoundException
,

InvalidRelationIdException
,

RelationTypeNotFoundException
,

InvalidRoleValueException
```

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Roles are initialized according to the role list provided in
parameter. The ones not initialized in this way are set to an empty
ArrayList of ObjectNames.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

**Parameters:** relationId

- relation identifier, to identify uniquely the relation
inside the Relation Service
**Parameters:** relationTypeName

- name of the relation type (has to be created
in the Relation Service)
**Parameters:** roleList

- role list to initialize roles of the relation (can
be null).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type
**Throws:** InvalidRelationIdException

- if relation id already used
**Throws:** RelationTypeNotFoundException

- if relation type not known in
Relation Service
**Throws:** InvalidRoleValueException

- if:

- the same role name is used for two different roles

- the number of referenced MBeans in given value is less than
expected minimum degree

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

- addRelation

```java
void addRelation​(
ObjectName
relationObjectName)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

NoSuchMethodException
,

InvalidRelationIdException
,

InstanceNotFoundException
,

InvalidRelationServiceException
,

RelationTypeNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
```

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Parameters:** relationObjectName

- ObjectName of the relation MBean to be added.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** NoSuchMethodException

- If the MBean does not implement the
Relation interface
**Throws:** InvalidRelationIdException

- if:

- no relation identifier in MBean

- the relation identifier is already used in the Relation Service
**Throws:** InstanceNotFoundException

- if the MBean for given ObjectName
has not been registered
**Throws:** InvalidRelationServiceException

- if:

- no Relation Service name in MBean

- the Relation Service name in the MBean is not the one of the
current Relation Service
**Throws:** RelationTypeNotFoundException

- if:

- no relation type name in MBean

- the relation type name in MBean does not correspond to a relation
type created in the Relation Service
**Throws:** InvalidRoleValueException

- if:

- the number of referenced MBeans in a role is less than
expected minimum degree

- the number of referenced MBeans in a role exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist
**Throws:** RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type

- isRelationMBean

```java
ObjectName
isRelationMBean​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

**Parameters:** relationId

- relation id identifying the relation
**Returns:** ObjectName of the corresponding relation MBean, or null if
the relation is not an MBean.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- there is no relation associated
to that id

- isRelation

```java
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Parameters:** objectName

- ObjectName of supposed relation
**Returns:** relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)
**Throws:** IllegalArgumentException

- if null parameter

- hasRelation

```java
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException
```

Checks if there is a relation identified in Relation Service with given
relation id.

**Parameters:** relationId

- relation id identifying the relation
**Returns:** boolean: true if there is a relation, false else
**Throws:** IllegalArgumentException

- if null parameter

- getAllRelationIds

```java
List
<
String
> getAllRelationIds()
```

Returns all the relation ids for all the relations handled by the
Relation Service.

**Returns:** ArrayList of String

- checkRoleReading

```java
Integer
checkRoleReading​(
String
roleName,

String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Checks if given Role can be read in a relation of the given type.

**Parameters:** roleName

- name of role to be checked
**Parameters:** relationTypeName

- name of the relation type
**Returns:** an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be read

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer corresponding to RoleStatus.ROLE_NOT_READABLE
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service

- checkRoleWriting

```java
Integer
checkRoleWriting​(
Role
role,

String
relationTypeName,

Boolean
initFlag)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Checks if given Role can be set in a relation of given type.

**Parameters:** role

- role to be checked
**Parameters:** relationTypeName

- name of relation type
**Parameters:** initFlag

- flag to specify that the checking is done for the
initialization of a role, write access shall not be verified.
**Returns:** an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be set

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if unknown relation type

- sendRelationCreationNotification

```java
void sendRelationCreationNotification​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a relation creation.
The notification type is:

- RelationNotification.RELATION_BASIC_CREATION if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

**Parameters:** relationId

- relation identifier of the updated relation
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRoleUpdateNotification

```java
void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a role update in the
given relation. The notification type is:

- RelationNotification.RELATION_BASIC_UPDATE if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldRoleValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRelationRemovalNotification

```java
void sendRelationRemovalNotification​(
String
relationId,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a relation removal.
The notification type is:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** unregMBeanList

- List of ObjectNames of MBeans expected
to be unregistered due to relation removal (can be null)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- updateRoleMap

```java
void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

RelationNotFoundException
```

Handles update of the Relation Service role map for the update of given
role in given relation.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldRoleValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** RelationNotFoundException

- if no relation for given id.

- removeRelation

```java
void removeRelation​(
String
relationId)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Removes given relation from the Relation Service.

A RelationNotification notification is sent, its type being:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

**Parameters:** relationId

- relation id of the relation to be removed
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation corresponding to
given relation id

- purgeRelations

```java
void purgeRelations()
throws
RelationServiceNotRegisteredException
```

Purges the relations.

Depending on the purgeFlag value, this method is either called
automatically when a notification is received for the unregistration of
an MBean referenced in a relation (if the flag is set to true), or not
(if the flag is set to false).

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

- findReferencingRelations

```java
Map
<
String
,​
List
<
String
>> findReferencingRelations​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException
```

Retrieves the relations where a given MBean is referenced.

This corresponds to the CIM "References" and "ReferenceNames"
operations.

**Parameters:** mbeanName

- ObjectName of MBean
**Parameters:** relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all relation types
are considered.
**Parameters:** roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be returned. Else all
roles are considered.
**Returns:** an HashMap, where the keys are the relation ids of the relations
where the MBean is referenced, and the value is, for each key,
an ArrayList of role names (as an MBean can be referenced in several
roles in the same relation).
**Throws:** IllegalArgumentException

- if null parameter

- findAssociatedMBeans

```java
Map
<
ObjectName
,​
List
<
String
>> findAssociatedMBeans​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException
```

Retrieves the MBeans associated to given one in a relation.

This corresponds to CIM Associators and AssociatorNames operations.

**Parameters:** mbeanName

- ObjectName of MBean
**Parameters:** relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all
relation types are considered.
**Parameters:** roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be considered. Else all
roles are considered.
**Returns:** an HashMap, where the keys are the ObjectNames of the MBeans
associated to given MBean, and the value is, for each key, an ArrayList
of the relation ids of the relations where the key MBean is
associated to given one (as they can be associated in several different
relations).
**Throws:** IllegalArgumentException

- if null parameter

- findRelationsOfType

```java
List
<
String
> findRelationsOfType​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Returns the relation ids for relations of the given type.

**Parameters:** relationTypeName

- relation type name
**Returns:** an ArrayList of relation ids.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if there is no relation type
with that name.

- getRole

```java
List
<
ObjectName
> getRole​(
String
relationId,

String
roleName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
```

Retrieves role value for given role name in given relation.

**Parameters:** relationId

- relation id
**Parameters:** roleName

- name of role
**Returns:** the ArrayList of ObjectName objects being the role value
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if:

- there is no role with given name

or

- the role is not readable.
**See Also:** setRole(java.lang.String, javax.management.relation.Role)

- getRoles

```java
RoleResult
getRoles​(
String
relationId,

String
[] roleNameArray)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Retrieves values of roles with given names in given relation.

**Parameters:** relationId

- relation id
**Parameters:** roleNameArray

- array of names of roles to be retrieved
**Returns:** a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
retrieved).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**See Also:** setRoles(java.lang.String, javax.management.relation.RoleList)

- getAllRoles

```java
RoleResult
getAllRoles​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RelationServiceNotRegisteredException
```

Returns all roles present in the relation.

**Parameters:** relationId

- relation id
**Returns:** a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
readable).
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given id
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server

- getRoleCardinality

```java
Integer
getRoleCardinality​(
String
relationId,

String
roleName)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
```

Retrieves the number of MBeans currently referenced in the
given role.

**Parameters:** relationId

- relation id
**Parameters:** roleName

- name of role
**Returns:** the number of currently referenced MBeans in that role
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if there is no role with given name

- setRole

```java
void setRole​(
String
relationId,

Role
role)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
,

RelationTypeNotFoundException
```

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:** relationId

- relation id
**Parameters:** role

- role to be set (name and new value)
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if:

- internal relation

and

- the role does not exist or is not writable
**Throws:** InvalidRoleValueException

- if internal relation and value
provided for role is not valid:

- the number of referenced MBeans in given value is less than
expected minimum degree

or

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist
**Throws:** RelationTypeNotFoundException

- if unknown relation type
**See Also:** getRole(java.lang.String, java.lang.String)

- setRoles

```java
RoleResult
setRoles​(
String
relationId,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Sets the given roles in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:** relationId

- relation id
**Parameters:** roleList

- list of roles to be set
**Returns:** a RoleResult object, including a RoleList (for roles
successfully set) and a RoleUnresolvedList (for roles not
set).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**See Also:** getRoles(java.lang.String, java.lang.String[])

- getReferencedMBeans

```java
Map
<
ObjectName
,​
List
<
String
>> getReferencedMBeans​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Retrieves MBeans referenced in the various roles of the relation.

**Parameters:** relationId

- relation id
**Returns:** a HashMap mapping:

ObjectName -> ArrayList of String (role
names)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

- getRelationTypeName

```java
String
getRelationTypeName​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Returns name of associated relation type for given relation.

**Parameters:** relationId

- relation id
**Returns:** the name of the associated relation type.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

Method Detail

- isActive

```java
void isActive()
throws
RelationServiceNotRegisteredException
```

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Throws:** RelationServiceNotRegisteredException

- if it is not
registered

- getPurgeFlag

```java
boolean getPurgeFlag()
```

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Returns:** true if purges are immediate.
**See Also:** setPurgeFlag(boolean)

- setPurgeFlag

```java
void setPurgeFlag​(boolean purgeFlag)
```

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Parameters:** purgeFlag

- flag
**See Also:** getPurgeFlag()

- createRelationType

```java
void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Parameters:** relationTypeName

- name of the relation type
**Parameters:** roleInfoArray

- array of role infos
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRelationTypeException

- If:

- there is already a relation type with that name

- the same name has been used for two different role infos

- no role info provided

- one null role info provided

- addRelationType

```java
void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Parameters:** relationTypeObj

- relation type object (implementing the
RelationType interface)
**Throws:** IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
**Throws:** InvalidRelationTypeException

- if there is already a relation
type with that name

- getAllRelationTypeNames

```java
List
<
String
> getAllRelationTypeNames()
```

Retrieves names of all known relation types.

**Returns:** ArrayList of relation type names (Strings)

- getRoleInfos

```java
List
<
RoleInfo
> getRoleInfos​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

**Parameters:** relationTypeName

- name of relation type
**Returns:** ArrayList of RoleInfo.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if there is no relation type
with that name.

- getRoleInfo

```java
RoleInfo
getRoleInfo​(
String
relationTypeName,

String
roleInfoName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
,

RoleInfoNotFoundException
```

Retrieves role info for given role of a given relation type.

**Parameters:** relationTypeName

- name of relation type
**Parameters:** roleInfoName

- name of role
**Returns:** RoleInfo object.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service
**Throws:** RoleInfoNotFoundException

- if the role is not part of the
relation type.

- removeRelationType

```java
void removeRelationType​(
String
relationTypeName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationTypeNotFoundException
```

Removes given relation type from Relation Service.

The relation objects of that type will be removed from the
Relation Service.

**Parameters:** relationTypeName

- name of the relation type to be removed
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- If there is no relation type
with that name

- createRelation

```java
void createRelation​(
String
relationId,

String
relationTypeName,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RoleNotFoundException
,

InvalidRelationIdException
,

RelationTypeNotFoundException
,

InvalidRoleValueException
```

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Roles are initialized according to the role list provided in
parameter. The ones not initialized in this way are set to an empty
ArrayList of ObjectNames.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

**Parameters:** relationId

- relation identifier, to identify uniquely the relation
inside the Relation Service
**Parameters:** relationTypeName

- name of the relation type (has to be created
in the Relation Service)
**Parameters:** roleList

- role list to initialize roles of the relation (can
be null).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type
**Throws:** InvalidRelationIdException

- if relation id already used
**Throws:** RelationTypeNotFoundException

- if relation type not known in
Relation Service
**Throws:** InvalidRoleValueException

- if:

- the same role name is used for two different roles

- the number of referenced MBeans in given value is less than
expected minimum degree

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

- addRelation

```java
void addRelation​(
ObjectName
relationObjectName)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

NoSuchMethodException
,

InvalidRelationIdException
,

InstanceNotFoundException
,

InvalidRelationServiceException
,

RelationTypeNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
```

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Parameters:** relationObjectName

- ObjectName of the relation MBean to be added.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** NoSuchMethodException

- If the MBean does not implement the
Relation interface
**Throws:** InvalidRelationIdException

- if:

- no relation identifier in MBean

- the relation identifier is already used in the Relation Service
**Throws:** InstanceNotFoundException

- if the MBean for given ObjectName
has not been registered
**Throws:** InvalidRelationServiceException

- if:

- no Relation Service name in MBean

- the Relation Service name in the MBean is not the one of the
current Relation Service
**Throws:** RelationTypeNotFoundException

- if:

- no relation type name in MBean

- the relation type name in MBean does not correspond to a relation
type created in the Relation Service
**Throws:** InvalidRoleValueException

- if:

- the number of referenced MBeans in a role is less than
expected minimum degree

- the number of referenced MBeans in a role exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist
**Throws:** RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type

- isRelationMBean

```java
ObjectName
isRelationMBean​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

**Parameters:** relationId

- relation id identifying the relation
**Returns:** ObjectName of the corresponding relation MBean, or null if
the relation is not an MBean.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- there is no relation associated
to that id

- isRelation

```java
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Parameters:** objectName

- ObjectName of supposed relation
**Returns:** relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)
**Throws:** IllegalArgumentException

- if null parameter

- hasRelation

```java
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException
```

Checks if there is a relation identified in Relation Service with given
relation id.

**Parameters:** relationId

- relation id identifying the relation
**Returns:** boolean: true if there is a relation, false else
**Throws:** IllegalArgumentException

- if null parameter

- getAllRelationIds

```java
List
<
String
> getAllRelationIds()
```

Returns all the relation ids for all the relations handled by the
Relation Service.

**Returns:** ArrayList of String

- checkRoleReading

```java
Integer
checkRoleReading​(
String
roleName,

String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Checks if given Role can be read in a relation of the given type.

**Parameters:** roleName

- name of role to be checked
**Parameters:** relationTypeName

- name of the relation type
**Returns:** an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be read

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer corresponding to RoleStatus.ROLE_NOT_READABLE
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service

- checkRoleWriting

```java
Integer
checkRoleWriting​(
Role
role,

String
relationTypeName,

Boolean
initFlag)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Checks if given Role can be set in a relation of given type.

**Parameters:** role

- role to be checked
**Parameters:** relationTypeName

- name of relation type
**Parameters:** initFlag

- flag to specify that the checking is done for the
initialization of a role, write access shall not be verified.
**Returns:** an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be set

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if unknown relation type

- sendRelationCreationNotification

```java
void sendRelationCreationNotification​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a relation creation.
The notification type is:

- RelationNotification.RELATION_BASIC_CREATION if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

**Parameters:** relationId

- relation identifier of the updated relation
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRoleUpdateNotification

```java
void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a role update in the
given relation. The notification type is:

- RelationNotification.RELATION_BASIC_UPDATE if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldRoleValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRelationRemovalNotification

```java
void sendRelationRemovalNotification​(
String
relationId,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a relation removal.
The notification type is:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** unregMBeanList

- List of ObjectNames of MBeans expected
to be unregistered due to relation removal (can be null)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- updateRoleMap

```java
void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

RelationNotFoundException
```

Handles update of the Relation Service role map for the update of given
role in given relation.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldRoleValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** RelationNotFoundException

- if no relation for given id.

- removeRelation

```java
void removeRelation​(
String
relationId)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Removes given relation from the Relation Service.

A RelationNotification notification is sent, its type being:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

**Parameters:** relationId

- relation id of the relation to be removed
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation corresponding to
given relation id

- purgeRelations

```java
void purgeRelations()
throws
RelationServiceNotRegisteredException
```

Purges the relations.

Depending on the purgeFlag value, this method is either called
automatically when a notification is received for the unregistration of
an MBean referenced in a relation (if the flag is set to true), or not
(if the flag is set to false).

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

- findReferencingRelations

```java
Map
<
String
,​
List
<
String
>> findReferencingRelations​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException
```

Retrieves the relations where a given MBean is referenced.

This corresponds to the CIM "References" and "ReferenceNames"
operations.

**Parameters:** mbeanName

- ObjectName of MBean
**Parameters:** relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all relation types
are considered.
**Parameters:** roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be returned. Else all
roles are considered.
**Returns:** an HashMap, where the keys are the relation ids of the relations
where the MBean is referenced, and the value is, for each key,
an ArrayList of role names (as an MBean can be referenced in several
roles in the same relation).
**Throws:** IllegalArgumentException

- if null parameter

- findAssociatedMBeans

```java
Map
<
ObjectName
,​
List
<
String
>> findAssociatedMBeans​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException
```

Retrieves the MBeans associated to given one in a relation.

This corresponds to CIM Associators and AssociatorNames operations.

**Parameters:** mbeanName

- ObjectName of MBean
**Parameters:** relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all
relation types are considered.
**Parameters:** roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be considered. Else all
roles are considered.
**Returns:** an HashMap, where the keys are the ObjectNames of the MBeans
associated to given MBean, and the value is, for each key, an ArrayList
of the relation ids of the relations where the key MBean is
associated to given one (as they can be associated in several different
relations).
**Throws:** IllegalArgumentException

- if null parameter

- findRelationsOfType

```java
List
<
String
> findRelationsOfType​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Returns the relation ids for relations of the given type.

**Parameters:** relationTypeName

- relation type name
**Returns:** an ArrayList of relation ids.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if there is no relation type
with that name.

- getRole

```java
List
<
ObjectName
> getRole​(
String
relationId,

String
roleName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
```

Retrieves role value for given role name in given relation.

**Parameters:** relationId

- relation id
**Parameters:** roleName

- name of role
**Returns:** the ArrayList of ObjectName objects being the role value
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if:

- there is no role with given name

or

- the role is not readable.
**See Also:** setRole(java.lang.String, javax.management.relation.Role)

- getRoles

```java
RoleResult
getRoles​(
String
relationId,

String
[] roleNameArray)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Retrieves values of roles with given names in given relation.

**Parameters:** relationId

- relation id
**Parameters:** roleNameArray

- array of names of roles to be retrieved
**Returns:** a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
retrieved).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**See Also:** setRoles(java.lang.String, javax.management.relation.RoleList)

- getAllRoles

```java
RoleResult
getAllRoles​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RelationServiceNotRegisteredException
```

Returns all roles present in the relation.

**Parameters:** relationId

- relation id
**Returns:** a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
readable).
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given id
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server

- getRoleCardinality

```java
Integer
getRoleCardinality​(
String
relationId,

String
roleName)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
```

Retrieves the number of MBeans currently referenced in the
given role.

**Parameters:** relationId

- relation id
**Parameters:** roleName

- name of role
**Returns:** the number of currently referenced MBeans in that role
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if there is no role with given name

- setRole

```java
void setRole​(
String
relationId,

Role
role)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
,

RelationTypeNotFoundException
```

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:** relationId

- relation id
**Parameters:** role

- role to be set (name and new value)
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if:

- internal relation

and

- the role does not exist or is not writable
**Throws:** InvalidRoleValueException

- if internal relation and value
provided for role is not valid:

- the number of referenced MBeans in given value is less than
expected minimum degree

or

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist
**Throws:** RelationTypeNotFoundException

- if unknown relation type
**See Also:** getRole(java.lang.String, java.lang.String)

- setRoles

```java
RoleResult
setRoles​(
String
relationId,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Sets the given roles in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:** relationId

- relation id
**Parameters:** roleList

- list of roles to be set
**Returns:** a RoleResult object, including a RoleList (for roles
successfully set) and a RoleUnresolvedList (for roles not
set).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**See Also:** getRoles(java.lang.String, java.lang.String[])

- getReferencedMBeans

```java
Map
<
ObjectName
,​
List
<
String
>> getReferencedMBeans​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Retrieves MBeans referenced in the various roles of the relation.

**Parameters:** relationId

- relation id
**Returns:** a HashMap mapping:

ObjectName -> ArrayList of String (role
names)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

- getRelationTypeName

```java
String
getRelationTypeName​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Returns name of associated relation type for given relation.

**Parameters:** relationId

- relation id
**Returns:** the name of the associated relation type.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

---

#### Method Detail

isActive

```java
void isActive()
throws
RelationServiceNotRegisteredException
```

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Throws:** RelationServiceNotRegisteredException

- if it is not
registered

---

#### isActive

void isActive()
throws

RelationServiceNotRegisteredException

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

getPurgeFlag

```java
boolean getPurgeFlag()
```

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Returns:** true if purges are immediate.
**See Also:** setPurgeFlag(boolean)

---

#### getPurgeFlag

boolean getPurgeFlag()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

true is immediate purge.

setPurgeFlag

```java
void setPurgeFlag​(boolean purgeFlag)
```

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

**Parameters:** purgeFlag

- flag
**See Also:** getPurgeFlag()

---

#### setPurgeFlag

void setPurgeFlag​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed, or if that will be performed only when the
purgeRelations method is explicitly called.

true is immediate purge.

true is immediate purge.

createRelationType

```java
void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Parameters:** relationTypeName

- name of the relation type
**Parameters:** roleInfoArray

- array of role infos
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRelationTypeException

- If:

- there is already a relation type with that name

- the same name has been used for two different role infos

- no role info provided

- one null role info provided

---

#### createRelationType

void createRelationType​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)
throws

IllegalArgumentException

,

InvalidRelationTypeException

Creates a relation type (RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

- there is already a relation type with that name

- the same name has been used for two different role infos

- no role info provided

- one null role info provided

- the same name has been used for two different role infos

- no role info provided

- one null role info provided

- no role info provided

- one null role info provided

- one null role info provided

addRelationType

```java
void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Parameters:** relationTypeObj

- relation type object (implementing the
RelationType interface)
**Throws:** IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
**Throws:** InvalidRelationTypeException

- if there is already a relation
type with that name

---

#### addRelationType

void addRelationType​(

RelationType

relationTypeObj)
throws

IllegalArgumentException

,

InvalidRelationTypeException

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

getAllRelationTypeNames

```java
List
<
String
> getAllRelationTypeNames()
```

Retrieves names of all known relation types.

**Returns:** ArrayList of relation type names (Strings)

---

#### getAllRelationTypeNames

List

<

String

> getAllRelationTypeNames()

Retrieves names of all known relation types.

getRoleInfos

```java
List
<
RoleInfo
> getRoleInfos​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

**Parameters:** relationTypeName

- name of relation type
**Returns:** ArrayList of RoleInfo.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if there is no relation type
with that name.

---

#### getRoleInfos

List

<

RoleInfo

> getRoleInfos​(

String

relationTypeName)
throws

IllegalArgumentException

,

RelationTypeNotFoundException

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

getRoleInfo

```java
RoleInfo
getRoleInfo​(
String
relationTypeName,

String
roleInfoName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
,

RoleInfoNotFoundException
```

Retrieves role info for given role of a given relation type.

**Parameters:** relationTypeName

- name of relation type
**Parameters:** roleInfoName

- name of role
**Returns:** RoleInfo object.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service
**Throws:** RoleInfoNotFoundException

- if the role is not part of the
relation type.

---

#### getRoleInfo

RoleInfo

getRoleInfo​(

String

relationTypeName,

String

roleInfoName)
throws

IllegalArgumentException

,

RelationTypeNotFoundException

,

RoleInfoNotFoundException

Retrieves role info for given role of a given relation type.

removeRelationType

```java
void removeRelationType​(
String
relationTypeName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationTypeNotFoundException
```

Removes given relation type from Relation Service.

The relation objects of that type will be removed from the
Relation Service.

**Parameters:** relationTypeName

- name of the relation type to be removed
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- If there is no relation type
with that name

---

#### removeRelationType

void removeRelationType​(

String

relationTypeName)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RelationTypeNotFoundException

Removes given relation type from Relation Service.

The relation objects of that type will be removed from the
Relation Service.

The relation objects of that type will be removed from the
Relation Service.

createRelation

```java
void createRelation​(
String
relationId,

String
relationTypeName,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RoleNotFoundException
,

InvalidRelationIdException
,

RelationTypeNotFoundException
,

InvalidRoleValueException
```

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Roles are initialized according to the role list provided in
parameter. The ones not initialized in this way are set to an empty
ArrayList of ObjectNames.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

**Parameters:** relationId

- relation identifier, to identify uniquely the relation
inside the Relation Service
**Parameters:** relationTypeName

- name of the relation type (has to be created
in the Relation Service)
**Parameters:** roleList

- role list to initialize roles of the relation (can
be null).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type
**Throws:** InvalidRelationIdException

- if relation id already used
**Throws:** RelationTypeNotFoundException

- if relation type not known in
Relation Service
**Throws:** InvalidRoleValueException

- if:

- the same role name is used for two different roles

- the number of referenced MBeans in given value is less than
expected minimum degree

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

---

#### createRelation

void createRelation​(

String

relationId,

String

relationTypeName,

RoleList

roleList)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RoleNotFoundException

,

InvalidRelationIdException

,

RelationTypeNotFoundException

,

InvalidRoleValueException

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Roles are initialized according to the role list provided in
parameter. The ones not initialized in this way are set to an empty
ArrayList of ObjectNames.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

Roles are initialized according to the role list provided in
parameter. The ones not initialized in this way are set to an empty
ArrayList of ObjectNames.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

A RelationNotification, with type RELATION_BASIC_CREATION, is sent.

- the same role name is used for two different roles

- the number of referenced MBeans in given value is less than
expected minimum degree

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

- the number of referenced MBeans in given value is less than
expected minimum degree

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

- the number of referenced MBeans in provided value exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for that role does not exist

- an MBean provided for that role does not exist

addRelation

```java
void addRelation​(
ObjectName
relationObjectName)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

NoSuchMethodException
,

InvalidRelationIdException
,

InstanceNotFoundException
,

InvalidRelationServiceException
,

RelationTypeNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
```

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Parameters:** relationObjectName

- ObjectName of the relation MBean to be added.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** NoSuchMethodException

- If the MBean does not implement the
Relation interface
**Throws:** InvalidRelationIdException

- if:

- no relation identifier in MBean

- the relation identifier is already used in the Relation Service
**Throws:** InstanceNotFoundException

- if the MBean for given ObjectName
has not been registered
**Throws:** InvalidRelationServiceException

- if:

- no Relation Service name in MBean

- the Relation Service name in the MBean is not the one of the
current Relation Service
**Throws:** RelationTypeNotFoundException

- if:

- no relation type name in MBean

- the relation type name in MBean does not correspond to a relation
type created in the Relation Service
**Throws:** InvalidRoleValueException

- if:

- the number of referenced MBeans in a role is less than
expected minimum degree

- the number of referenced MBeans in a role exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist
**Throws:** RoleNotFoundException

- if a value is provided for a role
that does not exist in the relation type

---

#### addRelation

void addRelation​(

ObjectName

relationObjectName)
throws

IllegalArgumentException

,

RelationServiceNotRegisteredException

,

NoSuchMethodException

,

InvalidRelationIdException

,

InstanceNotFoundException

,

InvalidRelationServiceException

,

RelationTypeNotFoundException

,

RoleNotFoundException

,

InvalidRoleValueException

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- have a relation id that is unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- have roles conforming to the role info provided in the relation
type.

- no relation identifier in MBean

- the relation identifier is already used in the Relation Service

- the relation identifier is already used in the Relation Service

- no Relation Service name in MBean

- the Relation Service name in the MBean is not the one of the
current Relation Service

- the Relation Service name in the MBean is not the one of the
current Relation Service

- no relation type name in MBean

- the relation type name in MBean does not correspond to a relation
type created in the Relation Service

- the relation type name in MBean does not correspond to a relation
type created in the Relation Service

- the number of referenced MBeans in a role is less than
expected minimum degree

- the number of referenced MBeans in a role exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist

- the number of referenced MBeans in a role exceeds expected
maximum degree

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

- an MBean provided for a role does not exist

- an MBean provided for a role does not exist

isRelationMBean

```java
ObjectName
isRelationMBean​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

**Parameters:** relationId

- relation id identifying the relation
**Returns:** ObjectName of the corresponding relation MBean, or null if
the relation is not an MBean.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- there is no relation associated
to that id

---

#### isRelationMBean

ObjectName

isRelationMBean​(

String

relationId)
throws

IllegalArgumentException

,

RelationNotFoundException

If the relation is represented by an MBean (created by the user and
added as a relation in the Relation Service), returns the ObjectName of
the MBean.

isRelation

```java
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Parameters:** objectName

- ObjectName of supposed relation
**Returns:** relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)
**Throws:** IllegalArgumentException

- if null parameter

---

#### isRelation

String

isRelation​(

ObjectName

objectName)
throws

IllegalArgumentException

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

hasRelation

```java
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException
```

Checks if there is a relation identified in Relation Service with given
relation id.

**Parameters:** relationId

- relation id identifying the relation
**Returns:** boolean: true if there is a relation, false else
**Throws:** IllegalArgumentException

- if null parameter

---

#### hasRelation

Boolean

hasRelation​(

String

relationId)
throws

IllegalArgumentException

Checks if there is a relation identified in Relation Service with given
relation id.

getAllRelationIds

```java
List
<
String
> getAllRelationIds()
```

Returns all the relation ids for all the relations handled by the
Relation Service.

**Returns:** ArrayList of String

---

#### getAllRelationIds

List

<

String

> getAllRelationIds()

Returns all the relation ids for all the relations handled by the
Relation Service.

checkRoleReading

```java
Integer
checkRoleReading​(
String
roleName,

String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Checks if given Role can be read in a relation of the given type.

**Parameters:** roleName

- name of role to be checked
**Parameters:** relationTypeName

- name of the relation type
**Returns:** an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be read

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer corresponding to RoleStatus.ROLE_NOT_READABLE
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if the relation type is not
known in the Relation Service

---

#### checkRoleReading

Integer

checkRoleReading​(

String

roleName,

String

relationTypeName)
throws

IllegalArgumentException

,

RelationTypeNotFoundException

Checks if given Role can be read in a relation of the given type.

- 0 if role can be read

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer corresponding to RoleStatus.ROLE_NOT_READABLE

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer corresponding to RoleStatus.ROLE_NOT_READABLE

- integer corresponding to RoleStatus.ROLE_NOT_READABLE

checkRoleWriting

```java
Integer
checkRoleWriting​(
Role
role,

String
relationTypeName,

Boolean
initFlag)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Checks if given Role can be set in a relation of given type.

**Parameters:** role

- role to be checked
**Parameters:** relationTypeName

- name of relation type
**Parameters:** initFlag

- flag to specify that the checking is done for the
initialization of a role, write access shall not be verified.
**Returns:** an Integer wrapping an integer corresponding to possible
problems represented as constants in RoleUnresolved:

- 0 if role can be set

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if unknown relation type

---

#### checkRoleWriting

Integer

checkRoleWriting​(

Role

role,

String

relationTypeName,

Boolean

initFlag)
throws

IllegalArgumentException

,

RelationTypeNotFoundException

Checks if given Role can be set in a relation of given type.

- 0 if role can be set

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

- integer corresponding to RoleStatus.NO_ROLE_WITH_NAME

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

- integer for RoleStatus.ROLE_NOT_WRITABLE

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

- integer for RoleStatus.LESS_THAN_MIN_ROLE_DEGREE

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

- integer for RoleStatus.MORE_THAN_MAX_ROLE_DEGREE

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

- integer for RoleStatus.REF_MBEAN_OF_INCORRECT_CLASS

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

- integer for RoleStatus.REF_MBEAN_NOT_REGISTERED

sendRelationCreationNotification

```java
void sendRelationCreationNotification​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a relation creation.
The notification type is:

- RelationNotification.RELATION_BASIC_CREATION if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

**Parameters:** relationId

- relation identifier of the updated relation
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

---

#### sendRelationCreationNotification

void sendRelationCreationNotification​(

String

relationId)
throws

IllegalArgumentException

,

RelationNotFoundException

Sends a notification (RelationNotification) for a relation creation.
The notification type is:

- RelationNotification.RELATION_BASIC_CREATION if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

- RelationNotification.RELATION_BASIC_CREATION if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

- RelationNotification.RELATION_MBEAN_CREATION if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

The source object is the Relation Service itself.

It is called in Relation Service createRelation() and
addRelation() methods.

It is called in Relation Service createRelation() and
addRelation() methods.

sendRoleUpdateNotification

```java
void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a role update in the
given relation. The notification type is:

- RelationNotification.RELATION_BASIC_UPDATE if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldRoleValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

---

#### sendRoleUpdateNotification

void sendRoleUpdateNotification​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldRoleValue)
throws

IllegalArgumentException

,

RelationNotFoundException

Sends a notification (RelationNotification) for a role update in the
given relation. The notification type is:

- RelationNotification.RELATION_BASIC_UPDATE if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

- RelationNotification.RELATION_BASIC_UPDATE if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

- RelationNotification.RELATION_MBEAN_UPDATE if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

The source object is the Relation Service itself.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

sendRelationRemovalNotification

```java
void sendRelationRemovalNotification​(
String
relationId,

List
<
ObjectName
> unregMBeanList)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Sends a notification (RelationNotification) for a relation removal.
The notification type is:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** unregMBeanList

- List of ObjectNames of MBeans expected
to be unregistered due to relation removal (can be null)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

---

#### sendRelationRemovalNotification

void sendRelationRemovalNotification​(

String

relationId,

List

<

ObjectName

> unregMBeanList)
throws

IllegalArgumentException

,

RelationNotFoundException

Sends a notification (RelationNotification) for a relation removal.
The notification type is:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

- RelationNotification.RELATION_BASIC_REMOVAL if the relation is an
object internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is a
MBean added as a relation.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

The source object is the Relation Service itself.

It is called in Relation Service removeRelation() method.

It is called in Relation Service removeRelation() method.

updateRoleMap

```java
void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldRoleValue)
throws
IllegalArgumentException
,

RelationServiceNotRegisteredException
,

RelationNotFoundException
```

Handles update of the Relation Service role map for the update of given
role in given relation.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldRoleValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** RelationNotFoundException

- if no relation for given id.

---

#### updateRoleMap

void updateRoleMap​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldRoleValue)
throws

IllegalArgumentException

,

RelationServiceNotRegisteredException

,

RelationNotFoundException

Handles update of the Relation Service role map for the update of given
role in given relation.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

It is called in relation MBean setRole() (for given role) and
setRoles() (for each role) methods (implementation provided in
RelationSupport class).

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

It is also called in Relation Service setRole() (for given role) and
setRoles() (for each role) methods.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

To allow the Relation Service to maintain the consistency (in case
of MBean unregistration) and to be able to perform queries, this method
must be called when a role is updated.

removeRelation

```java
void removeRelation​(
String
relationId)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Removes given relation from the Relation Service.

A RelationNotification notification is sent, its type being:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

**Parameters:** relationId

- relation id of the relation to be removed
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation corresponding to
given relation id

---

#### removeRelation

void removeRelation​(

String

relationId)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RelationNotFoundException

Removes given relation from the Relation Service.

A RelationNotification notification is sent, its type being:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

A RelationNotification notification is sent, its type being:

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

- RelationNotification.RELATION_BASIC_REMOVAL if the relation was
only internal to the Relation Service

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

- RelationNotification.RELATION_MBEAN_REMOVAL if the relation is
registered as an MBean.

For MBeans referenced in such relation, nothing will be done,

For MBeans referenced in such relation, nothing will be done,

purgeRelations

```java
void purgeRelations()
throws
RelationServiceNotRegisteredException
```

Purges the relations.

Depending on the purgeFlag value, this method is either called
automatically when a notification is received for the unregistration of
an MBean referenced in a relation (if the flag is set to true), or not
(if the flag is set to false).

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

---

#### purgeRelations

void purgeRelations()
throws

RelationServiceNotRegisteredException

Purges the relations.

Depending on the purgeFlag value, this method is either called
automatically when a notification is received for the unregistration of
an MBean referenced in a relation (if the flag is set to true), or not
(if the flag is set to false).

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

Depending on the purgeFlag value, this method is either called
automatically when a notification is received for the unregistration of
an MBean referenced in a relation (if the flag is set to true), or not
(if the flag is set to false).

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

In that case it is up to the user to call it to maintain the
consistency of the relations. To be kept in mind that if an MBean is
unregistered and the purge not done immediately, if the ObjectName is
reused and assigned to another MBean referenced in a relation, calling
manually this purgeRelations() method will cause trouble, as will
consider the ObjectName as corresponding to the unregistered MBean, not
seeing the new one.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

The behavior depends on the cardinality of the role where the
unregistered MBean is referenced:

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

- if removing one MBean reference in the role makes its number of
references less than the minimum degree, the relation has to be removed.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

- if the remaining number of references after removing the MBean
reference is still in the cardinality range, keep the relation and
update it calling its handleMBeanUnregistration() callback.

findReferencingRelations

```java
Map
<
String
,​
List
<
String
>> findReferencingRelations​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException
```

Retrieves the relations where a given MBean is referenced.

This corresponds to the CIM "References" and "ReferenceNames"
operations.

**Parameters:** mbeanName

- ObjectName of MBean
**Parameters:** relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all relation types
are considered.
**Parameters:** roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be returned. Else all
roles are considered.
**Returns:** an HashMap, where the keys are the relation ids of the relations
where the MBean is referenced, and the value is, for each key,
an ArrayList of role names (as an MBean can be referenced in several
roles in the same relation).
**Throws:** IllegalArgumentException

- if null parameter

---

#### findReferencingRelations

Map

<

String

,​

List

<

String

>> findReferencingRelations​(

ObjectName

mbeanName,

String

relationTypeName,

String

roleName)
throws

IllegalArgumentException

Retrieves the relations where a given MBean is referenced.

This corresponds to the CIM "References" and "ReferenceNames"
operations.

This corresponds to the CIM "References" and "ReferenceNames"
operations.

findAssociatedMBeans

```java
Map
<
ObjectName
,​
List
<
String
>> findAssociatedMBeans​(
ObjectName
mbeanName,

String
relationTypeName,

String
roleName)
throws
IllegalArgumentException
```

Retrieves the MBeans associated to given one in a relation.

This corresponds to CIM Associators and AssociatorNames operations.

**Parameters:** mbeanName

- ObjectName of MBean
**Parameters:** relationTypeName

- can be null; if specified, only the relations
of that type will be considered in the search. Else all
relation types are considered.
**Parameters:** roleName

- can be null; if specified, only the relations
where the MBean is referenced in that role will be considered. Else all
roles are considered.
**Returns:** an HashMap, where the keys are the ObjectNames of the MBeans
associated to given MBean, and the value is, for each key, an ArrayList
of the relation ids of the relations where the key MBean is
associated to given one (as they can be associated in several different
relations).
**Throws:** IllegalArgumentException

- if null parameter

---

#### findAssociatedMBeans

Map

<

ObjectName

,​

List

<

String

>> findAssociatedMBeans​(

ObjectName

mbeanName,

String

relationTypeName,

String

roleName)
throws

IllegalArgumentException

Retrieves the MBeans associated to given one in a relation.

This corresponds to CIM Associators and AssociatorNames operations.

This corresponds to CIM Associators and AssociatorNames operations.

findRelationsOfType

```java
List
<
String
> findRelationsOfType​(
String
relationTypeName)
throws
IllegalArgumentException
,

RelationTypeNotFoundException
```

Returns the relation ids for relations of the given type.

**Parameters:** relationTypeName

- relation type name
**Returns:** an ArrayList of relation ids.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationTypeNotFoundException

- if there is no relation type
with that name.

---

#### findRelationsOfType

List

<

String

> findRelationsOfType​(

String

relationTypeName)
throws

IllegalArgumentException

,

RelationTypeNotFoundException

Returns the relation ids for relations of the given type.

getRole

```java
List
<
ObjectName
> getRole​(
String
relationId,

String
roleName)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
```

Retrieves role value for given role name in given relation.

**Parameters:** relationId

- relation id
**Parameters:** roleName

- name of role
**Returns:** the ArrayList of ObjectName objects being the role value
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if:

- there is no role with given name

or

- the role is not readable.
**See Also:** setRole(java.lang.String, javax.management.relation.Role)

---

#### getRole

List

<

ObjectName

> getRole​(

String

relationId,

String

roleName)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RelationNotFoundException

,

RoleNotFoundException

Retrieves role value for given role name in given relation.

- there is no role with given name

or

- the role is not readable.

or

- the role is not readable.

- the role is not readable.

getRoles

```java
RoleResult
getRoles​(
String
relationId,

String
[] roleNameArray)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Retrieves values of roles with given names in given relation.

**Parameters:** relationId

- relation id
**Parameters:** roleNameArray

- array of names of roles to be retrieved
**Returns:** a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
retrieved).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**See Also:** setRoles(java.lang.String, javax.management.relation.RoleList)

---

#### getRoles

RoleResult

getRoles​(

String

relationId,

String

[] roleNameArray)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RelationNotFoundException

Retrieves values of roles with given names in given relation.

getAllRoles

```java
RoleResult
getAllRoles​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RelationServiceNotRegisteredException
```

Returns all roles present in the relation.

**Parameters:** relationId

- relation id
**Returns:** a RoleResult object, including a RoleList (for roles
successfully retrieved) and a RoleUnresolvedList (for roles not
readable).
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given id
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server

---

#### getAllRoles

RoleResult

getAllRoles​(

String

relationId)
throws

IllegalArgumentException

,

RelationNotFoundException

,

RelationServiceNotRegisteredException

Returns all roles present in the relation.

getRoleCardinality

```java
Integer
getRoleCardinality​(
String
relationId,

String
roleName)
throws
IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
```

Retrieves the number of MBeans currently referenced in the
given role.

**Parameters:** relationId

- relation id
**Parameters:** roleName

- name of role
**Returns:** the number of currently referenced MBeans in that role
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if there is no role with given name

---

#### getRoleCardinality

Integer

getRoleCardinality​(

String

relationId,

String

roleName)
throws

IllegalArgumentException

,

RelationNotFoundException

,

RoleNotFoundException

Retrieves the number of MBeans currently referenced in the
given role.

setRole

```java
void setRole​(
String
relationId,

Role
role)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
,

RoleNotFoundException
,

InvalidRoleValueException
,

RelationTypeNotFoundException
```

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:** relationId

- relation id
**Parameters:** role

- role to be set (name and new value)
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**Throws:** RoleNotFoundException

- if:

- internal relation

and

- the role does not exist or is not writable
**Throws:** InvalidRoleValueException

- if internal relation and value
provided for role is not valid:

- the number of referenced MBeans in given value is less than
expected minimum degree

or

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist
**Throws:** RelationTypeNotFoundException

- if unknown relation type
**See Also:** getRole(java.lang.String, java.lang.String)

---

#### setRole

void setRole​(

String

relationId,

Role

role)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RelationNotFoundException

,

RoleNotFoundException

,

InvalidRoleValueException

,

RelationTypeNotFoundException

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

- internal relation

and

- the role does not exist or is not writable

and

- the role does not exist or is not writable

- the role does not exist or is not writable

- the number of referenced MBeans in given value is less than
expected minimum degree

or

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist

or

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist

- the number of referenced MBeans in provided value exceeds expected
maximum degree

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist

or

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist

- one referenced MBean in the value is not an Object of the MBean
class expected for that role

or

- an MBean provided for that role does not exist

or

- an MBean provided for that role does not exist

- an MBean provided for that role does not exist

setRoles

```java
RoleResult
setRoles​(
String
relationId,

RoleList
roleList)
throws
RelationServiceNotRegisteredException
,

IllegalArgumentException
,

RelationNotFoundException
```

Sets the given roles in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

**Parameters:** relationId

- relation id
**Parameters:** roleList

- list of roles to be set
**Returns:** a RoleResult object, including a RoleList (for roles
successfully set) and a RoleUnresolvedList (for roles not
set).
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation with given id
**See Also:** getRoles(java.lang.String, java.lang.String[])

---

#### setRoles

RoleResult

setRoles​(

String

relationId,

RoleList

roleList)
throws

RelationServiceNotRegisteredException

,

IllegalArgumentException

,

RelationNotFoundException

Sets the given roles in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

The Relation Service keeps track of the changes to keep the
consistency of relations by handling referenced MBean deregistrations.

getReferencedMBeans

```java
Map
<
ObjectName
,​
List
<
String
>> getReferencedMBeans​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Retrieves MBeans referenced in the various roles of the relation.

**Parameters:** relationId

- relation id
**Returns:** a HashMap mapping:

ObjectName -> ArrayList of String (role
names)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

---

#### getReferencedMBeans

Map

<

ObjectName

,​

List

<

String

>> getReferencedMBeans​(

String

relationId)
throws

IllegalArgumentException

,

RelationNotFoundException

Retrieves MBeans referenced in the various roles of the relation.

ObjectName -> ArrayList of String (role
names)

getRelationTypeName

```java
String
getRelationTypeName​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException
```

Returns name of associated relation type for given relation.

**Parameters:** relationId

- relation id
**Returns:** the name of the associated relation type.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

---

#### getRelationTypeName

String

getRelationTypeName​(

String

relationId)
throws

IllegalArgumentException

,

RelationNotFoundException

Returns name of associated relation type for given relation.

---

