# Interface Group

**Source:** `java.base\java\security\acl\Group.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Group

extends
Principal
```

This interface is used to represent a group of principals. (A principal
represents an entity such as an individual user or a company).

Note that Group extends Principal. Thus, either a Principal or a Group can
be passed as an argument to methods containing a Principal parameter. For
example, you can add either a Principal or a Group to a Group object by
calling the object's

addMember

method, passing it the
Principal or Group.

**All Superinterfaces:** Principal

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean addMember​(
Principal
user)

Adds the specified member to the group.

**Parameters:**
- user

- the principal to add to this group.

**Returns:**
- true if the member was successfully added,
false if the principal was already a member.

---

#### boolean removeMember​(
Principal
user)

Removes the specified member from the group.

**Parameters:**
- user

- the principal to remove from this group.

**Returns:**
- true if the principal was removed, or
false if the principal was not a member.

---

#### boolean isMember​(
Principal
member)

Returns true if the passed principal is a member of the group.
This method does a recursive search, so if a principal belongs to a
group which is a member of this group, true is returned.

**Parameters:**
- member

- the principal whose membership is to be checked.

**Returns:**
- true if the principal is a member of this group,
false otherwise.

---

#### Enumeration
<? extends
Principal
> members()

Returns an enumeration of the members in the group.
The returned objects can be instances of either Principal
or Group (which is a subclass of Principal).

**Returns:**
- an enumeration of the group members.

---

### Additional Sections

#### Interface Group

**All Superinterfaces:** Principal

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Group

extends
Principal
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.Policy

and related classes since 1.2.

This interface is used to represent a group of principals. (A principal
represents an entity such as an individual user or a company).

Note that Group extends Principal. Thus, either a Principal or a Group can
be passed as an argument to methods containing a Principal parameter. For
example, you can add either a Principal or a Group to a Group object by
calling the object's

addMember

method, passing it the
Principal or Group.

**Since:** 1.1

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Group

extends

Principal

This interface is used to represent a group of principals. (A principal
represents an entity such as an individual user or a company).

Note that Group extends Principal. Thus, either a Principal or a Group can
be passed as an argument to methods containing a Principal parameter. For
example, you can add either a Principal or a Group to a Group object by
calling the object's

addMember

method, passing it the
Principal or Group.

Note that Group extends Principal. Thus, either a Principal or a Group can
be passed as an argument to methods containing a Principal parameter. For
example, you can add either a Principal or a Group to a Group object by
calling the object's

addMember

method, passing it the
Principal or Group.

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

addMember

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified member to the group.

boolean

isMember

​(

Principal

member)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the passed principal is a member of the group.

Enumeration

<? extends

Principal

>

members

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the members in the group.

boolean

removeMember

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified member from the group.

- Methods declared in interface java.security.

Principal

equals

,

getName

,

hashCode

,

implies

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

addMember

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified member to the group.

boolean

isMember

​(

Principal

member)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the passed principal is a member of the group.

Enumeration

<? extends

Principal

>

members

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the members in the group.

boolean

removeMember

​(

Principal

user)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified member from the group.

- Methods declared in interface java.security.

Principal

equals

,

getName

,

hashCode

,

implies

,

toString

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified member to the group.

Returns true if the passed principal is a member of the group.

Returns an enumeration of the members in the group.

Removes the specified member from the group.

Methods declared in interface java.security.

Principal

equals

,

getName

,

hashCode

,

implies

,

toString

---

#### Methods declared in interface java.security. Principal

============ METHOD DETAIL ==========

- Method Detail

- addMember

```java
boolean addMember​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified member to the group.

**Parameters:** user

- the principal to add to this group.
**Returns:** true if the member was successfully added,
false if the principal was already a member.

- removeMember

```java
boolean removeMember​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified member from the group.

**Parameters:** user

- the principal to remove from this group.
**Returns:** true if the principal was removed, or
false if the principal was not a member.

- isMember

```java
boolean isMember​(
Principal
member)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the passed principal is a member of the group.
This method does a recursive search, so if a principal belongs to a
group which is a member of this group, true is returned.

**Parameters:** member

- the principal whose membership is to be checked.
**Returns:** true if the principal is a member of this group,
false otherwise.

- members

```java
Enumeration
<? extends
Principal
> members()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the members in the group.
The returned objects can be instances of either Principal
or Group (which is a subclass of Principal).

**Returns:** an enumeration of the group members.

Method Detail

- addMember

```java
boolean addMember​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified member to the group.

**Parameters:** user

- the principal to add to this group.
**Returns:** true if the member was successfully added,
false if the principal was already a member.

- removeMember

```java
boolean removeMember​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified member from the group.

**Parameters:** user

- the principal to remove from this group.
**Returns:** true if the principal was removed, or
false if the principal was not a member.

- isMember

```java
boolean isMember​(
Principal
member)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the passed principal is a member of the group.
This method does a recursive search, so if a principal belongs to a
group which is a member of this group, true is returned.

**Parameters:** member

- the principal whose membership is to be checked.
**Returns:** true if the principal is a member of this group,
false otherwise.

- members

```java
Enumeration
<? extends
Principal
> members()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the members in the group.
The returned objects can be instances of either Principal
or Group (which is a subclass of Principal).

**Returns:** an enumeration of the group members.

---

#### Method Detail

addMember

```java
boolean addMember​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds the specified member to the group.

**Parameters:** user

- the principal to add to this group.
**Returns:** true if the member was successfully added,
false if the principal was already a member.

---

#### addMember

boolean addMember​(

Principal

user)

Adds the specified member to the group.

removeMember

```java
boolean removeMember​(
Principal
user)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes the specified member from the group.

**Parameters:** user

- the principal to remove from this group.
**Returns:** true if the principal was removed, or
false if the principal was not a member.

---

#### removeMember

boolean removeMember​(

Principal

user)

Removes the specified member from the group.

isMember

```java
boolean isMember​(
Principal
member)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns true if the passed principal is a member of the group.
This method does a recursive search, so if a principal belongs to a
group which is a member of this group, true is returned.

**Parameters:** member

- the principal whose membership is to be checked.
**Returns:** true if the principal is a member of this group,
false otherwise.

---

#### isMember

boolean isMember​(

Principal

member)

Returns true if the passed principal is a member of the group.
This method does a recursive search, so if a principal belongs to a
group which is a member of this group, true is returned.

members

```java
Enumeration
<? extends
Principal
> members()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of the members in the group.
The returned objects can be instances of either Principal
or Group (which is a subclass of Principal).

**Returns:** an enumeration of the group members.

---

#### members

Enumeration

<? extends

Principal

> members()

Returns an enumeration of the members in the group.
The returned objects can be instances of either Principal
or Group (which is a subclass of Principal).

---

