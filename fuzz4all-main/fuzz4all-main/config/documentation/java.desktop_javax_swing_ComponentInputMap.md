# Class ComponentInputMap

**Source:** `java.desktop\javax\swing\ComponentInputMap.html`

### Class Description

```java
public class
ComponentInputMap

extends
InputMap
```

A

ComponentInputMap

is an

InputMap

associated with a particular

JComponent

.
The component is automatically notified whenever
the

ComponentInputMap

changes.

ComponentInputMap

s are used for

WHEN_IN_FOCUSED_WINDOW

bindings.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ComponentInputMap​(
JComponent
component)

Creates a

ComponentInputMap

associated with the
specified component.

**Parameters:**
- component

- a non-null

JComponent

**Throws:**
- IllegalArgumentException

- if

component

is null

---

### Method Details

#### public void setParent​(
InputMap
map)

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

**Overrides:**
- setParent

in class

InputMap

**Parameters:**
- map

- a

ComponentInputMap

**Throws:**
- IllegalArgumentException

- if

map

is not a

ComponentInputMap

or is not associated with the same component

---

#### public
JComponent
getComponent()

Returns the component the

InputMap

was created for.

**Returns:**
- the component the

InputMap

was created for.

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

**Overrides:**
- put

in class

InputMap

**Parameters:**
- keyStroke

- a

KeyStroke
- actionMapKey

- an action map key

---

#### public void remove​(
KeyStroke
key)

Removes the binding for

key

from this object.

**Overrides:**
- remove

in class

InputMap

**Parameters:**
- key

- the

KeyStroke

for which to remove the binding

---

#### public void clear()

Removes all the mappings from this object.

**Overrides:**
- clear

in class

InputMap

---

### Additional Sections

#### Class ComponentInputMap

java.lang.Object

- javax.swing.InputMap
- - javax.swing.ComponentInputMap

javax.swing.InputMap

- javax.swing.ComponentInputMap

javax.swing.ComponentInputMap

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ComponentInputMapUIResource

```java
public class
ComponentInputMap

extends
InputMap
```

A

ComponentInputMap

is an

InputMap

associated with a particular

JComponent

.
The component is automatically notified whenever
the

ComponentInputMap

changes.

ComponentInputMap

s are used for

WHEN_IN_FOCUSED_WINDOW

bindings.

**Since:** 1.3
**See Also:** Serialized Form

public class

ComponentInputMap

extends

InputMap

A

ComponentInputMap

is an

InputMap

associated with a particular

JComponent

.
The component is automatically notified whenever
the

ComponentInputMap

changes.

ComponentInputMap

s are used for

WHEN_IN_FOCUSED_WINDOW

bindings.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ComponentInputMap

​(

JComponent

component)

Creates a

ComponentInputMap

associated with the
specified component.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Removes all the mappings from this object.

JComponent

getComponent

()

Returns the component the

InputMap

was created for.

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

from this object.

void

setParent

​(

InputMap

map)

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

- Methods declared in class javax.swing.

InputMap

allKeys

,

get

,

getParent

,

keys

,

size

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

ComponentInputMap

​(

JComponent

component)

Creates a

ComponentInputMap

associated with the
specified component.

---

#### Constructor Summary

Creates a

ComponentInputMap

associated with the
specified component.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Removes all the mappings from this object.

JComponent

getComponent

()

Returns the component the

InputMap

was created for.

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

from this object.

void

setParent

​(

InputMap

map)

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

- Methods declared in class javax.swing.

InputMap

allKeys

,

get

,

getParent

,

keys

,

size

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

Removes all the mappings from this object.

Returns the component the

InputMap

was created for.

Adds a binding for

keyStroke

to

actionMapKey

.

Removes the binding for

key

from this object.

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

Methods declared in class javax.swing.

InputMap

allKeys

,

get

,

getParent

,

keys

,

size

---

#### Methods declared in class javax.swing. InputMap

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

- ComponentInputMap

```java
public ComponentInputMap​(
JComponent
component)
```

Creates a

ComponentInputMap

associated with the
specified component.

**Parameters:** component

- a non-null

JComponent
**Throws:** IllegalArgumentException

- if

component

is null

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
InputMap
map)
```

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

**Overrides:** setParent

in class

InputMap
**Parameters:** map

- a

ComponentInputMap
**Throws:** IllegalArgumentException

- if

map

is not a

ComponentInputMap

or is not associated with the same component

- getComponent

```java
public
JComponent
getComponent()
```

Returns the component the

InputMap

was created for.

**Returns:** the component the

InputMap

was created for.

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

**Overrides:** put

in class

InputMap
**Parameters:** keyStroke

- a

KeyStroke
**Parameters:** actionMapKey

- an action map key

- remove

```java
public void remove​(
KeyStroke
key)
```

Removes the binding for

key

from this object.

**Overrides:** remove

in class

InputMap
**Parameters:** key

- the

KeyStroke

for which to remove the binding

- clear

```java
public void clear()
```

Removes all the mappings from this object.

**Overrides:** clear

in class

InputMap

Constructor Detail

- ComponentInputMap

```java
public ComponentInputMap​(
JComponent
component)
```

Creates a

ComponentInputMap

associated with the
specified component.

**Parameters:** component

- a non-null

JComponent
**Throws:** IllegalArgumentException

- if

component

is null

---

#### Constructor Detail

ComponentInputMap

```java
public ComponentInputMap​(
JComponent
component)
```

Creates a

ComponentInputMap

associated with the
specified component.

**Parameters:** component

- a non-null

JComponent
**Throws:** IllegalArgumentException

- if

component

is null

---

#### ComponentInputMap

public ComponentInputMap​(

JComponent

component)

Creates a

ComponentInputMap

associated with the
specified component.

Method Detail

- setParent

```java
public void setParent​(
InputMap
map)
```

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

**Overrides:** setParent

in class

InputMap
**Parameters:** map

- a

ComponentInputMap
**Throws:** IllegalArgumentException

- if

map

is not a

ComponentInputMap

or is not associated with the same component

- getComponent

```java
public
JComponent
getComponent()
```

Returns the component the

InputMap

was created for.

**Returns:** the component the

InputMap

was created for.

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

**Overrides:** put

in class

InputMap
**Parameters:** keyStroke

- a

KeyStroke
**Parameters:** actionMapKey

- an action map key

- remove

```java
public void remove​(
KeyStroke
key)
```

Removes the binding for

key

from this object.

**Overrides:** remove

in class

InputMap
**Parameters:** key

- the

KeyStroke

for which to remove the binding

- clear

```java
public void clear()
```

Removes all the mappings from this object.

**Overrides:** clear

in class

InputMap

---

#### Method Detail

setParent

```java
public void setParent​(
InputMap
map)
```

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

**Overrides:** setParent

in class

InputMap
**Parameters:** map

- a

ComponentInputMap
**Throws:** IllegalArgumentException

- if

map

is not a

ComponentInputMap

or is not associated with the same component

---

#### setParent

public void setParent​(

InputMap

map)

Sets the parent, which must be a

ComponentInputMap

associated with the same component as this

ComponentInputMap

.

getComponent

```java
public
JComponent
getComponent()
```

Returns the component the

InputMap

was created for.

**Returns:** the component the

InputMap

was created for.

---

#### getComponent

public

JComponent

getComponent()

Returns the component the

InputMap

was created for.

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

**Overrides:** put

in class

InputMap
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

remove

```java
public void remove​(
KeyStroke
key)
```

Removes the binding for

key

from this object.

**Overrides:** remove

in class

InputMap
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

from this object.

clear

```java
public void clear()
```

Removes all the mappings from this object.

**Overrides:** clear

in class

InputMap

---

#### clear

public void clear()

Removes all the mappings from this object.

---

