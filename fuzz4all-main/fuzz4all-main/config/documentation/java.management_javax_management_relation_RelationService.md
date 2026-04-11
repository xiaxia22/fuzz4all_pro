# Class RelationService

**Source:** `java.management\javax\management\relation\RelationService.html`

### Class Description

```java
public class
RelationService

extends
NotificationBroadcasterSupport

implements
RelationServiceMBean
,
MBeanRegistration
,
NotificationListener
```

The Relation Service is in charge of creating and deleting relation types
and relations, of handling the consistency and of providing query
mechanisms.

It implements the NotificationBroadcaster by extending
NotificationBroadcasterSupport to send notifications when a relation is
removed from it.

It implements the NotificationListener interface to be able to receive
notifications concerning unregistration of MBeans referenced in relation
roles and of relation MBeans.

It implements the MBeanRegistration interface to be able to retrieve
its ObjectName and MBean Server.

**All Implemented Interfaces:** EventListener

,

MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

NotificationListener

,

RelationServiceMBean

---

### Field Details

*No entries found.*

### Constructor Details

#### public RelationService​(boolean immediatePurgeFlag)

Constructor.

**Parameters:**
- immediatePurgeFlag

- flag to indicate when a notification is
received for the unregistration of an MBean referenced in a relation, if
an immediate "purge" of the relations (look for the relations no
longer valid) has to be performed , or if that will be performed only
when the purgeRelations method will be explicitly called.

true is immediate purge.

---

### Method Details

#### public void isActive()
throws
RelationServiceNotRegisteredException

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Specified by:**
- isActive

in interface

RelationServiceMBean

**Throws:**
- RelationServiceNotRegisteredException

- if it is not
registered

---

#### public boolean getPurgeFlag()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:**
- getPurgeFlag

in interface

RelationServiceMBean

**Returns:**
- true if purges are automatic.

**See Also:**
- setPurgeFlag(boolean)

---

#### public void setPurgeFlag​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:**
- setPurgeFlag

in interface

RelationServiceMBean

**Parameters:**
- purgeFlag

- flag

**See Also:**
- getPurgeFlag()

---

#### public void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException

Creates a relation type (a RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Specified by:**
- createRelationType

in interface

RelationServiceMBean

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

#### public void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Specified by:**
- addRelationType

in interface

RelationServiceMBean

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

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- there is already a relation type with that name

---

#### public
List
<
String
> getAllRelationTypeNames()

Retrieves names of all known relation types.

**Specified by:**
- getAllRelationTypeNames

in interface

RelationServiceMBean

**Returns:**
- ArrayList of relation type names (Strings)

---

#### public
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

**Specified by:**
- getRoleInfos

in interface

RelationServiceMBean

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

#### public
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

Retrieves role info for given role name of a given relation type.

**Specified by:**
- getRoleInfo

in interface

RelationServiceMBean

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

#### public void removeRelationType​(
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

**Specified by:**
- removeRelationType

in interface

RelationServiceMBean

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

#### public void createRelation​(
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

**Specified by:**
- createRelation

in interface

RelationServiceMBean

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

- if null parameter, except the role
list which can be null if no role initialization
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

#### public void addRelation​(
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

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Specified by:**
- addRelation

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- isRelationMBean

in interface

RelationServiceMBean

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

#### public
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Specified by:**
- isRelation

in interface

RelationServiceMBean

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

#### public
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException

Checks if there is a relation identified in Relation Service with given
relation id.

**Specified by:**
- hasRelation

in interface

RelationServiceMBean

**Parameters:**
- relationId

- relation id identifying the relation

**Returns:**
- boolean: true if there is a relation, false else

**Throws:**
- IllegalArgumentException

- if null parameter

---

#### public
List
<
String
> getAllRelationIds()

Returns all the relation ids for all the relations handled by the
Relation Service.

**Specified by:**
- getAllRelationIds

in interface

RelationServiceMBean

**Returns:**
- ArrayList of String

---

#### public
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

**Specified by:**
- checkRoleReading

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- checkRoleWriting

in interface

RelationServiceMBean

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

#### public void sendRelationCreationNotification​(
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

**Specified by:**
- sendRelationCreationNotification

in interface

RelationServiceMBean

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

#### public void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:**
- sendRoleUpdateNotification

in interface

RelationServiceMBean

**Parameters:**
- relationId

- relation identifier of the updated relation
- newRole

- new role (name and new value)
- oldValue

- old role value (List of ObjectName objects)

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if there is no relation for given
relation id

---

#### public void sendRelationRemovalNotification​(
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

**Specified by:**
- sendRelationRemovalNotification

in interface

RelationServiceMBean

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

#### public void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:**
- updateRoleMap

in interface

RelationServiceMBean

**Parameters:**
- relationId

- relation identifier of the updated relation
- newRole

- new role (name and new value)
- oldValue

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

#### public void removeRelation​(
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

**Specified by:**
- removeRelation

in interface

RelationServiceMBean

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

#### public void purgeRelations()
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

**Specified by:**
- purgeRelations

in interface

RelationServiceMBean

**Throws:**
- RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

---

#### public
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

**Specified by:**
- findReferencingRelations

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- findAssociatedMBeans

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- findRelationsOfType

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- getRole

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- getRoles

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- getAllRoles

in interface

RelationServiceMBean

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

#### public
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

Retrieves the number of MBeans currently referenced in the given role.

**Specified by:**
- getRoleCardinality

in interface

RelationServiceMBean

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

#### public void setRole​(
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

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Specified by:**
- setRole

in interface

RelationServiceMBean

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

- if the role does not exist or is not
writable
- InvalidRoleValueException

- if value provided for role is not
valid:

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

**See Also:**
- getRole(java.lang.String, java.lang.String)

---

#### public
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

**Specified by:**
- setRoles

in interface

RelationServiceMBean

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

#### public
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

**Specified by:**
- getReferencedMBeans

in interface

RelationServiceMBean

**Parameters:**
- relationId

- relation id

**Returns:**
- a HashMap mapping:

ObjectName -> ArrayList of String (role names)

**Throws:**
- IllegalArgumentException

- if null parameter
- RelationNotFoundException

- if no relation for given
relation id

---

#### public
String
getRelationTypeName​(
String
relationId)
throws
IllegalArgumentException
,

RelationNotFoundException

Returns name of associated relation type for given relation.

**Specified by:**
- getRelationTypeName

in interface

RelationServiceMBean

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

#### public void handleNotification​(
Notification
notif,

Object
handback)

Invoked when a JMX notification occurs.
Currently handles notifications for unregistration of MBeans, either
referenced in a relation role or being a relation itself.

**Specified by:**
- handleNotification

in interface

NotificationListener

**Parameters:**
- notif

- The notification.
- handback

- An opaque object which helps the listener to
associate information regarding the MBean emitter (can be null).

---

#### public
MBeanNotificationInfo
[] getNotificationInfo()

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

**Specified by:**
- getNotificationInfo

in interface

NotificationBroadcaster

**Returns:**
- the array of possible notifications.

---

### Additional Sections

#### Class RelationService

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.relation.RelationService

javax.management.NotificationBroadcasterSupport

- javax.management.relation.RelationService

javax.management.relation.RelationService

**All Implemented Interfaces:** EventListener

,

MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

NotificationListener

,

RelationServiceMBean

```java
public class
RelationService

extends
NotificationBroadcasterSupport

implements
RelationServiceMBean
,
MBeanRegistration
,
NotificationListener
```

The Relation Service is in charge of creating and deleting relation types
and relations, of handling the consistency and of providing query
mechanisms.

It implements the NotificationBroadcaster by extending
NotificationBroadcasterSupport to send notifications when a relation is
removed from it.

It implements the NotificationListener interface to be able to receive
notifications concerning unregistration of MBeans referenced in relation
roles and of relation MBeans.

It implements the MBeanRegistration interface to be able to retrieve
its ObjectName and MBean Server.

**Since:** 1.5

public class

RelationService

extends

NotificationBroadcasterSupport

implements

RelationServiceMBean

,

MBeanRegistration

,

NotificationListener

The Relation Service is in charge of creating and deleting relation types
and relations, of handling the consistency and of providing query
mechanisms.

It implements the NotificationBroadcaster by extending
NotificationBroadcasterSupport to send notifications when a relation is
removed from it.

It implements the NotificationListener interface to be able to receive
notifications concerning unregistration of MBeans referenced in relation
roles and of relation MBeans.

It implements the MBeanRegistration interface to be able to retrieve
its ObjectName and MBean Server.

It implements the NotificationBroadcaster by extending
NotificationBroadcasterSupport to send notifications when a relation is
removed from it.

It implements the NotificationListener interface to be able to receive
notifications concerning unregistration of MBeans referenced in relation
roles and of relation MBeans.

It implements the MBeanRegistration interface to be able to retrieve
its ObjectName and MBean Server.

It implements the NotificationListener interface to be able to receive
notifications concerning unregistration of MBeans referenced in relation
roles and of relation MBeans.

It implements the MBeanRegistration interface to be able to retrieve
its ObjectName and MBean Server.

It implements the MBeanRegistration interface to be able to retrieve
its ObjectName and MBean Server.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RelationService

​(boolean immediatePurgeFlag)

Constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

Creates a relation type (a RelationTypeSupport object) with given
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

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

boolean

getPurgeFlag

()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

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

Retrieves the number of MBeans currently referenced in the given role.

RoleInfo

getRoleInfo

​(

String

relationTypeName,

String

roleInfoName)

Retrieves role info for given role name of a given relation type.

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

void

handleNotification

​(

Notification

notif,

Object

handback)

Invoked when a JMX notification occurs.

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

> oldValue)

Sends a notification (RelationNotification) for a role update in the
given relation.

void

setPurgeFlag

​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

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

> oldValue)

Handles update of the Relation Service role map for the update of given
role in given relation.

- Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

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

- Methods declared in interface javax.management.

MBeanRegistration

postDeregister

,

postRegister

,

preDeregister

,

preRegister

- Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

Constructor Summary

Constructors

Constructor

Description

RelationService

​(boolean immediatePurgeFlag)

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

Creates a relation type (a RelationTypeSupport object) with given
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

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

boolean

getPurgeFlag

()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

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

Retrieves the number of MBeans currently referenced in the given role.

RoleInfo

getRoleInfo

​(

String

relationTypeName,

String

roleInfoName)

Retrieves role info for given role name of a given relation type.

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

void

handleNotification

​(

Notification

notif,

Object

handback)

Invoked when a JMX notification occurs.

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

> oldValue)

Sends a notification (RelationNotification) for a role update in the
given relation.

void

setPurgeFlag

​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

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

> oldValue)

Handles update of the Relation Service role map for the update of given
role in given relation.

- Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

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

- Methods declared in interface javax.management.

MBeanRegistration

postDeregister

,

postRegister

,

preDeregister

,

preRegister

- Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Adds an MBean created by the user (and registered by him in the MBean
Server) as a relation in the Relation Service.

Adds given object as a relation type.

Checks if given Role can be read in a relation of the given type.

Checks if given Role can be set in a relation of given type.

Creates a simple relation (represented by a RelationSupport object) of
given relation type, and adds it in the Relation Service.

Creates a relation type (a RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

Retrieves the MBeans associated to given one in a relation.

Retrieves the relations where a given MBean is referenced.

Returns the relation ids for relations of the given type.

Returns all the relation ids for all the relations handled by the
Relation Service.

Retrieves names of all known relation types.

Returns all roles present in the relation.

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

Retrieves MBeans referenced in the various roles of the relation.

Returns name of associated relation type for given relation.

Retrieves role value for given role name in given relation.

Retrieves the number of MBeans currently referenced in the given role.

Retrieves role info for given role name of a given relation type.

Retrieves list of role infos (RoleInfo objects) of a given relation
type.

Retrieves values of roles with given names in given relation.

Invoked when a JMX notification occurs.

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
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

Sets the given role in given relation.

Sets the given roles in given relation.

Handles update of the Relation Service role map for the update of given
role in given relation.

Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

---

#### Methods declared in class javax.management. NotificationBroadcasterSupport

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

Methods declared in interface javax.management.

MBeanRegistration

postDeregister

,

postRegister

,

preDeregister

,

preRegister

---

#### Methods declared in interface javax.management. MBeanRegistration

Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationBroadcaster

Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationEmitter

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RelationService

```java
public RelationService​(boolean immediatePurgeFlag)
```

Constructor.

**Parameters:** immediatePurgeFlag

- flag to indicate when a notification is
received for the unregistration of an MBean referenced in a relation, if
an immediate "purge" of the relations (look for the relations no
longer valid) has to be performed , or if that will be performed only
when the purgeRelations method will be explicitly called.

true is immediate purge.

============ METHOD DETAIL ==========

- Method Detail

- isActive

```java
public void isActive()
throws
RelationServiceNotRegisteredException
```

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Specified by:** isActive

in interface

RelationServiceMBean
**Throws:** RelationServiceNotRegisteredException

- if it is not
registered

- getPurgeFlag

```java
public boolean getPurgeFlag()
```

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:** getPurgeFlag

in interface

RelationServiceMBean
**Returns:** true if purges are automatic.
**See Also:** setPurgeFlag(boolean)

- setPurgeFlag

```java
public void setPurgeFlag​(boolean purgeFlag)
```

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:** setPurgeFlag

in interface

RelationServiceMBean
**Parameters:** purgeFlag

- flag
**See Also:** getPurgeFlag()

- createRelationType

```java
public void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Creates a relation type (a RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Specified by:** createRelationType

in interface

RelationServiceMBean
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
public void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Specified by:** addRelationType

in interface

RelationServiceMBean
**Parameters:** relationTypeObj

- relation type object (implementing the
RelationType interface)
**Throws:** IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
**Throws:** InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- there is already a relation type with that name

- getAllRelationTypeNames

```java
public
List
<
String
> getAllRelationTypeNames()
```

Retrieves names of all known relation types.

**Specified by:** getAllRelationTypeNames

in interface

RelationServiceMBean
**Returns:** ArrayList of relation type names (Strings)

- getRoleInfos

```java
public
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

**Specified by:** getRoleInfos

in interface

RelationServiceMBean
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
public
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

Retrieves role info for given role name of a given relation type.

**Specified by:** getRoleInfo

in interface

RelationServiceMBean
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
public void removeRelationType​(
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

**Specified by:** removeRelationType

in interface

RelationServiceMBean
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
public void createRelation​(
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

**Specified by:** createRelation

in interface

RelationServiceMBean
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

- if null parameter, except the role
list which can be null if no role initialization
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
public void addRelation​(
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

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Specified by:** addRelation

in interface

RelationServiceMBean
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
public
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

**Specified by:** isRelationMBean

in interface

RelationServiceMBean
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
public
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Specified by:** isRelation

in interface

RelationServiceMBean
**Parameters:** objectName

- ObjectName of supposed relation
**Returns:** relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)
**Throws:** IllegalArgumentException

- if null parameter

- hasRelation

```java
public
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException
```

Checks if there is a relation identified in Relation Service with given
relation id.

**Specified by:** hasRelation

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id identifying the relation
**Returns:** boolean: true if there is a relation, false else
**Throws:** IllegalArgumentException

- if null parameter

- getAllRelationIds

```java
public
List
<
String
> getAllRelationIds()
```

Returns all the relation ids for all the relations handled by the
Relation Service.

**Specified by:** getAllRelationIds

in interface

RelationServiceMBean
**Returns:** ArrayList of String

- checkRoleReading

```java
public
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

**Specified by:** checkRoleReading

in interface

RelationServiceMBean
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
public
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

**Specified by:** checkRoleWriting

in interface

RelationServiceMBean
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
public void sendRelationCreationNotification​(
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

**Specified by:** sendRelationCreationNotification

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRoleUpdateNotification

```java
public void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:** sendRoleUpdateNotification

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRelationRemovalNotification

```java
public void sendRelationRemovalNotification​(
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

**Specified by:** sendRelationRemovalNotification

in interface

RelationServiceMBean
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
public void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:** updateRoleMap

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldValue

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
public void removeRelation​(
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

**Specified by:** removeRelation

in interface

RelationServiceMBean
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
public void purgeRelations()
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

**Specified by:** purgeRelations

in interface

RelationServiceMBean
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

- findReferencingRelations

```java
public
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

**Specified by:** findReferencingRelations

in interface

RelationServiceMBean
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
public
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

**Specified by:** findAssociatedMBeans

in interface

RelationServiceMBean
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
public
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

**Specified by:** findRelationsOfType

in interface

RelationServiceMBean
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
public
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

**Specified by:** getRole

in interface

RelationServiceMBean
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
public
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

**Specified by:** getRoles

in interface

RelationServiceMBean
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
public
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

**Specified by:** getAllRoles

in interface

RelationServiceMBean
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
public
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

Retrieves the number of MBeans currently referenced in the given role.

**Specified by:** getRoleCardinality

in interface

RelationServiceMBean
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
public void setRole​(
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
```

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Specified by:** setRole

in interface

RelationServiceMBean
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

- if the role does not exist or is not
writable
**Throws:** InvalidRoleValueException

- if value provided for role is not
valid:

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
**See Also:** getRole(java.lang.String, java.lang.String)

- setRoles

```java
public
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

**Specified by:** setRoles

in interface

RelationServiceMBean
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
public
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

**Specified by:** getReferencedMBeans

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id
**Returns:** a HashMap mapping:

ObjectName -> ArrayList of String (role names)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

- getRelationTypeName

```java
public
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

**Specified by:** getRelationTypeName

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id
**Returns:** the name of the associated relation type.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

- handleNotification

```java
public void handleNotification​(
Notification
notif,

Object
handback)
```

Invoked when a JMX notification occurs.
Currently handles notifications for unregistration of MBeans, either
referenced in a relation role or being a relation itself.

**Specified by:** handleNotification

in interface

NotificationListener
**Parameters:** notif

- The notification.
**Parameters:** handback

- An opaque object which helps the listener to
associate information regarding the MBean emitter (can be null).

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

Constructor Detail

- RelationService

```java
public RelationService​(boolean immediatePurgeFlag)
```

Constructor.

**Parameters:** immediatePurgeFlag

- flag to indicate when a notification is
received for the unregistration of an MBean referenced in a relation, if
an immediate "purge" of the relations (look for the relations no
longer valid) has to be performed , or if that will be performed only
when the purgeRelations method will be explicitly called.

true is immediate purge.

---

#### Constructor Detail

RelationService

```java
public RelationService​(boolean immediatePurgeFlag)
```

Constructor.

**Parameters:** immediatePurgeFlag

- flag to indicate when a notification is
received for the unregistration of an MBean referenced in a relation, if
an immediate "purge" of the relations (look for the relations no
longer valid) has to be performed , or if that will be performed only
when the purgeRelations method will be explicitly called.

true is immediate purge.

---

#### RelationService

public RelationService​(boolean immediatePurgeFlag)

Constructor.

true is immediate purge.

Method Detail

- isActive

```java
public void isActive()
throws
RelationServiceNotRegisteredException
```

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Specified by:** isActive

in interface

RelationServiceMBean
**Throws:** RelationServiceNotRegisteredException

- if it is not
registered

- getPurgeFlag

```java
public boolean getPurgeFlag()
```

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:** getPurgeFlag

in interface

RelationServiceMBean
**Returns:** true if purges are automatic.
**See Also:** setPurgeFlag(boolean)

- setPurgeFlag

```java
public void setPurgeFlag​(boolean purgeFlag)
```

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:** setPurgeFlag

in interface

RelationServiceMBean
**Parameters:** purgeFlag

- flag
**See Also:** getPurgeFlag()

- createRelationType

```java
public void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Creates a relation type (a RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Specified by:** createRelationType

in interface

RelationServiceMBean
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
public void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Specified by:** addRelationType

in interface

RelationServiceMBean
**Parameters:** relationTypeObj

- relation type object (implementing the
RelationType interface)
**Throws:** IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
**Throws:** InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- there is already a relation type with that name

- getAllRelationTypeNames

```java
public
List
<
String
> getAllRelationTypeNames()
```

Retrieves names of all known relation types.

**Specified by:** getAllRelationTypeNames

in interface

RelationServiceMBean
**Returns:** ArrayList of relation type names (Strings)

- getRoleInfos

```java
public
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

**Specified by:** getRoleInfos

in interface

RelationServiceMBean
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
public
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

Retrieves role info for given role name of a given relation type.

**Specified by:** getRoleInfo

in interface

RelationServiceMBean
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
public void removeRelationType​(
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

**Specified by:** removeRelationType

in interface

RelationServiceMBean
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
public void createRelation​(
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

**Specified by:** createRelation

in interface

RelationServiceMBean
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

- if null parameter, except the role
list which can be null if no role initialization
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
public void addRelation​(
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

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Specified by:** addRelation

in interface

RelationServiceMBean
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
public
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

**Specified by:** isRelationMBean

in interface

RelationServiceMBean
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
public
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Specified by:** isRelation

in interface

RelationServiceMBean
**Parameters:** objectName

- ObjectName of supposed relation
**Returns:** relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)
**Throws:** IllegalArgumentException

- if null parameter

- hasRelation

```java
public
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException
```

Checks if there is a relation identified in Relation Service with given
relation id.

**Specified by:** hasRelation

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id identifying the relation
**Returns:** boolean: true if there is a relation, false else
**Throws:** IllegalArgumentException

- if null parameter

- getAllRelationIds

```java
public
List
<
String
> getAllRelationIds()
```

Returns all the relation ids for all the relations handled by the
Relation Service.

**Specified by:** getAllRelationIds

in interface

RelationServiceMBean
**Returns:** ArrayList of String

- checkRoleReading

```java
public
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

**Specified by:** checkRoleReading

in interface

RelationServiceMBean
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
public
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

**Specified by:** checkRoleWriting

in interface

RelationServiceMBean
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
public void sendRelationCreationNotification​(
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

**Specified by:** sendRelationCreationNotification

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRoleUpdateNotification

```java
public void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:** sendRoleUpdateNotification

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

- sendRelationRemovalNotification

```java
public void sendRelationRemovalNotification​(
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

**Specified by:** sendRelationRemovalNotification

in interface

RelationServiceMBean
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
public void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:** updateRoleMap

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldValue

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
public void removeRelation​(
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

**Specified by:** removeRelation

in interface

RelationServiceMBean
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
public void purgeRelations()
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

**Specified by:** purgeRelations

in interface

RelationServiceMBean
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

- findReferencingRelations

```java
public
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

**Specified by:** findReferencingRelations

in interface

RelationServiceMBean
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
public
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

**Specified by:** findAssociatedMBeans

in interface

RelationServiceMBean
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
public
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

**Specified by:** findRelationsOfType

in interface

RelationServiceMBean
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
public
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

**Specified by:** getRole

in interface

RelationServiceMBean
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
public
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

**Specified by:** getRoles

in interface

RelationServiceMBean
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
public
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

**Specified by:** getAllRoles

in interface

RelationServiceMBean
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
public
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

Retrieves the number of MBeans currently referenced in the given role.

**Specified by:** getRoleCardinality

in interface

RelationServiceMBean
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
public void setRole​(
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
```

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Specified by:** setRole

in interface

RelationServiceMBean
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

- if the role does not exist or is not
writable
**Throws:** InvalidRoleValueException

- if value provided for role is not
valid:

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
**See Also:** getRole(java.lang.String, java.lang.String)

- setRoles

```java
public
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

**Specified by:** setRoles

in interface

RelationServiceMBean
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
public
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

**Specified by:** getReferencedMBeans

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id
**Returns:** a HashMap mapping:

ObjectName -> ArrayList of String (role names)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

- getRelationTypeName

```java
public
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

**Specified by:** getRelationTypeName

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id
**Returns:** the name of the associated relation type.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

- handleNotification

```java
public void handleNotification​(
Notification
notif,

Object
handback)
```

Invoked when a JMX notification occurs.
Currently handles notifications for unregistration of MBeans, either
referenced in a relation role or being a relation itself.

**Specified by:** handleNotification

in interface

NotificationListener
**Parameters:** notif

- The notification.
**Parameters:** handback

- An opaque object which helps the listener to
associate information regarding the MBean emitter (can be null).

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

---

#### Method Detail

isActive

```java
public void isActive()
throws
RelationServiceNotRegisteredException
```

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

**Specified by:** isActive

in interface

RelationServiceMBean
**Throws:** RelationServiceNotRegisteredException

- if it is not
registered

---

#### isActive

public void isActive()
throws

RelationServiceNotRegisteredException

Checks if the Relation Service is active.
Current condition is that the Relation Service must be registered in the
MBean Server

getPurgeFlag

```java
public boolean getPurgeFlag()
```

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:** getPurgeFlag

in interface

RelationServiceMBean
**Returns:** true if purges are automatic.
**See Also:** setPurgeFlag(boolean)

---

#### getPurgeFlag

public boolean getPurgeFlag()

Returns the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

true is immediate purge.

setPurgeFlag

```java
public void setPurgeFlag​(boolean purgeFlag)
```

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

**Specified by:** setPurgeFlag

in interface

RelationServiceMBean
**Parameters:** purgeFlag

- flag
**See Also:** getPurgeFlag()

---

#### setPurgeFlag

public void setPurgeFlag​(boolean purgeFlag)

Sets the flag to indicate if when a notification is received for the
unregistration of an MBean referenced in a relation, if an immediate
"purge" of the relations (look for the relations no longer valid)
has to be performed , or if that will be performed only when the
purgeRelations method will be explicitly called.

true is immediate purge.

true is immediate purge.

createRelationType

```java
public void createRelationType​(
String
relationTypeName,

RoleInfo
[] roleInfoArray)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Creates a relation type (a RelationTypeSupport object) with given
role infos (provided by the RoleInfo objects), and adds it in the
Relation Service.

**Specified by:** createRelationType

in interface

RelationServiceMBean
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

public void createRelationType​(

String

relationTypeName,

RoleInfo

[] roleInfoArray)
throws

IllegalArgumentException

,

InvalidRelationTypeException

Creates a relation type (a RelationTypeSupport object) with given
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
public void addRelationType​(
RelationType
relationTypeObj)
throws
IllegalArgumentException
,

InvalidRelationTypeException
```

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

**Specified by:** addRelationType

in interface

RelationServiceMBean
**Parameters:** relationTypeObj

- relation type object (implementing the
RelationType interface)
**Throws:** IllegalArgumentException

- if null parameter or if

relationTypeObj.getRelationTypeName()

returns null.
**Throws:** InvalidRelationTypeException

- if:

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- there is already a relation type with that name

---

#### addRelationType

public void addRelationType​(

RelationType

relationTypeObj)
throws

IllegalArgumentException

,

InvalidRelationTypeException

Adds given object as a relation type. The object is expected to
implement the RelationType interface.

- the same name has been used for two different roles

- no role info provided

- one null role info provided

- there is already a relation type with that name

- no role info provided

- one null role info provided

- there is already a relation type with that name

- one null role info provided

- there is already a relation type with that name

- there is already a relation type with that name

getAllRelationTypeNames

```java
public
List
<
String
> getAllRelationTypeNames()
```

Retrieves names of all known relation types.

**Specified by:** getAllRelationTypeNames

in interface

RelationServiceMBean
**Returns:** ArrayList of relation type names (Strings)

---

#### getAllRelationTypeNames

public

List

<

String

> getAllRelationTypeNames()

Retrieves names of all known relation types.

getRoleInfos

```java
public
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

**Specified by:** getRoleInfos

in interface

RelationServiceMBean
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

public

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
public
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

Retrieves role info for given role name of a given relation type.

**Specified by:** getRoleInfo

in interface

RelationServiceMBean
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

public

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

Retrieves role info for given role name of a given relation type.

removeRelationType

```java
public void removeRelationType​(
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

**Specified by:** removeRelationType

in interface

RelationServiceMBean
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

public void removeRelationType​(

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
public void createRelation​(
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

**Specified by:** createRelation

in interface

RelationServiceMBean
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

- if null parameter, except the role
list which can be null if no role initialization
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

public void createRelation​(

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
public void addRelation​(
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

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

**Specified by:** addRelation

in interface

RelationServiceMBean
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

public void addRelation​(

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

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

To be added as a relation, the MBean must conform to the
following:

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- implement the Relation interface

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- have for RelationService ObjectName the ObjectName of current
Relation Service

- have a relation id unique and unused in current Relation Service

- have for relation type a relation type created in the Relation
Service

- have roles conforming to the role info provided in the relation
type.

- have a relation id unique and unused in current Relation Service

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
public
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

**Specified by:** isRelationMBean

in interface

RelationServiceMBean
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

public

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
public
String
isRelation​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Returns the relation id associated to the given ObjectName if the
MBean has been added as a relation in the Relation Service.

**Specified by:** isRelation

in interface

RelationServiceMBean
**Parameters:** objectName

- ObjectName of supposed relation
**Returns:** relation id (String) or null (if the ObjectName is not a
relation handled by the Relation Service)
**Throws:** IllegalArgumentException

- if null parameter

---

#### isRelation

public

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
public
Boolean
hasRelation​(
String
relationId)
throws
IllegalArgumentException
```

Checks if there is a relation identified in Relation Service with given
relation id.

**Specified by:** hasRelation

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id identifying the relation
**Returns:** boolean: true if there is a relation, false else
**Throws:** IllegalArgumentException

- if null parameter

---

#### hasRelation

public

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
public
List
<
String
> getAllRelationIds()
```

Returns all the relation ids for all the relations handled by the
Relation Service.

**Specified by:** getAllRelationIds

in interface

RelationServiceMBean
**Returns:** ArrayList of String

---

#### getAllRelationIds

public

List

<

String

> getAllRelationIds()

Returns all the relation ids for all the relations handled by the
Relation Service.

checkRoleReading

```java
public
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

**Specified by:** checkRoleReading

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** checkRoleWriting

in interface

RelationServiceMBean
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

public

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
public void sendRelationCreationNotification​(
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

**Specified by:** sendRelationCreationNotification

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

---

#### sendRelationCreationNotification

public void sendRelationCreationNotification​(

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
public void sendRoleUpdateNotification​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:** sendRoleUpdateNotification

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldValue

- old role value (List of ObjectName objects)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if there is no relation for given
relation id

---

#### sendRoleUpdateNotification

public void sendRoleUpdateNotification​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldValue)
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
public void sendRelationRemovalNotification​(
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

**Specified by:** sendRelationRemovalNotification

in interface

RelationServiceMBean
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

public void sendRelationRemovalNotification​(

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
public void updateRoleMap​(
String
relationId,

Role
newRole,

List
<
ObjectName
> oldValue)
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

**Specified by:** updateRoleMap

in interface

RelationServiceMBean
**Parameters:** relationId

- relation identifier of the updated relation
**Parameters:** newRole

- new role (name and new value)
**Parameters:** oldValue

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

public void updateRoleMap​(

String

relationId,

Role

newRole,

List

<

ObjectName

> oldValue)
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
public void removeRelation​(
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

**Specified by:** removeRelation

in interface

RelationServiceMBean
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

public void removeRelation​(

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
public void purgeRelations()
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

**Specified by:** purgeRelations

in interface

RelationServiceMBean
**Throws:** RelationServiceNotRegisteredException

- if the Relation
Service is not registered in the MBean Server.

---

#### purgeRelations

public void purgeRelations()
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
public
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

**Specified by:** findReferencingRelations

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** findAssociatedMBeans

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** findRelationsOfType

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** getRole

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** getRoles

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** getAllRoles

in interface

RelationServiceMBean
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

public

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
public
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

Retrieves the number of MBeans currently referenced in the given role.

**Specified by:** getRoleCardinality

in interface

RelationServiceMBean
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

public

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

Retrieves the number of MBeans currently referenced in the given role.

setRole

```java
public void setRole​(
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
```

Sets the given role in given relation.

Will check the role according to its corresponding role definition
provided in relation's relation type

The Relation Service will keep track of the change to keep the
consistency of relations by handling referenced MBean deregistrations.

**Specified by:** setRole

in interface

RelationServiceMBean
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

- if the role does not exist or is not
writable
**Throws:** InvalidRoleValueException

- if value provided for role is not
valid:

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
**See Also:** getRole(java.lang.String, java.lang.String)

---

#### setRole

public void setRole​(

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
public
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

**Specified by:** setRoles

in interface

RelationServiceMBean
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

public

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
public
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

**Specified by:** getReferencedMBeans

in interface

RelationServiceMBean
**Parameters:** relationId

- relation id
**Returns:** a HashMap mapping:

ObjectName -> ArrayList of String (role names)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** RelationNotFoundException

- if no relation for given
relation id

---

#### getReferencedMBeans

public

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

ObjectName -> ArrayList of String (role names)

getRelationTypeName

```java
public
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

**Specified by:** getRelationTypeName

in interface

RelationServiceMBean
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

public

String

getRelationTypeName​(

String

relationId)
throws

IllegalArgumentException

,

RelationNotFoundException

Returns name of associated relation type for given relation.

handleNotification

```java
public void handleNotification​(
Notification
notif,

Object
handback)
```

Invoked when a JMX notification occurs.
Currently handles notifications for unregistration of MBeans, either
referenced in a relation role or being a relation itself.

**Specified by:** handleNotification

in interface

NotificationListener
**Parameters:** notif

- The notification.
**Parameters:** handback

- An opaque object which helps the listener to
associate information regarding the MBean emitter (can be null).

---

#### handleNotification

public void handleNotification​(

Notification

notif,

Object

handback)

Invoked when a JMX notification occurs.
Currently handles notifications for unregistration of MBeans, either
referenced in a relation role or being a relation itself.

getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

---

#### getNotificationInfo

public

MBeanNotificationInfo

[] getNotificationInfo()

Returns a NotificationInfo object containing the name of the Java class
of the notification and the notification types sent.

---

