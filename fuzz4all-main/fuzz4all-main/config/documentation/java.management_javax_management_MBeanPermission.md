# Class MBeanPermission

**Source:** `java.management\javax\management\MBeanPermission.html`

### Class Description

```java
public class
MBeanPermission

extends
Permission
```

Permission controlling access to MBeanServer operations. If a
security manager has been set using

System.setSecurityManager(java.lang.SecurityManager)

, most operations on the MBean Server
require that the caller's permissions imply an MBeanPermission
appropriate for the operation. This is described in detail in the
documentation for the

MBeanServer

interface.

As with other

Permission

objects, an MBeanPermission can
represent either a permission that you

have

or a
permission that you

need

. When a sensitive operation is
being checked for permission, an MBeanPermission is constructed
representing the permission you need. The operation is only
allowed if the permissions you have

imply

the
permission you need.

An MBeanPermission contains four items of information:

- The

action

. For a permission you need,
this is one of the actions in the list

below

. For a permission you have, this is
a comma-separated list of those actions, or

*

,
representing all actions.

The action is returned by

getActions()

.

The

class name

.

For a permission you need, this is the class name of an MBean
you are accessing, as returned by

MBeanServer.getMBeanInfo(name)

.

getClassName()

. Certain operations do not reference a class name,
in which case the class name is null.

For a permission you have, this is either empty or a

class
name pattern

. A class name pattern is a string following the
Java conventions for dot-separated class names. It may end with
"

.*

" meaning that the permission grants access to any
class that begins with the string preceding "

.*

". For
instance, "

javax.management.*

" grants access to

javax.management.MBeanServerDelegate

and

javax.management.timer.Timer

, among other classes.

A class name pattern can also be empty or the single character
"

*

", both of which grant access to any class.

The

member

.

For a permission you need, this is the name of the attribute or
operation you are accessing. For operations that do not reference
an attribute or operation, the member is null.

For a permission you have, this is either the name of an attribute
or operation you can access, or it is empty or the single character
"

*

", both of which grant access to any member.

The

object name

.

For a permission you need, this is the

ObjectName

of the
MBean you are accessing. For operations that do not reference a
single MBean, it is null. It is never an object name pattern.

For a permission you have, this is the

ObjectName

of the
MBean or MBeans you can access. It may be an object name pattern
to grant access to all MBeans whose names match the pattern. It
may also be empty, which grants access to all MBeans whatever their
name.

If you have an MBeanPermission, it allows operations only if all
four of the items match.

The class name, member, and object name can be written together
as a single string, which is the

name

of this permission.
The name of the permission is the string returned by

getName()

. The format of the string is:

className#member[objectName]

The object name is written using the usual syntax for

ObjectName

. It may contain any legal characters, including

]

. It is terminated by a

]

character
that is the last character in the string.

One or more of the

className

,

member

,
or

objectName

may be omitted. If the

member

is omitted, the

#

may be too (but
does not have to be). If the

objectName

is omitted,
the

[]

may be too (but does not have to be). It is
not legal to omit all three items, that is to have a

name

that is the empty string.

One or more of the

className

,

member

,
or

objectName

may be the character "

-

",
which is equivalent to a null value. A null value is implied by
any value (including another null value) but does not imply any
other value.

The possible actions are these:

- addNotificationListener
- getAttribute
- getClassLoader
- getClassLoaderFor
- getClassLoaderRepository
- getDomains
- getMBeanInfo
- getObjectInstance
- instantiate
- invoke
- isInstanceOf
- queryMBeans
- queryNames
- registerMBean
- removeNotificationListener
- setAttribute
- unregisterMBean

In a comma-separated list of actions, spaces are allowed before
and after each action.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanPermission​(
String
name,

String
actions)

Create a new MBeanPermission object with the specified target name
and actions.

The target name is of the form
"

className#member[objectName]

" where each part is
optional. It must not be empty or null.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:**
- name

- the triplet "className#member[objectName]".
- actions

- the action string.

**Throws:**
- IllegalArgumentException

- if the

name

or

actions

is invalid.

---

#### public MBeanPermission​(
String
className,

String
member,

ObjectName
objectName,

String
actions)

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

The class name, member and object name parameters define a
target name of the form
"

className#member[objectName]

" where each part is
optional. This will be the result of

Permission.getName()

on the
resultant MBeanPermission.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:**
- className

- the class name to which this permission applies.
May be null or

"-"

, which represents a class name
that is implied by any class name but does not imply any other
class name.
- member

- the member to which this permission applies. May
be null or

"-"

, which represents a member that is
implied by any member but does not imply any other member.
- objectName

- the object name to which this permission
applies. May be null, which represents an object name that is
implied by any object name but does not imply any other object
name.
- actions

- the action string.

---

### Method Details

#### public
String
getActions()

Returns the "canonical string representation" of the actions. That is,
this method always returns present actions in alphabetical order.

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the canonical string representation of the actions.

---

#### public int hashCode()

Returns the hash code value for this object.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean implies​(
Permission
p)

Checks if this MBeanPermission object "implies" the
specified permission.

More specifically, this method returns true if:

- p

is an instance of MBeanPermission; and
- p

has a null className or

p

's className
matches this object's className; and
- p

has a null member or

p

's member matches this
object's member; and
- p

has a null object name or

p

's
object name matches this object's object name; and
- p

's actions are a subset of this object's actions

If this object's className is "

*

",

p

's
className always matches it. If it is "

a.*

",

p

's
className matches it if it begins with "

a.

".

If this object's member is "

*

",

p

's
member always matches it.

If this object's objectName

n1

is an object name pattern,

p

's objectName

n2

matches it if

n1

.equals(

n2

)

or if

n1

.apply(

n2

)

.

A permission that includes the

queryMBeans

action
is considered to include

queryNames

as well.

**Specified by:**
- implies

in class

Permission

**Parameters:**
- p

- the permission to check against.

**Returns:**
- true if the specified permission is implied by this object,
false if not.

---

#### public boolean equals​(
Object
obj)

Checks two MBeanPermission objects for equality. Checks
that

obj

is an MBeanPermission, and has the same
name and actions as this object.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object we are testing for equality with this object.

**Returns:**
- true if obj is an MBeanPermission, and has the
same name and actions as this MBeanPermission object.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class MBeanPermission

java.lang.Object

- java.security.Permission
- - javax.management.MBeanPermission

java.security.Permission

- javax.management.MBeanPermission

javax.management.MBeanPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public class
MBeanPermission

extends
Permission
```

Permission controlling access to MBeanServer operations. If a
security manager has been set using

System.setSecurityManager(java.lang.SecurityManager)

, most operations on the MBean Server
require that the caller's permissions imply an MBeanPermission
appropriate for the operation. This is described in detail in the
documentation for the

MBeanServer

interface.

As with other

Permission

objects, an MBeanPermission can
represent either a permission that you

have

or a
permission that you

need

. When a sensitive operation is
being checked for permission, an MBeanPermission is constructed
representing the permission you need. The operation is only
allowed if the permissions you have

imply

the
permission you need.

An MBeanPermission contains four items of information:

- The

action

. For a permission you need,
this is one of the actions in the list

below

. For a permission you have, this is
a comma-separated list of those actions, or

*

,
representing all actions.

The action is returned by

getActions()

.

The

class name

.

For a permission you need, this is the class name of an MBean
you are accessing, as returned by

MBeanServer.getMBeanInfo(name)

.

getClassName()

. Certain operations do not reference a class name,
in which case the class name is null.

For a permission you have, this is either empty or a

class
name pattern

. A class name pattern is a string following the
Java conventions for dot-separated class names. It may end with
"

.*

" meaning that the permission grants access to any
class that begins with the string preceding "

.*

". For
instance, "

javax.management.*

" grants access to

javax.management.MBeanServerDelegate

and

javax.management.timer.Timer

, among other classes.

A class name pattern can also be empty or the single character
"

*

", both of which grant access to any class.

The

member

.

For a permission you need, this is the name of the attribute or
operation you are accessing. For operations that do not reference
an attribute or operation, the member is null.

For a permission you have, this is either the name of an attribute
or operation you can access, or it is empty or the single character
"

*

", both of which grant access to any member.

The

object name

.

For a permission you need, this is the

ObjectName

of the
MBean you are accessing. For operations that do not reference a
single MBean, it is null. It is never an object name pattern.

For a permission you have, this is the

ObjectName

of the
MBean or MBeans you can access. It may be an object name pattern
to grant access to all MBeans whose names match the pattern. It
may also be empty, which grants access to all MBeans whatever their
name.

If you have an MBeanPermission, it allows operations only if all
four of the items match.

The class name, member, and object name can be written together
as a single string, which is the

name

of this permission.
The name of the permission is the string returned by

getName()

. The format of the string is:

className#member[objectName]

The object name is written using the usual syntax for

ObjectName

. It may contain any legal characters, including

]

. It is terminated by a

]

character
that is the last character in the string.

One or more of the

className

,

member

,
or

objectName

may be omitted. If the

member

is omitted, the

#

may be too (but
does not have to be). If the

objectName

is omitted,
the

[]

may be too (but does not have to be). It is
not legal to omit all three items, that is to have a

name

that is the empty string.

One or more of the

className

,

member

,
or

objectName

may be the character "

-

",
which is equivalent to a null value. A null value is implied by
any value (including another null value) but does not imply any
other value.

The possible actions are these:

- addNotificationListener
- getAttribute
- getClassLoader
- getClassLoaderFor
- getClassLoaderRepository
- getDomains
- getMBeanInfo
- getObjectInstance
- instantiate
- invoke
- isInstanceOf
- queryMBeans
- queryNames
- registerMBean
- removeNotificationListener
- setAttribute
- unregisterMBean

In a comma-separated list of actions, spaces are allowed before
and after each action.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanPermission

extends

Permission

Permission controlling access to MBeanServer operations. If a
security manager has been set using

System.setSecurityManager(java.lang.SecurityManager)

, most operations on the MBean Server
require that the caller's permissions imply an MBeanPermission
appropriate for the operation. This is described in detail in the
documentation for the

MBeanServer

interface.

As with other

Permission

objects, an MBeanPermission can
represent either a permission that you

have

or a
permission that you

need

. When a sensitive operation is
being checked for permission, an MBeanPermission is constructed
representing the permission you need. The operation is only
allowed if the permissions you have

imply

the
permission you need.

An MBeanPermission contains four items of information:

- The

action

. For a permission you need,
this is one of the actions in the list

below

. For a permission you have, this is
a comma-separated list of those actions, or

*

,
representing all actions.

The action is returned by

getActions()

.

The

class name

.

For a permission you need, this is the class name of an MBean
you are accessing, as returned by

MBeanServer.getMBeanInfo(name)

.

getClassName()

. Certain operations do not reference a class name,
in which case the class name is null.

For a permission you have, this is either empty or a

class
name pattern

. A class name pattern is a string following the
Java conventions for dot-separated class names. It may end with
"

.*

" meaning that the permission grants access to any
class that begins with the string preceding "

.*

". For
instance, "

javax.management.*

" grants access to

javax.management.MBeanServerDelegate

and

javax.management.timer.Timer

, among other classes.

A class name pattern can also be empty or the single character
"

*

", both of which grant access to any class.

The

member

.

For a permission you need, this is the name of the attribute or
operation you are accessing. For operations that do not reference
an attribute or operation, the member is null.

For a permission you have, this is either the name of an attribute
or operation you can access, or it is empty or the single character
"

*

", both of which grant access to any member.

The

object name

.

For a permission you need, this is the

ObjectName

of the
MBean you are accessing. For operations that do not reference a
single MBean, it is null. It is never an object name pattern.

For a permission you have, this is the

ObjectName

of the
MBean or MBeans you can access. It may be an object name pattern
to grant access to all MBeans whose names match the pattern. It
may also be empty, which grants access to all MBeans whatever their
name.

If you have an MBeanPermission, it allows operations only if all
four of the items match.

The class name, member, and object name can be written together
as a single string, which is the

name

of this permission.
The name of the permission is the string returned by

getName()

. The format of the string is:

className#member[objectName]

The object name is written using the usual syntax for

ObjectName

. It may contain any legal characters, including

]

. It is terminated by a

]

character
that is the last character in the string.

One or more of the

className

,

member

,
or

objectName

may be omitted. If the

member

is omitted, the

#

may be too (but
does not have to be). If the

objectName

is omitted,
the

[]

may be too (but does not have to be). It is
not legal to omit all three items, that is to have a

name

that is the empty string.

One or more of the

className

,

member

,
or

objectName

may be the character "

-

",
which is equivalent to a null value. A null value is implied by
any value (including another null value) but does not imply any
other value.

The possible actions are these:

- addNotificationListener
- getAttribute
- getClassLoader
- getClassLoaderFor
- getClassLoaderRepository
- getDomains
- getMBeanInfo
- getObjectInstance
- instantiate
- invoke
- isInstanceOf
- queryMBeans
- queryNames
- registerMBean
- removeNotificationListener
- setAttribute
- unregisterMBean

In a comma-separated list of actions, spaces are allowed before
and after each action.

Permission controlling access to MBeanServer operations. If a
security manager has been set using

System.setSecurityManager(java.lang.SecurityManager)

, most operations on the MBean Server
require that the caller's permissions imply an MBeanPermission
appropriate for the operation. This is described in detail in the
documentation for the

MBeanServer

interface.

As with other

Permission

objects, an MBeanPermission can
represent either a permission that you

have

or a
permission that you

need

. When a sensitive operation is
being checked for permission, an MBeanPermission is constructed
representing the permission you need. The operation is only
allowed if the permissions you have

imply

the
permission you need.

An MBeanPermission contains four items of information:

The

action

. For a permission you need,
this is one of the actions in the list

below

. For a permission you have, this is
a comma-separated list of those actions, or

*

,
representing all actions.

The action is returned by

getActions()

.

The

class name

.

For a permission you need, this is the class name of an MBean
you are accessing, as returned by

MBeanServer.getMBeanInfo(name)

.

getClassName()

. Certain operations do not reference a class name,
in which case the class name is null.

For a permission you have, this is either empty or a

class
name pattern

. A class name pattern is a string following the
Java conventions for dot-separated class names. It may end with
"

.*

" meaning that the permission grants access to any
class that begins with the string preceding "

.*

". For
instance, "

javax.management.*

" grants access to

javax.management.MBeanServerDelegate

and

javax.management.timer.Timer

, among other classes.

A class name pattern can also be empty or the single character
"

*

", both of which grant access to any class.

The

member

.

For a permission you need, this is the name of the attribute or
operation you are accessing. For operations that do not reference
an attribute or operation, the member is null.

For a permission you have, this is either the name of an attribute
or operation you can access, or it is empty or the single character
"

*

", both of which grant access to any member.

The

object name

.

For a permission you need, this is the

ObjectName

of the
MBean you are accessing. For operations that do not reference a
single MBean, it is null. It is never an object name pattern.

For a permission you have, this is the

ObjectName

of the
MBean or MBeans you can access. It may be an object name pattern
to grant access to all MBeans whose names match the pattern. It
may also be empty, which grants access to all MBeans whatever their
name.

The

action

. For a permission you need,
this is one of the actions in the list

below

. For a permission you have, this is
a comma-separated list of those actions, or

*

,
representing all actions.

The action is returned by

getActions()

.

The

class name

.

For a permission you need, this is the class name of an MBean
you are accessing, as returned by

MBeanServer.getMBeanInfo(name)

.

getClassName()

. Certain operations do not reference a class name,
in which case the class name is null.

For a permission you have, this is either empty or a

class
name pattern

. A class name pattern is a string following the
Java conventions for dot-separated class names. It may end with
"

.*

" meaning that the permission grants access to any
class that begins with the string preceding "

.*

". For
instance, "

javax.management.*

" grants access to

javax.management.MBeanServerDelegate

and

javax.management.timer.Timer

, among other classes.

A class name pattern can also be empty or the single character
"

*

", both of which grant access to any class.

The

member

.

For a permission you need, this is the name of the attribute or
operation you are accessing. For operations that do not reference
an attribute or operation, the member is null.

For a permission you have, this is either the name of an attribute
or operation you can access, or it is empty or the single character
"

*

", both of which grant access to any member.

The

object name

.

For a permission you need, this is the

ObjectName

of the
MBean you are accessing. For operations that do not reference a
single MBean, it is null. It is never an object name pattern.

For a permission you have, this is the

ObjectName

of the
MBean or MBeans you can access. It may be an object name pattern
to grant access to all MBeans whose names match the pattern. It
may also be empty, which grants access to all MBeans whatever their
name.

If you have an MBeanPermission, it allows operations only if all
four of the items match.

The class name, member, and object name can be written together
as a single string, which is the

name

of this permission.
The name of the permission is the string returned by

getName()

. The format of the string is:

The object name is written using the usual syntax for

ObjectName

. It may contain any legal characters, including

]

. It is terminated by a

]

character
that is the last character in the string.

One or more of the

className

,

member

,
or

objectName

may be omitted. If the

member

is omitted, the

#

may be too (but
does not have to be). If the

objectName

is omitted,
the

[]

may be too (but does not have to be). It is
not legal to omit all three items, that is to have a

name

that is the empty string.

One or more of the

className

,

member

,
or

objectName

may be the character "

-

",
which is equivalent to a null value. A null value is implied by
any value (including another null value) but does not imply any
other value.

The possible actions are these:

addNotificationListener

getAttribute

getClassLoader

getClassLoaderFor

getClassLoaderRepository

getDomains

getMBeanInfo

getObjectInstance

instantiate

invoke

isInstanceOf

queryMBeans

queryNames

registerMBean

removeNotificationListener

setAttribute

unregisterMBean

In a comma-separated list of actions, spaces are allowed before
and after each action.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanPermission

​(

String

name,

String

actions)

Create a new MBeanPermission object with the specified target name
and actions.

MBeanPermission

​(

String

className,

String

member,

ObjectName

objectName,

String

actions)

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two MBeanPermission objects for equality.

String

getActions

()

Returns the "canonical string representation" of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this MBeanPermission object "implies" the
specified permission.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

newPermissionCollection

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

MBeanPermission

​(

String

name,

String

actions)

Create a new MBeanPermission object with the specified target name
and actions.

MBeanPermission

​(

String

className,

String

member,

ObjectName

objectName,

String

actions)

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

---

#### Constructor Summary

Create a new MBeanPermission object with the specified target name
and actions.

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two MBeanPermission objects for equality.

String

getActions

()

Returns the "canonical string representation" of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this MBeanPermission object "implies" the
specified permission.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

newPermissionCollection

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Checks two MBeanPermission objects for equality.

Returns the "canonical string representation" of the actions.

Returns the hash code value for this object.

Checks if this MBeanPermission object "implies" the
specified permission.

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

newPermissionCollection

,

toString

---

#### Methods declared in class java.security. Permission

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- MBeanPermission

```java
public MBeanPermission​(
String
name,

String
actions)
```

Create a new MBeanPermission object with the specified target name
and actions.

The target name is of the form
"

className#member[objectName]

" where each part is
optional. It must not be empty or null.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:** name

- the triplet "className#member[objectName]".
**Parameters:** actions

- the action string.
**Throws:** IllegalArgumentException

- if the

name

or

actions

is invalid.

- MBeanPermission

```java
public MBeanPermission​(
String
className,

String
member,

ObjectName
objectName,

String
actions)
```

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

The class name, member and object name parameters define a
target name of the form
"

className#member[objectName]

" where each part is
optional. This will be the result of

Permission.getName()

on the
resultant MBeanPermission.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:** className

- the class name to which this permission applies.
May be null or

"-"

, which represents a class name
that is implied by any class name but does not imply any other
class name.
**Parameters:** member

- the member to which this permission applies. May
be null or

"-"

, which represents a member that is
implied by any member but does not imply any other member.
**Parameters:** objectName

- the object name to which this permission
applies. May be null, which represents an object name that is
implied by any object name but does not imply any other object
name.
**Parameters:** actions

- the action string.

============ METHOD DETAIL ==========

- Method Detail

- getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions. That is,
this method always returns present actions in alphabetical order.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this MBeanPermission object "implies" the
specified permission.

More specifically, this method returns true if:

- p

is an instance of MBeanPermission; and
- p

has a null className or

p

's className
matches this object's className; and
- p

has a null member or

p

's member matches this
object's member; and
- p

has a null object name or

p

's
object name matches this object's object name; and
- p

's actions are a subset of this object's actions

If this object's className is "

*

",

p

's
className always matches it. If it is "

a.*

",

p

's
className matches it if it begins with "

a.

".

If this object's member is "

*

",

p

's
member always matches it.

If this object's objectName

n1

is an object name pattern,

p

's objectName

n2

matches it if

n1

.equals(

n2

)

or if

n1

.apply(

n2

)

.

A permission that includes the

queryMBeans

action
is considered to include

queryNames

as well.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two MBeanPermission objects for equality. Checks
that

obj

is an MBeanPermission, and has the same
name and actions as this object.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is an MBeanPermission, and has the
same name and actions as this MBeanPermission object.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- MBeanPermission

```java
public MBeanPermission​(
String
name,

String
actions)
```

Create a new MBeanPermission object with the specified target name
and actions.

The target name is of the form
"

className#member[objectName]

" where each part is
optional. It must not be empty or null.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:** name

- the triplet "className#member[objectName]".
**Parameters:** actions

- the action string.
**Throws:** IllegalArgumentException

- if the

name

or

actions

is invalid.

- MBeanPermission

```java
public MBeanPermission​(
String
className,

String
member,

ObjectName
objectName,

String
actions)
```

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

The class name, member and object name parameters define a
target name of the form
"

className#member[objectName]

" where each part is
optional. This will be the result of

Permission.getName()

on the
resultant MBeanPermission.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:** className

- the class name to which this permission applies.
May be null or

"-"

, which represents a class name
that is implied by any class name but does not imply any other
class name.
**Parameters:** member

- the member to which this permission applies. May
be null or

"-"

, which represents a member that is
implied by any member but does not imply any other member.
**Parameters:** objectName

- the object name to which this permission
applies. May be null, which represents an object name that is
implied by any object name but does not imply any other object
name.
**Parameters:** actions

- the action string.

---

#### Constructor Detail

MBeanPermission

```java
public MBeanPermission​(
String
name,

String
actions)
```

Create a new MBeanPermission object with the specified target name
and actions.

The target name is of the form
"

className#member[objectName]

" where each part is
optional. It must not be empty or null.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:** name

- the triplet "className#member[objectName]".
**Parameters:** actions

- the action string.
**Throws:** IllegalArgumentException

- if the

name

or

actions

is invalid.

---

#### MBeanPermission

public MBeanPermission​(

String

name,

String

actions)

Create a new MBeanPermission object with the specified target name
and actions.

The target name is of the form
"

className#member[objectName]

" where each part is
optional. It must not be empty or null.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

Create a new MBeanPermission object with the specified target name
and actions.

The target name is of the form
"

className#member[objectName]

" where each part is
optional. It must not be empty or null.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

MBeanPermission

```java
public MBeanPermission​(
String
className,

String
member,

ObjectName
objectName,

String
actions)
```

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

The class name, member and object name parameters define a
target name of the form
"

className#member[objectName]

" where each part is
optional. This will be the result of

Permission.getName()

on the
resultant MBeanPermission.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

**Parameters:** className

- the class name to which this permission applies.
May be null or

"-"

, which represents a class name
that is implied by any class name but does not imply any other
class name.
**Parameters:** member

- the member to which this permission applies. May
be null or

"-"

, which represents a member that is
implied by any member but does not imply any other member.
**Parameters:** objectName

- the object name to which this permission
applies. May be null, which represents an object name that is
implied by any object name but does not imply any other object
name.
**Parameters:** actions

- the action string.

---

#### MBeanPermission

public MBeanPermission​(

String

className,

String

member,

ObjectName

objectName,

String

actions)

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

The class name, member and object name parameters define a
target name of the form
"

className#member[objectName]

" where each part is
optional. This will be the result of

Permission.getName()

on the
resultant MBeanPermission.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

Create a new MBeanPermission object with the specified target name
(class name, member, object name) and actions.

The class name, member and object name parameters define a
target name of the form
"

className#member[objectName]

" where each part is
optional. This will be the result of

Permission.getName()

on the
resultant MBeanPermission.

The actions parameter contains a comma-separated list of the
desired actions granted on the target name. It must not be
empty or null.

Method Detail

- getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions. That is,
this method always returns present actions in alphabetical order.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this MBeanPermission object "implies" the
specified permission.

More specifically, this method returns true if:

- p

is an instance of MBeanPermission; and
- p

has a null className or

p

's className
matches this object's className; and
- p

has a null member or

p

's member matches this
object's member; and
- p

has a null object name or

p

's
object name matches this object's object name; and
- p

's actions are a subset of this object's actions

If this object's className is "

*

",

p

's
className always matches it. If it is "

a.*

",

p

's
className matches it if it begins with "

a.

".

If this object's member is "

*

",

p

's
member always matches it.

If this object's objectName

n1

is an object name pattern,

p

's objectName

n2

matches it if

n1

.equals(

n2

)

or if

n1

.apply(

n2

)

.

A permission that includes the

queryMBeans

action
is considered to include

queryNames

as well.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two MBeanPermission objects for equality. Checks
that

obj

is an MBeanPermission, and has the same
name and actions as this object.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is an MBeanPermission, and has the
same name and actions as this MBeanPermission object.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getActions

```java
public
String
getActions()
```

Returns the "canonical string representation" of the actions. That is,
this method always returns present actions in alphabetical order.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

---

#### getActions

public

String

getActions()

Returns the "canonical string representation" of the actions. That is,
this method always returns present actions in alphabetical order.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this MBeanPermission object "implies" the
specified permission.

More specifically, this method returns true if:

- p

is an instance of MBeanPermission; and
- p

has a null className or

p

's className
matches this object's className; and
- p

has a null member or

p

's member matches this
object's member; and
- p

has a null object name or

p

's
object name matches this object's object name; and
- p

's actions are a subset of this object's actions

If this object's className is "

*

",

p

's
className always matches it. If it is "

a.*

",

p

's
className matches it if it begins with "

a.

".

If this object's member is "

*

",

p

's
member always matches it.

If this object's objectName

n1

is an object name pattern,

p

's objectName

n2

matches it if

n1

.equals(

n2

)

or if

n1

.apply(

n2

)

.

A permission that includes the

queryMBeans

action
is considered to include

queryNames

as well.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

---

#### implies

public boolean implies​(

Permission

p)

Checks if this MBeanPermission object "implies" the
specified permission.

More specifically, this method returns true if:

- p

is an instance of MBeanPermission; and
- p

has a null className or

p

's className
matches this object's className; and
- p

has a null member or

p

's member matches this
object's member; and
- p

has a null object name or

p

's
object name matches this object's object name; and
- p

's actions are a subset of this object's actions

If this object's className is "

*

",

p

's
className always matches it. If it is "

a.*

",

p

's
className matches it if it begins with "

a.

".

If this object's member is "

*

",

p

's
member always matches it.

If this object's objectName

n1

is an object name pattern,

p

's objectName

n2

matches it if

n1

.equals(

n2

)

or if

n1

.apply(

n2

)

.

A permission that includes the

queryMBeans

action
is considered to include

queryNames

as well.

Checks if this MBeanPermission object "implies" the
specified permission.

More specifically, this method returns true if:

p

is an instance of MBeanPermission; and

p

has a null className or

p

's className
matches this object's className; and

p

has a null member or

p

's member matches this
object's member; and

p

has a null object name or

p

's
object name matches this object's object name; and

p

's actions are a subset of this object's actions

If this object's className is "

*

",

p

's
className always matches it. If it is "

a.*

",

p

's
className matches it if it begins with "

a.

".

If this object's member is "

*

",

p

's
member always matches it.

If this object's objectName

n1

is an object name pattern,

p

's objectName

n2

matches it if

n1

.equals(

n2

)

or if

n1

.apply(

n2

)

.

A permission that includes the

queryMBeans

action
is considered to include

queryNames

as well.

equals

```java
public boolean equals​(
Object
obj)
```

Checks two MBeanPermission objects for equality. Checks
that

obj

is an MBeanPermission, and has the same
name and actions as this object.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object we are testing for equality with this object.
**Returns:** true if obj is an MBeanPermission, and has the
same name and actions as this MBeanPermission object.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two MBeanPermission objects for equality. Checks
that

obj

is an MBeanPermission, and has the same
name and actions as this object.

---

