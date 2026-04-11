# Class AccessibleStateSet

**Source:** `java.desktop\javax\accessibility\AccessibleStateSet.html`

### Class Description

```java
public class
AccessibleStateSet

extends
Object
```

Class

AccessibleStateSet

determines a component's state set. The
state set of a component is a set of

AccessibleState

objects and
descriptions. E.G., The current overall state of the object, such as whether
it is enabled, has focus, etc.

**See Also:** AccessibleState

---

### Field Details

#### protected
Vector
<
AccessibleState
> states

Each entry in the

Vector

represents an

AccessibleState

.

**See Also:**
- add(javax.accessibility.AccessibleState)

,

addAll(javax.accessibility.AccessibleState[])

,

remove(javax.accessibility.AccessibleState)

,

contains(javax.accessibility.AccessibleState)

,

toArray()

,

clear()

---

### Constructor Details

#### public AccessibleStateSet()

Creates a new empty state set.

---

#### public AccessibleStateSet​(
AccessibleState
[] states)

Creates a new state with the initial set of states contained in the array
of states passed in. Duplicate entries are ignored.

**Parameters:**
- states

- an array of

AccessibleState

describing the state
set

---

### Method Details

#### public boolean add​(
AccessibleState
state)

Adds a new state to the current state set if it is not already present.
If the state is already in the state set, the state set is unchanged and
the return value is

false

. Otherwise, the state is added to the
state set and the return value is

true

.

**Parameters:**
- state

- the state to add to the state set

**Returns:**
- true

if state is added to the state set;

false

if
the state set is unchanged

---

#### public void addAll​(
AccessibleState
[] states)

Adds all of the states to the existing state set. Duplicate entries are
ignored.

**Parameters:**
- states

-

AccessibleState

array describing the state set

---

#### public boolean remove​(
AccessibleState
state)

Removes a state from the current state set. If the state is not in the
set, the state set will be unchanged and the return value will be

false

. If the state is in the state set, it will be removed from
the set and the return value will be

true

.

**Parameters:**
- state

- the state to remove from the state set

**Returns:**
- true

if the state is in the state set;

false

if
the state set will be unchanged

---

#### public void clear()

Removes all the states from the current state set.

---

#### public boolean contains​(
AccessibleState
state)

Checks if the current state is in the state set.

**Parameters:**
- state

- the state

**Returns:**
- true

if the state is in the state set; otherwise

false

---

#### public
AccessibleState
[] toArray()

Returns the current state set as an array of

AccessibleState

.

**Returns:**
- AccessibleState

array containing the current state

---

#### public
String
toString()

Creates a localized string representing all the states in the set using
the default locale.

**Overrides:**
- toString

in class

Object

**Returns:**
- comma separated localized string

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

### Additional Sections

#### Class AccessibleStateSet

java.lang.Object

- javax.accessibility.AccessibleStateSet

javax.accessibility.AccessibleStateSet

```java
public class
AccessibleStateSet

extends
Object
```

Class

AccessibleStateSet

determines a component's state set. The
state set of a component is a set of

AccessibleState

objects and
descriptions. E.G., The current overall state of the object, such as whether
it is enabled, has focus, etc.

**See Also:** AccessibleState

public class

AccessibleStateSet

extends

Object

Class

AccessibleStateSet

determines a component's state set. The
state set of a component is a set of

AccessibleState

objects and
descriptions. E.G., The current overall state of the object, such as whether
it is enabled, has focus, etc.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

AccessibleState

>

states

Each entry in the

Vector

represents an

AccessibleState

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleStateSet

()

Creates a new empty state set.

AccessibleStateSet

​(

AccessibleState

[] states)

Creates a new state with the initial set of states contained in the array
of states passed in.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

AccessibleState

state)

Adds a new state to the current state set if it is not already present.

void

addAll

​(

AccessibleState

[] states)

Adds all of the states to the existing state set.

void

clear

()

Removes all the states from the current state set.

boolean

contains

​(

AccessibleState

state)

Checks if the current state is in the state set.

boolean

remove

​(

AccessibleState

state)

Removes a state from the current state set.

AccessibleState

[]

toArray

()

Returns the current state set as an array of

AccessibleState

.

String

toString

()

Creates a localized string representing all the states in the set using
the default locale.

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

protected

Vector

<

AccessibleState

>

states

Each entry in the

Vector

represents an

AccessibleState

.

---

#### Field Summary

Each entry in the

Vector

represents an

AccessibleState

.

Constructor Summary

Constructors

Constructor

Description

AccessibleStateSet

()

Creates a new empty state set.

AccessibleStateSet

​(

AccessibleState

[] states)

Creates a new state with the initial set of states contained in the array
of states passed in.

---

#### Constructor Summary

Creates a new empty state set.

Creates a new state with the initial set of states contained in the array
of states passed in.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

AccessibleState

state)

Adds a new state to the current state set if it is not already present.

void

addAll

​(

AccessibleState

[] states)

Adds all of the states to the existing state set.

void

clear

()

Removes all the states from the current state set.

boolean

contains

​(

AccessibleState

state)

Checks if the current state is in the state set.

boolean

remove

​(

AccessibleState

state)

Removes a state from the current state set.

AccessibleState

[]

toArray

()

Returns the current state set as an array of

AccessibleState

.

String

toString

()

Creates a localized string representing all the states in the set using
the default locale.

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

Adds a new state to the current state set if it is not already present.

Adds all of the states to the existing state set.

Removes all the states from the current state set.

Checks if the current state is in the state set.

Removes a state from the current state set.

Returns the current state set as an array of

AccessibleState

.

Creates a localized string representing all the states in the set using
the default locale.

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

- states

```java
protected
Vector
<
AccessibleState
> states
```

Each entry in the

Vector

represents an

AccessibleState

.

**See Also:** add(javax.accessibility.AccessibleState)

,

addAll(javax.accessibility.AccessibleState[])

,

remove(javax.accessibility.AccessibleState)

,

contains(javax.accessibility.AccessibleState)

,

toArray()

,

clear()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleStateSet

```java
public AccessibleStateSet()
```

Creates a new empty state set.

- AccessibleStateSet

```java
public AccessibleStateSet​(
AccessibleState
[] states)
```

Creates a new state with the initial set of states contained in the array
of states passed in. Duplicate entries are ignored.

**Parameters:** states

- an array of

AccessibleState

describing the state
set

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public boolean add​(
AccessibleState
state)
```

Adds a new state to the current state set if it is not already present.
If the state is already in the state set, the state set is unchanged and
the return value is

false

. Otherwise, the state is added to the
state set and the return value is

true

.

**Parameters:** state

- the state to add to the state set
**Returns:** true

if state is added to the state set;

false

if
the state set is unchanged

- addAll

```java
public void addAll​(
AccessibleState
[] states)
```

Adds all of the states to the existing state set. Duplicate entries are
ignored.

**Parameters:** states

-

AccessibleState

array describing the state set

- remove

```java
public boolean remove​(
AccessibleState
state)
```

Removes a state from the current state set. If the state is not in the
set, the state set will be unchanged and the return value will be

false

. If the state is in the state set, it will be removed from
the set and the return value will be

true

.

**Parameters:** state

- the state to remove from the state set
**Returns:** true

if the state is in the state set;

false

if
the state set will be unchanged

- clear

```java
public void clear()
```

Removes all the states from the current state set.

- contains

```java
public boolean contains​(
AccessibleState
state)
```

Checks if the current state is in the state set.

**Parameters:** state

- the state
**Returns:** true

if the state is in the state set; otherwise

false

- toArray

```java
public
AccessibleState
[] toArray()
```

Returns the current state set as an array of

AccessibleState

.

**Returns:** AccessibleState

array containing the current state

- toString

```java
public
String
toString()
```

Creates a localized string representing all the states in the set using
the default locale.

**Overrides:** toString

in class

Object
**Returns:** comma separated localized string
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

Field Detail

- states

```java
protected
Vector
<
AccessibleState
> states
```

Each entry in the

Vector

represents an

AccessibleState

.

**See Also:** add(javax.accessibility.AccessibleState)

,

addAll(javax.accessibility.AccessibleState[])

,

remove(javax.accessibility.AccessibleState)

,

contains(javax.accessibility.AccessibleState)

,

toArray()

,

clear()

---

#### Field Detail

states

```java
protected
Vector
<
AccessibleState
> states
```

Each entry in the

Vector

represents an

AccessibleState

.

**See Also:** add(javax.accessibility.AccessibleState)

,

addAll(javax.accessibility.AccessibleState[])

,

remove(javax.accessibility.AccessibleState)

,

contains(javax.accessibility.AccessibleState)

,

toArray()

,

clear()

---

#### states

protected

Vector

<

AccessibleState

> states

Each entry in the

Vector

represents an

AccessibleState

.

Constructor Detail

- AccessibleStateSet

```java
public AccessibleStateSet()
```

Creates a new empty state set.

- AccessibleStateSet

```java
public AccessibleStateSet​(
AccessibleState
[] states)
```

Creates a new state with the initial set of states contained in the array
of states passed in. Duplicate entries are ignored.

**Parameters:** states

- an array of

AccessibleState

describing the state
set

---

#### Constructor Detail

AccessibleStateSet

```java
public AccessibleStateSet()
```

Creates a new empty state set.

---

#### AccessibleStateSet

public AccessibleStateSet()

Creates a new empty state set.

AccessibleStateSet

```java
public AccessibleStateSet​(
AccessibleState
[] states)
```

Creates a new state with the initial set of states contained in the array
of states passed in. Duplicate entries are ignored.

**Parameters:** states

- an array of

AccessibleState

describing the state
set

---

#### AccessibleStateSet

public AccessibleStateSet​(

AccessibleState

[] states)

Creates a new state with the initial set of states contained in the array
of states passed in. Duplicate entries are ignored.

Method Detail

- add

```java
public boolean add​(
AccessibleState
state)
```

Adds a new state to the current state set if it is not already present.
If the state is already in the state set, the state set is unchanged and
the return value is

false

. Otherwise, the state is added to the
state set and the return value is

true

.

**Parameters:** state

- the state to add to the state set
**Returns:** true

if state is added to the state set;

false

if
the state set is unchanged

- addAll

```java
public void addAll​(
AccessibleState
[] states)
```

Adds all of the states to the existing state set. Duplicate entries are
ignored.

**Parameters:** states

-

AccessibleState

array describing the state set

- remove

```java
public boolean remove​(
AccessibleState
state)
```

Removes a state from the current state set. If the state is not in the
set, the state set will be unchanged and the return value will be

false

. If the state is in the state set, it will be removed from
the set and the return value will be

true

.

**Parameters:** state

- the state to remove from the state set
**Returns:** true

if the state is in the state set;

false

if
the state set will be unchanged

- clear

```java
public void clear()
```

Removes all the states from the current state set.

- contains

```java
public boolean contains​(
AccessibleState
state)
```

Checks if the current state is in the state set.

**Parameters:** state

- the state
**Returns:** true

if the state is in the state set; otherwise

false

- toArray

```java
public
AccessibleState
[] toArray()
```

Returns the current state set as an array of

AccessibleState

.

**Returns:** AccessibleState

array containing the current state

- toString

```java
public
String
toString()
```

Creates a localized string representing all the states in the set using
the default locale.

**Overrides:** toString

in class

Object
**Returns:** comma separated localized string
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### Method Detail

add

```java
public boolean add​(
AccessibleState
state)
```

Adds a new state to the current state set if it is not already present.
If the state is already in the state set, the state set is unchanged and
the return value is

false

. Otherwise, the state is added to the
state set and the return value is

true

.

**Parameters:** state

- the state to add to the state set
**Returns:** true

if state is added to the state set;

false

if
the state set is unchanged

---

#### add

public boolean add​(

AccessibleState

state)

Adds a new state to the current state set if it is not already present.
If the state is already in the state set, the state set is unchanged and
the return value is

false

. Otherwise, the state is added to the
state set and the return value is

true

.

addAll

```java
public void addAll​(
AccessibleState
[] states)
```

Adds all of the states to the existing state set. Duplicate entries are
ignored.

**Parameters:** states

-

AccessibleState

array describing the state set

---

#### addAll

public void addAll​(

AccessibleState

[] states)

Adds all of the states to the existing state set. Duplicate entries are
ignored.

remove

```java
public boolean remove​(
AccessibleState
state)
```

Removes a state from the current state set. If the state is not in the
set, the state set will be unchanged and the return value will be

false

. If the state is in the state set, it will be removed from
the set and the return value will be

true

.

**Parameters:** state

- the state to remove from the state set
**Returns:** true

if the state is in the state set;

false

if
the state set will be unchanged

---

#### remove

public boolean remove​(

AccessibleState

state)

Removes a state from the current state set. If the state is not in the
set, the state set will be unchanged and the return value will be

false

. If the state is in the state set, it will be removed from
the set and the return value will be

true

.

clear

```java
public void clear()
```

Removes all the states from the current state set.

---

#### clear

public void clear()

Removes all the states from the current state set.

contains

```java
public boolean contains​(
AccessibleState
state)
```

Checks if the current state is in the state set.

**Parameters:** state

- the state
**Returns:** true

if the state is in the state set; otherwise

false

---

#### contains

public boolean contains​(

AccessibleState

state)

Checks if the current state is in the state set.

toArray

```java
public
AccessibleState
[] toArray()
```

Returns the current state set as an array of

AccessibleState

.

**Returns:** AccessibleState

array containing the current state

---

#### toArray

public

AccessibleState

[] toArray()

Returns the current state set as an array of

AccessibleState

.

toString

```java
public
String
toString()
```

Creates a localized string representing all the states in the set using
the default locale.

**Overrides:** toString

in class

Object
**Returns:** comma separated localized string
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### toString

public

String

toString()

Creates a localized string representing all the states in the set using
the default locale.

---

