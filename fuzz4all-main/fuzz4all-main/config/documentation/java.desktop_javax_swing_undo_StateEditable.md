# Interface StateEditable

**Source:** `java.desktop\javax\swing\undo\StateEditable.html`

### Class Description

```java
public interface
StateEditable
```

StateEditable defines the interface for objects that can have
their state undone/redone by a StateEdit.

**See Also:** StateEdit

---

### Field Details

#### static final
String
RCSID

Resource ID for this class.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void storeState​(
Hashtable
<
Object
,​
Object
> state)

Upon receiving this message the receiver should place any relevant
state into

state

.

**Parameters:**
- state

- Hashtable object to store the state

---

#### void restoreState​(
Hashtable
<?,​?> state)

Upon receiving this message the receiver should extract any relevant
state out of

state

.

**Parameters:**
- state

- Hashtable object to restore the state from it

---

### Additional Sections

#### Interface StateEditable

```java
public interface
StateEditable
```

StateEditable defines the interface for objects that can have
their state undone/redone by a StateEdit.

**See Also:** StateEdit

public interface

StateEditable

StateEditable defines the interface for objects that can have
their state undone/redone by a StateEdit.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

RCSID

Resource ID for this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

restoreState

​(

Hashtable

<?,​?> state)

Upon receiving this message the receiver should extract any relevant
state out of

state

.

void

storeState

​(

Hashtable

<

Object

,​

Object

> state)

Upon receiving this message the receiver should place any relevant
state into

state

.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

RCSID

Resource ID for this class.

---

#### Field Summary

Resource ID for this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

restoreState

​(

Hashtable

<?,​?> state)

Upon receiving this message the receiver should extract any relevant
state out of

state

.

void

storeState

​(

Hashtable

<

Object

,​

Object

> state)

Upon receiving this message the receiver should place any relevant
state into

state

.

---

#### Method Summary

Upon receiving this message the receiver should extract any relevant
state out of

state

.

Upon receiving this message the receiver should place any relevant
state into

state

.

============ FIELD DETAIL ===========

- Field Detail

- RCSID

```java
static final
String
RCSID
```

Resource ID for this class.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- storeState

```java
void storeState​(
Hashtable
<
Object
,​
Object
> state)
```

Upon receiving this message the receiver should place any relevant
state into

state

.

**Parameters:** state

- Hashtable object to store the state

- restoreState

```java
void restoreState​(
Hashtable
<?,​?> state)
```

Upon receiving this message the receiver should extract any relevant
state out of

state

.

**Parameters:** state

- Hashtable object to restore the state from it

Field Detail

- RCSID

```java
static final
String
RCSID
```

Resource ID for this class.

**See Also:** Constant Field Values

---

#### Field Detail

RCSID

```java
static final
String
RCSID
```

Resource ID for this class.

**See Also:** Constant Field Values

---

#### RCSID

static final

String

RCSID

Resource ID for this class.

Method Detail

- storeState

```java
void storeState​(
Hashtable
<
Object
,​
Object
> state)
```

Upon receiving this message the receiver should place any relevant
state into

state

.

**Parameters:** state

- Hashtable object to store the state

- restoreState

```java
void restoreState​(
Hashtable
<?,​?> state)
```

Upon receiving this message the receiver should extract any relevant
state out of

state

.

**Parameters:** state

- Hashtable object to restore the state from it

---

#### Method Detail

storeState

```java
void storeState​(
Hashtable
<
Object
,​
Object
> state)
```

Upon receiving this message the receiver should place any relevant
state into

state

.

**Parameters:** state

- Hashtable object to store the state

---

#### storeState

void storeState​(

Hashtable

<

Object

,​

Object

> state)

Upon receiving this message the receiver should place any relevant
state into

state

.

restoreState

```java
void restoreState​(
Hashtable
<?,​?> state)
```

Upon receiving this message the receiver should extract any relevant
state out of

state

.

**Parameters:** state

- Hashtable object to restore the state from it

---

#### restoreState

void restoreState​(

Hashtable

<?,​?> state)

Upon receiving this message the receiver should extract any relevant
state out of

state

.

---

