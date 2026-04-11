# Class DnDConstants

**Source:** `java.desktop\java\awt\dnd\DnDConstants.html`

### Class Description

```java
public final class
DnDConstants

extends
Object
```

This class contains constant values representing
the type of action(s) to be performed by a Drag and Drop operation.

**Since:** 1.2

---

### Field Details

#### @Native

public static final int ACTION_NONE

An

int

representing no action.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int ACTION_COPY

An

int

representing a "copy" action.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int ACTION_MOVE

An

int

representing a "move" action.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int ACTION_COPY_OR_MOVE

An

int

representing a "copy" or
"move" action.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int ACTION_LINK

An

int

representing a "link" action.

The link verb is found in many, if not all native DnD platforms, and the
actual interpretation of LINK semantics is both platform
and application dependent. Broadly speaking, the
semantic is "do not copy, or move the operand, but create a reference
to it". Defining the meaning of "reference" is where ambiguity is
introduced.

The verb is provided for completeness, but its use is not recommended
for DnD operations between logically distinct applications where
misinterpretation of the operations semantics could lead to confusing
results for the user.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int ACTION_REFERENCE

An

int

representing a "reference"
action (synonym for ACTION_LINK).

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class DnDConstants

java.lang.Object

- java.awt.dnd.DnDConstants

java.awt.dnd.DnDConstants

```java
public final class
DnDConstants

extends
Object
```

This class contains constant values representing
the type of action(s) to be performed by a Drag and Drop operation.

**Since:** 1.2

public final class

DnDConstants

extends

Object

This class contains constant values representing
the type of action(s) to be performed by a Drag and Drop operation.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTION_COPY

An

int

representing a "copy" action.

static int

ACTION_COPY_OR_MOVE

An

int

representing a "copy" or
"move" action.

static int

ACTION_LINK

An

int

representing a "link" action.

static int

ACTION_MOVE

An

int

representing a "move" action.

static int

ACTION_NONE

An

int

representing no action.

static int

ACTION_REFERENCE

An

int

representing a "reference"
action (synonym for ACTION_LINK).

========== METHOD SUMMARY ===========

- Method Summary

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTION_COPY

An

int

representing a "copy" action.

static int

ACTION_COPY_OR_MOVE

An

int

representing a "copy" or
"move" action.

static int

ACTION_LINK

An

int

representing a "link" action.

static int

ACTION_MOVE

An

int

representing a "move" action.

static int

ACTION_NONE

An

int

representing no action.

static int

ACTION_REFERENCE

An

int

representing a "reference"
action (synonym for ACTION_LINK).

---

#### Field Summary

An

int

representing a "copy" action.

An

int

representing a "copy" or
"move" action.

An

int

representing a "link" action.

An

int

representing a "move" action.

An

int

representing no action.

An

int

representing a "reference"
action (synonym for ACTION_LINK).

Method Summary

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

============ FIELD DETAIL ===========

- Field Detail

- ACTION_NONE

```java
@Native

public static final int ACTION_NONE
```

An

int

representing no action.

**See Also:** Constant Field Values

- ACTION_COPY

```java
@Native

public static final int ACTION_COPY
```

An

int

representing a "copy" action.

**See Also:** Constant Field Values

- ACTION_MOVE

```java
@Native

public static final int ACTION_MOVE
```

An

int

representing a "move" action.

**See Also:** Constant Field Values

- ACTION_COPY_OR_MOVE

```java
@Native

public static final int ACTION_COPY_OR_MOVE
```

An

int

representing a "copy" or
"move" action.

**See Also:** Constant Field Values

- ACTION_LINK

```java
@Native

public static final int ACTION_LINK
```

An

int

representing a "link" action.

The link verb is found in many, if not all native DnD platforms, and the
actual interpretation of LINK semantics is both platform
and application dependent. Broadly speaking, the
semantic is "do not copy, or move the operand, but create a reference
to it". Defining the meaning of "reference" is where ambiguity is
introduced.

The verb is provided for completeness, but its use is not recommended
for DnD operations between logically distinct applications where
misinterpretation of the operations semantics could lead to confusing
results for the user.

**See Also:** Constant Field Values

- ACTION_REFERENCE

```java
@Native

public static final int ACTION_REFERENCE
```

An

int

representing a "reference"
action (synonym for ACTION_LINK).

**See Also:** Constant Field Values

Field Detail

- ACTION_NONE

```java
@Native

public static final int ACTION_NONE
```

An

int

representing no action.

**See Also:** Constant Field Values

- ACTION_COPY

```java
@Native

public static final int ACTION_COPY
```

An

int

representing a "copy" action.

**See Also:** Constant Field Values

- ACTION_MOVE

```java
@Native

public static final int ACTION_MOVE
```

An

int

representing a "move" action.

**See Also:** Constant Field Values

- ACTION_COPY_OR_MOVE

```java
@Native

public static final int ACTION_COPY_OR_MOVE
```

An

int

representing a "copy" or
"move" action.

**See Also:** Constant Field Values

- ACTION_LINK

```java
@Native

public static final int ACTION_LINK
```

An

int

representing a "link" action.

The link verb is found in many, if not all native DnD platforms, and the
actual interpretation of LINK semantics is both platform
and application dependent. Broadly speaking, the
semantic is "do not copy, or move the operand, but create a reference
to it". Defining the meaning of "reference" is where ambiguity is
introduced.

The verb is provided for completeness, but its use is not recommended
for DnD operations between logically distinct applications where
misinterpretation of the operations semantics could lead to confusing
results for the user.

**See Also:** Constant Field Values

- ACTION_REFERENCE

```java
@Native

public static final int ACTION_REFERENCE
```

An

int

representing a "reference"
action (synonym for ACTION_LINK).

**See Also:** Constant Field Values

---

#### Field Detail

ACTION_NONE

```java
@Native

public static final int ACTION_NONE
```

An

int

representing no action.

**See Also:** Constant Field Values

---

#### ACTION_NONE

@Native

public static final int ACTION_NONE

An

int

representing no action.

ACTION_COPY

```java
@Native

public static final int ACTION_COPY
```

An

int

representing a "copy" action.

**See Also:** Constant Field Values

---

#### ACTION_COPY

@Native

public static final int ACTION_COPY

An

int

representing a "copy" action.

ACTION_MOVE

```java
@Native

public static final int ACTION_MOVE
```

An

int

representing a "move" action.

**See Also:** Constant Field Values

---

#### ACTION_MOVE

@Native

public static final int ACTION_MOVE

An

int

representing a "move" action.

ACTION_COPY_OR_MOVE

```java
@Native

public static final int ACTION_COPY_OR_MOVE
```

An

int

representing a "copy" or
"move" action.

**See Also:** Constant Field Values

---

#### ACTION_COPY_OR_MOVE

@Native

public static final int ACTION_COPY_OR_MOVE

An

int

representing a "copy" or
"move" action.

ACTION_LINK

```java
@Native

public static final int ACTION_LINK
```

An

int

representing a "link" action.

The link verb is found in many, if not all native DnD platforms, and the
actual interpretation of LINK semantics is both platform
and application dependent. Broadly speaking, the
semantic is "do not copy, or move the operand, but create a reference
to it". Defining the meaning of "reference" is where ambiguity is
introduced.

The verb is provided for completeness, but its use is not recommended
for DnD operations between logically distinct applications where
misinterpretation of the operations semantics could lead to confusing
results for the user.

**See Also:** Constant Field Values

---

#### ACTION_LINK

@Native

public static final int ACTION_LINK

An

int

representing a "link" action.

The link verb is found in many, if not all native DnD platforms, and the
actual interpretation of LINK semantics is both platform
and application dependent. Broadly speaking, the
semantic is "do not copy, or move the operand, but create a reference
to it". Defining the meaning of "reference" is where ambiguity is
introduced.

The verb is provided for completeness, but its use is not recommended
for DnD operations between logically distinct applications where
misinterpretation of the operations semantics could lead to confusing
results for the user.

ACTION_REFERENCE

```java
@Native

public static final int ACTION_REFERENCE
```

An

int

representing a "reference"
action (synonym for ACTION_LINK).

**See Also:** Constant Field Values

---

#### ACTION_REFERENCE

@Native

public static final int ACTION_REFERENCE

An

int

representing a "reference"
action (synonym for ACTION_LINK).

---

