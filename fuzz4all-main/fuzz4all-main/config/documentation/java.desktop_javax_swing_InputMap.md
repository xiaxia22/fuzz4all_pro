# Class InputMap

**Source:** `java.desktop\javax\swing\InputMap.html`

### Class Description

```java
public class
InputMap

extends
Object

implements
Serializable
```

InputMap

provides a binding between an input event (currently only

KeyStroke

s are used) and an

Object

.

InputMap

s are
usually used with an

ActionMap

, to determine an

Action

to
perform when a key is pressed. An

InputMap

can have a parent that
is searched for bindings not defined in the

InputMap

.

As with

ActionMap

if you create a cycle, eg:

```java
InputMap am = new InputMap();
InputMap bm = new InputMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InputMap()

Creates an

InputMap

with no parent and no mappings.

---

### Method Details

#### public void setParent​(
InputMap
map)

Sets this

InputMap

's parent.

**Parameters:**
- map

- the

InputMap

that is the parent of this one

---

#### public
InputMap
getParent()

Gets this

InputMap

's parent.

**Returns:**
- map the

InputMap

that is the parent of this one,
or null if this

InputMap

has no parent

---

#### public void put​(
KeyStroke
keyStroke,

Object
actionMapKey)

Adds a binding for

keyStroke

to

actionMapKey

.
If

actionMapKey

is null, this removes the current binding
for

keyStroke

.

**Parameters:**
- keyStroke

- a

KeyStroke
- actionMapKey

- an action map key

---

#### public
Object
get​(
KeyStroke
keyStroke)

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

**Parameters:**
- keyStroke

- the

KeyStroke

for which to get the binding

**Returns:**
- the binding for

keyStroke

---

#### public void remove​(
KeyStroke
key)

Removes the binding for

key

from this

InputMap

.

**Parameters:**
- key

- the

KeyStroke

for which to remove the binding

---

#### public void clear()

Removes all the mappings from this

InputMap

.

---

#### public
KeyStroke
[] keys()

Returns the

KeyStroke

s that are bound in this

InputMap

.

**Returns:**
- an array of the

KeyStroke

s that are bound in this

InputMap

---

#### public int size()

Returns the number of

KeyStroke

bindings.

**Returns:**
- the number of

KeyStroke

bindings

---

#### public
KeyStroke
[] allKeys()

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent. This differs from

keys()

in that this method includes the keys defined in the parent.

**Returns:**
- an array of the

KeyStroke

s defined in this

InputMap

and its parent

---

### Additional Sections

#### Class InputMap

java.lang.Object

- javax.swing.InputMap

javax.swing.InputMap

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ComponentInputMap

,

InputMapUIResource

```java
public class
InputMap

extends
Object

implements
Serializable
```

InputMap

provides a binding between an input event (currently only

KeyStroke

s are used) and an

Object

.

InputMap

s are
usually used with an

ActionMap

, to determine an

Action

to
perform when a key is pressed. An

InputMap

can have a parent that
is searched for bindings not defined in the

InputMap

.

As with

ActionMap

if you create a cycle, eg:

```java
InputMap am = new InputMap();
InputMap bm = new InputMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

**Since:** 1.3
**See Also:** Serialized Form

public class

InputMap

extends

Object

implements

Serializable

InputMap

provides a binding between an input event (currently only

KeyStroke

s are used) and an

Object

.

InputMap

s are
usually used with an

ActionMap

, to determine an

Action

to
perform when a key is pressed. An

InputMap

can have a parent that
is searched for bindings not defined in the

InputMap

.

As with

ActionMap

if you create a cycle, eg:

```java
InputMap am = new InputMap();
InputMap bm = new InputMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

As with

ActionMap

if you create a cycle, eg:

```java
InputMap am = new InputMap();
InputMap bm = new InputMap():
am.setParent(bm);
bm.setParent(am);
```

some of the methods will cause a StackOverflowError to be thrown.

InputMap am = new InputMap();
InputMap bm = new InputMap():
am.setParent(bm);
bm.setParent(am);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InputMap

()

Creates an

InputMap

with no parent and no mappings.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

KeyStroke

[]

allKeys

()

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent.

void

clear

()

Removes all the mappings from this

InputMap

.

Object

get

​(

KeyStroke

keyStroke)

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

InputMap

getParent

()

Gets this

InputMap

's parent.

KeyStroke

[]

keys

()

Returns the

KeyStroke

s that are bound in this

InputMap

.

void

put

​(

KeyStroke

keyStroke,

Object

actionMapKey)

Adds a binding for

keyStroke

to

actionMapKey

.

void

remove

​(

KeyStroke

key)

Removes the binding for

key

from this

InputMap

.

void

setParent

​(

InputMap

map)

Sets this

InputMap

's parent.

int

size

()

Returns the number of

KeyStroke

bindings.

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

InputMap

()

Creates an

InputMap

with no parent and no mappings.

---

#### Constructor Summary

Creates an

InputMap

with no parent and no mappings.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

KeyStroke

[]

allKeys

()

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent.

void

clear

()

Removes all the mappings from this

InputMap

.

Object

get

​(

KeyStroke

keyStroke)

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

InputMap

getParent

()

Gets this

InputMap

's parent.

KeyStroke

[]

keys

()

Returns the

KeyStroke

s that are bound in this

InputMap

.

void

put

​(

KeyStroke

keyStroke,

Object

actionMapKey)

Adds a binding for

keyStroke

to

actionMapKey

.

void

remove

​(

KeyStroke

key)

Removes the binding for

key

from this

InputMap

.

void

setParent

​(

InputMap

map)

Sets this

InputMap

's parent.

int

size

()

Returns the number of

KeyStroke

bindings.

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

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent.

Removes all the mappings from this

InputMap

.

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

Gets this

InputMap

's parent.

Returns the

KeyStroke

s that are bound in this

InputMap

.

Adds a binding for

keyStroke

to

actionMapKey

.

Removes the binding for

key

from this

InputMap

.

Sets this

InputMap

's parent.

Returns the number of

KeyStroke

bindings.

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

- InputMap

```java
public InputMap()
```

Creates an

InputMap

with no parent and no mappings.

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
InputMap
map)
```

Sets this

InputMap

's parent.

**Parameters:** map

- the

InputMap

that is the parent of this one

- getParent

```java
public
InputMap
getParent()
```

Gets this

InputMap

's parent.

**Returns:** map the

InputMap

that is the parent of this one,
or null if this

InputMap

has no parent

- put

```java
public void put​(
KeyStroke
keyStroke,

Object
actionMapKey)
```

Adds a binding for

keyStroke

to

actionMapKey

.
If

actionMapKey

is null, this removes the current binding
for

keyStroke

.

**Parameters:** keyStroke

- a

KeyStroke
**Parameters:** actionMapKey

- an action map key

- get

```java
public
Object
get​(
KeyStroke
keyStroke)
```

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

**Parameters:** keyStroke

- the

KeyStroke

for which to get the binding
**Returns:** the binding for

keyStroke

- remove

```java
public void remove​(
KeyStroke
key)
```

Removes the binding for

key

from this

InputMap

.

**Parameters:** key

- the

KeyStroke

for which to remove the binding

- clear

```java
public void clear()
```

Removes all the mappings from this

InputMap

.

- keys

```java
public
KeyStroke
[] keys()
```

Returns the

KeyStroke

s that are bound in this

InputMap

.

**Returns:** an array of the

KeyStroke

s that are bound in this

InputMap

- size

```java
public int size()
```

Returns the number of

KeyStroke

bindings.

**Returns:** the number of

KeyStroke

bindings

- allKeys

```java
public
KeyStroke
[] allKeys()
```

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent. This differs from

keys()

in that this method includes the keys defined in the parent.

**Returns:** an array of the

KeyStroke

s defined in this

InputMap

and its parent

Constructor Detail

- InputMap

```java
public InputMap()
```

Creates an

InputMap

with no parent and no mappings.

---

#### Constructor Detail

InputMap

```java
public InputMap()
```

Creates an

InputMap

with no parent and no mappings.

---

#### InputMap

public InputMap()

Creates an

InputMap

with no parent and no mappings.

Method Detail

- setParent

```java
public void setParent​(
InputMap
map)
```

Sets this

InputMap

's parent.

**Parameters:** map

- the

InputMap

that is the parent of this one

- getParent

```java
public
InputMap
getParent()
```

Gets this

InputMap

's parent.

**Returns:** map the

InputMap

that is the parent of this one,
or null if this

InputMap

has no parent

- put

```java
public void put​(
KeyStroke
keyStroke,

Object
actionMapKey)
```

Adds a binding for

keyStroke

to

actionMapKey

.
If

actionMapKey

is null, this removes the current binding
for

keyStroke

.

**Parameters:** keyStroke

- a

KeyStroke
**Parameters:** actionMapKey

- an action map key

- get

```java
public
Object
get​(
KeyStroke
keyStroke)
```

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

**Parameters:** keyStroke

- the

KeyStroke

for which to get the binding
**Returns:** the binding for

keyStroke

- remove

```java
public void remove​(
KeyStroke
key)
```

Removes the binding for

key

from this

InputMap

.

**Parameters:** key

- the

KeyStroke

for which to remove the binding

- clear

```java
public void clear()
```

Removes all the mappings from this

InputMap

.

- keys

```java
public
KeyStroke
[] keys()
```

Returns the

KeyStroke

s that are bound in this

InputMap

.

**Returns:** an array of the

KeyStroke

s that are bound in this

InputMap

- size

```java
public int size()
```

Returns the number of

KeyStroke

bindings.

**Returns:** the number of

KeyStroke

bindings

- allKeys

```java
public
KeyStroke
[] allKeys()
```

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent. This differs from

keys()

in that this method includes the keys defined in the parent.

**Returns:** an array of the

KeyStroke

s defined in this

InputMap

and its parent

---

#### Method Detail

setParent

```java
public void setParent​(
InputMap
map)
```

Sets this

InputMap

's parent.

**Parameters:** map

- the

InputMap

that is the parent of this one

---

#### setParent

public void setParent​(

InputMap

map)

Sets this

InputMap

's parent.

getParent

```java
public
InputMap
getParent()
```

Gets this

InputMap

's parent.

**Returns:** map the

InputMap

that is the parent of this one,
or null if this

InputMap

has no parent

---

#### getParent

public

InputMap

getParent()

Gets this

InputMap

's parent.

put

```java
public void put​(
KeyStroke
keyStroke,

Object
actionMapKey)
```

Adds a binding for

keyStroke

to

actionMapKey

.
If

actionMapKey

is null, this removes the current binding
for

keyStroke

.

**Parameters:** keyStroke

- a

KeyStroke
**Parameters:** actionMapKey

- an action map key

---

#### put

public void put​(

KeyStroke

keyStroke,

Object

actionMapKey)

Adds a binding for

keyStroke

to

actionMapKey

.
If

actionMapKey

is null, this removes the current binding
for

keyStroke

.

get

```java
public
Object
get​(
KeyStroke
keyStroke)
```

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

**Parameters:** keyStroke

- the

KeyStroke

for which to get the binding
**Returns:** the binding for

keyStroke

---

#### get

public

Object

get​(

KeyStroke

keyStroke)

Returns the binding for

keyStroke

, messaging the
parent

InputMap

if the binding is not locally defined.

remove

```java
public void remove​(
KeyStroke
key)
```

Removes the binding for

key

from this

InputMap

.

**Parameters:** key

- the

KeyStroke

for which to remove the binding

---

#### remove

public void remove​(

KeyStroke

key)

Removes the binding for

key

from this

InputMap

.

clear

```java
public void clear()
```

Removes all the mappings from this

InputMap

.

---

#### clear

public void clear()

Removes all the mappings from this

InputMap

.

keys

```java
public
KeyStroke
[] keys()
```

Returns the

KeyStroke

s that are bound in this

InputMap

.

**Returns:** an array of the

KeyStroke

s that are bound in this

InputMap

---

#### keys

public

KeyStroke

[] keys()

Returns the

KeyStroke

s that are bound in this

InputMap

.

size

```java
public int size()
```

Returns the number of

KeyStroke

bindings.

**Returns:** the number of

KeyStroke

bindings

---

#### size

public int size()

Returns the number of

KeyStroke

bindings.

allKeys

```java
public
KeyStroke
[] allKeys()
```

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent. This differs from

keys()

in that this method includes the keys defined in the parent.

**Returns:** an array of the

KeyStroke

s defined in this

InputMap

and its parent

---

#### allKeys

public

KeyStroke

[] allKeys()

Returns an array of the

KeyStroke

s defined in this

InputMap

and its parent. This differs from

keys()

in that this method includes the keys defined in the parent.

---

