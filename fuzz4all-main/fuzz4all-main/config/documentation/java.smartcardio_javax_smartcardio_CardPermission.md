# Class CardPermission

**Source:** `java.smartcardio\javax\smartcardio\CardPermission.html`

### Class Description

```java
public class
CardPermission

extends
Permission
```

A permission for Smart Card operations. A CardPermission consists of the
name of the card terminal the permission applies to and a set of actions
that are valid for that terminal.

A CardPermission with a name of

*

applies to all
card terminals. The actions string is a comma separated list of the actions
listed below, or

*

to signify "all actions."

Individual actions are:

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public CardPermission​(
String
terminalName,

String
actions)

Constructs a new CardPermission with the specified actions.

terminalName

is the name of a CardTerminal or

*

if this permission applies to all terminals.

actions

contains a comma-separated list of the individual actions
or

*

to signify all actions. For more information,
see the documentation at the top of this

class

.

**Parameters:**
- terminalName

- the name of the card terminal, or

*
- actions

- the action string (or null if the set of permitted
actions is empty)

**Throws:**
- NullPointerException

- if terminalName is null
- IllegalArgumentException

- if actions is an invalid actions
specification

---

### Method Details

#### public
String
getActions()

Returns the canonical string representation of the actions.
It is

*

to signify all actions defined by this class or
the string concatenation of the comma-separated,
lexicographically sorted list of individual actions.

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the canonical string representation of the actions.

---

#### public boolean implies​(
Permission
permission)

Checks if this CardPermission object implies the specified permission.
That is the case, if and only if

- permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

**Specified by:**
- implies

in class

Permission

**Parameters:**
- permission

- the permission to check against

**Returns:**
- true if and only if this CardPermission object implies the
specified permission.

---

#### public boolean equals​(
Object
obj)

Compares the specified object with this CardPermission for equality.
This CardPermission is equal to another Object

object

, if
and only if

- object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object to be compared for equality with this CardPermission

**Returns:**
- true if and only if the specified object is equal to this
CardPermission

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this CardPermission object.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- the hash code value for this CardPermission object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class CardPermission

java.lang.Object

- java.security.Permission
- - javax.smartcardio.CardPermission

java.security.Permission

- javax.smartcardio.CardPermission

javax.smartcardio.CardPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public class
CardPermission

extends
Permission
```

A permission for Smart Card operations. A CardPermission consists of the
name of the card terminal the permission applies to and a set of actions
that are valid for that terminal.

A CardPermission with a name of

*

applies to all
card terminals. The actions string is a comma separated list of the actions
listed below, or

*

to signify "all actions."

Individual actions are:

**Since:** 1.6
**See Also:** Serialized Form

public class

CardPermission

extends

Permission

A permission for Smart Card operations. A CardPermission consists of the
name of the card terminal the permission applies to and a set of actions
that are valid for that terminal.

A CardPermission with a name of

*

applies to all
card terminals. The actions string is a comma separated list of the actions
listed below, or

*

to signify "all actions."

Individual actions are:

A CardPermission with a name of

*

applies to all
card terminals. The actions string is a comma separated list of the actions
listed below, or

*

to signify "all actions."

Individual actions are:

Individual actions are:

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CardPermission

​(

String

terminalName,

String

actions)

Constructs a new CardPermission with the specified actions.

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

Compares the specified object with this CardPermission for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this CardPermission object.

boolean

implies

​(

Permission

permission)

Checks if this CardPermission object implies the specified permission.

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

CardPermission

​(

String

terminalName,

String

actions)

Constructs a new CardPermission with the specified actions.

---

#### Constructor Summary

Constructs a new CardPermission with the specified actions.

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

Compares the specified object with this CardPermission for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this CardPermission object.

boolean

implies

​(

Permission

permission)

Checks if this CardPermission object implies the specified permission.

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

Compares the specified object with this CardPermission for equality.

Returns the canonical string representation of the actions.

Returns the hash code value for this CardPermission object.

Checks if this CardPermission object implies the specified permission.

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

- CardPermission

```java
public CardPermission​(
String
terminalName,

String
actions)
```

Constructs a new CardPermission with the specified actions.

terminalName

is the name of a CardTerminal or

*

if this permission applies to all terminals.

actions

contains a comma-separated list of the individual actions
or

*

to signify all actions. For more information,
see the documentation at the top of this

class

.

**Parameters:** terminalName

- the name of the card terminal, or

*
**Parameters:** actions

- the action string (or null if the set of permitted
actions is empty)
**Throws:** NullPointerException

- if terminalName is null
**Throws:** IllegalArgumentException

- if actions is an invalid actions
specification

============ METHOD DETAIL ==========

- Method Detail

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
It is

*

to signify all actions defined by this class or
the string concatenation of the comma-separated,
lexicographically sorted list of individual actions.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

- implies

```java
public boolean implies​(
Permission
permission)
```

Checks if this CardPermission object implies the specified permission.
That is the case, if and only if

- permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

**Specified by:** implies

in class

Permission
**Parameters:** permission

- the permission to check against
**Returns:** true if and only if this CardPermission object implies the
specified permission.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this CardPermission for equality.
This CardPermission is equal to another Object

object

, if
and only if

- object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to be compared for equality with this CardPermission
**Returns:** true if and only if the specified object is equal to this
CardPermission
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this CardPermission object.

**Specified by:** hashCode

in class

Permission
**Returns:** the hash code value for this CardPermission object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- CardPermission

```java
public CardPermission​(
String
terminalName,

String
actions)
```

Constructs a new CardPermission with the specified actions.

terminalName

is the name of a CardTerminal or

*

if this permission applies to all terminals.

actions

contains a comma-separated list of the individual actions
or

*

to signify all actions. For more information,
see the documentation at the top of this

class

.

**Parameters:** terminalName

- the name of the card terminal, or

*
**Parameters:** actions

- the action string (or null if the set of permitted
actions is empty)
**Throws:** NullPointerException

- if terminalName is null
**Throws:** IllegalArgumentException

- if actions is an invalid actions
specification

---

#### Constructor Detail

CardPermission

```java
public CardPermission​(
String
terminalName,

String
actions)
```

Constructs a new CardPermission with the specified actions.

terminalName

is the name of a CardTerminal or

*

if this permission applies to all terminals.

actions

contains a comma-separated list of the individual actions
or

*

to signify all actions. For more information,
see the documentation at the top of this

class

.

**Parameters:** terminalName

- the name of the card terminal, or

*
**Parameters:** actions

- the action string (or null if the set of permitted
actions is empty)
**Throws:** NullPointerException

- if terminalName is null
**Throws:** IllegalArgumentException

- if actions is an invalid actions
specification

---

#### CardPermission

public CardPermission​(

String

terminalName,

String

actions)

Constructs a new CardPermission with the specified actions.

terminalName

is the name of a CardTerminal or

*

if this permission applies to all terminals.

actions

contains a comma-separated list of the individual actions
or

*

to signify all actions. For more information,
see the documentation at the top of this

class

.

Method Detail

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
It is

*

to signify all actions defined by this class or
the string concatenation of the comma-separated,
lexicographically sorted list of individual actions.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

- implies

```java
public boolean implies​(
Permission
permission)
```

Checks if this CardPermission object implies the specified permission.
That is the case, if and only if

- permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

**Specified by:** implies

in class

Permission
**Parameters:** permission

- the permission to check against
**Returns:** true if and only if this CardPermission object implies the
specified permission.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this CardPermission for equality.
This CardPermission is equal to another Object

object

, if
and only if

- object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to be compared for equality with this CardPermission
**Returns:** true if and only if the specified object is equal to this
CardPermission
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this CardPermission object.

**Specified by:** hashCode

in class

Permission
**Returns:** the hash code value for this CardPermission object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
It is

*

to signify all actions defined by this class or
the string concatenation of the comma-separated,
lexicographically sorted list of individual actions.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

---

#### getActions

public

String

getActions()

Returns the canonical string representation of the actions.
It is

*

to signify all actions defined by this class or
the string concatenation of the comma-separated,
lexicographically sorted list of individual actions.

implies

```java
public boolean implies​(
Permission
permission)
```

Checks if this CardPermission object implies the specified permission.
That is the case, if and only if

- permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

**Specified by:** implies

in class

Permission
**Parameters:** permission

- the permission to check against
**Returns:** true if and only if this CardPermission object implies the
specified permission.

---

#### implies

public boolean implies​(

Permission

permission)

Checks if this CardPermission object implies the specified permission.
That is the case, if and only if

- permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

permission

is an instance of CardPermission,

permission

's actions are a proper subset of this
object's actions, and

this object's

getName()

method is either

*

or equal to

permission

's

name

.

equals

```java
public boolean equals​(
Object
obj)
```

Compares the specified object with this CardPermission for equality.
This CardPermission is equal to another Object

object

, if
and only if

- object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to be compared for equality with this CardPermission
**Returns:** true if and only if the specified object is equal to this
CardPermission
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares the specified object with this CardPermission for equality.
This CardPermission is equal to another Object

object

, if
and only if

- object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

object

is an instance of CardPermission,

this.getName()

is equal to

((CardPermission)object).getName()

, and

this.getActions()

is equal to

((CardPermission)object).getActions()

.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this CardPermission object.

**Specified by:** hashCode

in class

Permission
**Returns:** the hash code value for this CardPermission object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this CardPermission object.

---

