# Class ActionMap

**Source:** `java.desktop\javax\swing\ActionMap.html`

### Class Description

```java
public class
ActionMap

extends
Object

implements
Serializable
```

ActionMap

provides mappings from

Object

s
(called

keys

or

Action

names

)
to

Action

s.
An

ActionMap

is usually used with an

InputMap

to locate a particular action
when a key is pressed. As with

InputMap

,
an

ActionMap

can have a parent
that is searched for keys not defined in the

ActionMap

.

As with

InputMap

if you create a cycle, eg:

```java
ActionMap am = new ActionMap();
ActionMap bm = new ActionMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ActionMap()

Creates an

ActionMap

with no parent and no mappings.

---

### Method Details

#### public void setParent​(
ActionMap
map)

Sets this

ActionMap

's parent.

**Parameters:**
- map

- the

ActionMap

that is the parent of this one

---

#### public
ActionMap
getParent()

Returns this

ActionMap

's parent.

**Returns:**
- the

ActionMap

that is the parent of this one,
or null if this

ActionMap

has no parent

---

#### public void put​(
Object
key,

Action
action)

Adds a binding for

key

to

action

.
If

action

is null, this removes the current binding
for

key

.

In most instances,

key

will be

action.getValue(NAME)

.

**Parameters:**
- key

- a key
- action

- a binding for

key

---

#### public
Action
get​(
Object
key)

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

**Parameters:**
- key

- a key

**Returns:**
- the binding for

key

---

#### public void remove​(
Object
key)

Removes the binding for

key

from this

ActionMap

.

**Parameters:**
- key

- a key

---

#### public void clear()

Removes all the mappings from this

ActionMap

.

---

#### public
Object
[] keys()

Returns the

Action

names that are bound in this

ActionMap

.

**Returns:**
- an array of the keys

---

#### public int size()

Returns the number of bindings in this

ActionMap

.

**Returns:**
- the number of bindings in this

ActionMap

---

#### public
Object
[] allKeys()

Returns an array of the keys defined in this

ActionMap

and
its parent. This method differs from

keys()

in that
this method includes the keys defined in the parent.

**Returns:**
- an array of the keys

---

### Additional Sections

#### Class ActionMap

java.lang.Object

- javax.swing.ActionMap

javax.swing.ActionMap

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ActionMapUIResource

```java
public class
ActionMap

extends
Object

implements
Serializable
```

ActionMap

provides mappings from

Object

s
(called

keys

or

Action

names

)
to

Action

s.
An

ActionMap

is usually used with an

InputMap

to locate a particular action
when a key is pressed. As with

InputMap

,
an

ActionMap

can have a parent
that is searched for keys not defined in the

ActionMap

.

As with

InputMap

if you create a cycle, eg:

```java
ActionMap am = new ActionMap();
ActionMap bm = new ActionMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

**Since:** 1.3
**See Also:** InputMap

,

Serialized Form

public class

ActionMap

extends

Object

implements

Serializable

ActionMap

provides mappings from

Object

s
(called

keys

or

Action

names

)
to

Action

s.
An

ActionMap

is usually used with an

InputMap

to locate a particular action
when a key is pressed. As with

InputMap

,
an

ActionMap

can have a parent
that is searched for keys not defined in the

ActionMap

.

As with

InputMap

if you create a cycle, eg:

```java
ActionMap am = new ActionMap();
ActionMap bm = new ActionMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

As with

InputMap

if you create a cycle, eg:

```java
ActionMap am = new ActionMap();
ActionMap bm = new ActionMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

ActionMap am = new ActionMap();
ActionMap bm = new ActionMap():
am.setParent(bm);
bm.setParent(am);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActionMap

()

Creates an

ActionMap

with no parent and no mappings.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

[]

allKeys

()

Returns an array of the keys defined in this

ActionMap

and
its parent.

void

clear

()

Removes all the mappings from this

ActionMap

.

Action

get

​(

Object

key)

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

ActionMap

getParent

()

Returns this

ActionMap

's parent.

Object

[]

keys

()

Returns the

Action

names that are bound in this

ActionMap

.

void

put

​(

Object

key,

Action

action)

Adds a binding for

key

to

action

.

void

remove

​(

Object

key)

Removes the binding for

key

from this

ActionMap

.

void

setParent

​(

ActionMap

map)

Sets this

ActionMap

's parent.

int

size

()

Returns the number of bindings in this

ActionMap

.

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

ActionMap

()

Creates an

ActionMap

with no parent and no mappings.

---

#### Constructor Summary

Creates an

ActionMap

with no parent and no mappings.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

[]

allKeys

()

Returns an array of the keys defined in this

ActionMap

and
its parent.

void

clear

()

Removes all the mappings from this

ActionMap

.

Action

get

​(

Object

key)

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

ActionMap

getParent

()

Returns this

ActionMap

's parent.

Object

[]

keys

()

Returns the

Action

names that are bound in this

ActionMap

.

void

put

​(

Object

key,

Action

action)

Adds a binding for

key

to

action

.

void

remove

​(

Object

key)

Removes the binding for

key

from this

ActionMap

.

void

setParent

​(

ActionMap

map)

Sets this

ActionMap

's parent.

int

size

()

Returns the number of bindings in this

ActionMap

.

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

Returns an array of the keys defined in this

ActionMap

and
its parent.

Removes all the mappings from this

ActionMap

.

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

Returns this

ActionMap

's parent.

Returns the

Action

names that are bound in this

ActionMap

.

Adds a binding for

key

to

action

.

Removes the binding for

key

from this

ActionMap

.

Sets this

ActionMap

's parent.

Returns the number of bindings in this

ActionMap

.

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

- ActionMap

```java
public ActionMap()
```

Creates an

ActionMap

with no parent and no mappings.

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
ActionMap
map)
```

Sets this

ActionMap

's parent.

**Parameters:** map

- the

ActionMap

that is the parent of this one

- getParent

```java
public
ActionMap
getParent()
```

Returns this

ActionMap

's parent.

**Returns:** the

ActionMap

that is the parent of this one,
or null if this

ActionMap

has no parent

- put

```java
public void put​(
Object
key,

Action
action)
```

Adds a binding for

key

to

action

.
If

action

is null, this removes the current binding
for

key

.

In most instances,

key

will be

action.getValue(NAME)

.

**Parameters:** key

- a key
**Parameters:** action

- a binding for

key

- get

```java
public
Action
get​(
Object
key)
```

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

**Parameters:** key

- a key
**Returns:** the binding for

key

- remove

```java
public void remove​(
Object
key)
```

Removes the binding for

key

from this

ActionMap

.

**Parameters:** key

- a key

- clear

```java
public void clear()
```

Removes all the mappings from this

ActionMap

.

- keys

```java
public
Object
[] keys()
```

Returns the

Action

names that are bound in this

ActionMap

.

**Returns:** an array of the keys

- size

```java
public int size()
```

Returns the number of bindings in this

ActionMap

.

**Returns:** the number of bindings in this

ActionMap

- allKeys

```java
public
Object
[] allKeys()
```

Returns an array of the keys defined in this

ActionMap

and
its parent. This method differs from

keys()

in that
this method includes the keys defined in the parent.

**Returns:** an array of the keys

Constructor Detail

- ActionMap

```java
public ActionMap()
```

Creates an

ActionMap

with no parent and no mappings.

---

#### Constructor Detail

ActionMap

```java
public ActionMap()
```

Creates an

ActionMap

with no parent and no mappings.

---

#### ActionMap

public ActionMap()

Creates an

ActionMap

with no parent and no mappings.

Method Detail

- setParent

```java
public void setParent​(
ActionMap
map)
```

Sets this

ActionMap

's parent.

**Parameters:** map

- the

ActionMap

that is the parent of this one

- getParent

```java
public
ActionMap
getParent()
```

Returns this

ActionMap

's parent.

**Returns:** the

ActionMap

that is the parent of this one,
or null if this

ActionMap

has no parent

- put

```java
public void put​(
Object
key,

Action
action)
```

Adds a binding for

key

to

action

.
If

action

is null, this removes the current binding
for

key

.

In most instances,

key

will be

action.getValue(NAME)

.

**Parameters:** key

- a key
**Parameters:** action

- a binding for

key

- get

```java
public
Action
get​(
Object
key)
```

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

**Parameters:** key

- a key
**Returns:** the binding for

key

- remove

```java
public void remove​(
Object
key)
```

Removes the binding for

key

from this

ActionMap

.

**Parameters:** key

- a key

- clear

```java
public void clear()
```

Removes all the mappings from this

ActionMap

.

- keys

```java
public
Object
[] keys()
```

Returns the

Action

names that are bound in this

ActionMap

.

**Returns:** an array of the keys

- size

```java
public int size()
```

Returns the number of bindings in this

ActionMap

.

**Returns:** the number of bindings in this

ActionMap

- allKeys

```java
public
Object
[] allKeys()
```

Returns an array of the keys defined in this

ActionMap

and
its parent. This method differs from

keys()

in that
this method includes the keys defined in the parent.

**Returns:** an array of the keys

---

#### Method Detail

setParent

```java
public void setParent​(
ActionMap
map)
```

Sets this

ActionMap

's parent.

**Parameters:** map

- the

ActionMap

that is the parent of this one

---

#### setParent

public void setParent​(

ActionMap

map)

Sets this

ActionMap

's parent.

getParent

```java
public
ActionMap
getParent()
```

Returns this

ActionMap

's parent.

**Returns:** the

ActionMap

that is the parent of this one,
or null if this

ActionMap

has no parent

---

#### getParent

public

ActionMap

getParent()

Returns this

ActionMap

's parent.

put

```java
public void put​(
Object
key,

Action
action)
```

Adds a binding for

key

to

action

.
If

action

is null, this removes the current binding
for

key

.

In most instances,

key

will be

action.getValue(NAME)

.

**Parameters:** key

- a key
**Parameters:** action

- a binding for

key

---

#### put

public void put​(

Object

key,

Action

action)

Adds a binding for

key

to

action

.
If

action

is null, this removes the current binding
for

key

.

In most instances,

key

will be

action.getValue(NAME)

.

In most instances,

key

will be

action.getValue(NAME)

.

get

```java
public
Action
get​(
Object
key)
```

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

**Parameters:** key

- a key
**Returns:** the binding for

key

---

#### get

public

Action

get​(

Object

key)

Returns the binding for

key

, messaging the
parent

ActionMap

if the binding is not locally defined.

remove

```java
public void remove​(
Object
key)
```

Removes the binding for

key

from this

ActionMap

.

**Parameters:** key

- a key

---

#### remove

public void remove​(

Object

key)

Removes the binding for

key

from this

ActionMap

.

clear

```java
public void clear()
```

Removes all the mappings from this

ActionMap

.

---

#### clear

public void clear()

Removes all the mappings from this

ActionMap

.

keys

```java
public
Object
[] keys()
```

Returns the

Action

names that are bound in this

ActionMap

.

**Returns:** an array of the keys

---

#### keys

public

Object

[] keys()

Returns the

Action

names that are bound in this

ActionMap

.

size

```java
public int size()
```

Returns the number of bindings in this

ActionMap

.

**Returns:** the number of bindings in this

ActionMap

---

#### size

public int size()

Returns the number of bindings in this

ActionMap

.

allKeys

```java
public
Object
[] allKeys()
```

Returns an array of the keys defined in this

ActionMap

and
its parent. This method differs from

keys()

in that
this method includes the keys defined in the parent.

**Returns:** an array of the keys

---

#### allKeys

public

Object

[] allKeys()

Returns an array of the keys defined in this

ActionMap

and
its parent. This method differs from

keys()

in that
this method includes the keys defined in the parent.

---

