# Enum DropMode

**Source:** `java.desktop\javax\swing\DropMode.html`

### Class Description

```java
public enum
DropMode

extends
Enum
<
DropMode
>
```

Drop modes, used to determine the method by which a component
tracks and indicates a drop location during drag and drop.

**All Implemented Interfaces:** Serializable

,

Comparable

<

DropMode

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
DropMode
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DropMode c : DropMode.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
DropMode
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum DropMode

java.lang.Object

- java.lang.Enum

<

DropMode

>
- - javax.swing.DropMode

java.lang.Enum

<

DropMode

>

- javax.swing.DropMode

javax.swing.DropMode

**All Implemented Interfaces:** Serializable

,

Comparable

<

DropMode

>

```java
public enum
DropMode

extends
Enum
<
DropMode
>
```

Drop modes, used to determine the method by which a component
tracks and indicates a drop location during drag and drop.

**Since:** 1.6
**See Also:** JTable.setDropMode(javax.swing.DropMode)

,

JList.setDropMode(javax.swing.DropMode)

,

JTree.setDropMode(javax.swing.DropMode)

,

JTextComponent.setDropMode(javax.swing.DropMode)

public enum

DropMode

extends

Enum

<

DropMode

>

Drop modes, used to determine the method by which a component
tracks and indicates a drop location during drag and drop.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

INSERT

The drop location should be tracked in terms of the position
where new data should be inserted.

INSERT_COLS

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data.

INSERT_ROWS

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data.

ON

The drop location should be tracked in terms of the index of
existing items.

ON_OR_INSERT

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

ON_OR_INSERT_COLS

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

ON_OR_INSERT_ROWS

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

USE_SELECTION

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

DropMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DropMode

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

INSERT

The drop location should be tracked in terms of the position
where new data should be inserted.

INSERT_COLS

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data.

INSERT_ROWS

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data.

ON

The drop location should be tracked in terms of the index of
existing items.

ON_OR_INSERT

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

ON_OR_INSERT_COLS

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

ON_OR_INSERT_ROWS

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

USE_SELECTION

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

---

#### Enum Constant Summary

The drop location should be tracked in terms of the position
where new data should be inserted.

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data.

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data.

The drop location should be tracked in terms of the index of
existing items.

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

DropMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DropMode

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- USE_SELECTION

```java
public static final
DropMode
USE_SELECTION
```

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

- ON

```java
public static final
DropMode
ON
```

The drop location should be tracked in terms of the index of
existing items. Useful for dropping on items in tables, lists,
and trees.

- INSERT

```java
public static final
DropMode
INSERT
```

The drop location should be tracked in terms of the position
where new data should be inserted. For components that manage
a list of items (list and tree for example), the drop location
should indicate the index where new data should be inserted.
For text components the location should represent a position
between characters. For components that manage tabular data
(table for example), the drop location should indicate
where to insert new rows, columns, or both, to accommodate
the dropped data.

- INSERT_ROWS

```java
public static final
DropMode
INSERT_ROWS
```

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

- INSERT_COLS

```java
public static final
DropMode
INSERT_COLS
```

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

- ON_OR_INSERT

```java
public static final
DropMode
ON_OR_INSERT
```

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

- ON_OR_INSERT_ROWS

```java
public static final
DropMode
ON_OR_INSERT_ROWS
```

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

- ON_OR_INSERT_COLS

```java
public static final
DropMode
ON_OR_INSERT_COLS
```

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
DropMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DropMode c : DropMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DropMode
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- USE_SELECTION

```java
public static final
DropMode
USE_SELECTION
```

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

- ON

```java
public static final
DropMode
ON
```

The drop location should be tracked in terms of the index of
existing items. Useful for dropping on items in tables, lists,
and trees.

- INSERT

```java
public static final
DropMode
INSERT
```

The drop location should be tracked in terms of the position
where new data should be inserted. For components that manage
a list of items (list and tree for example), the drop location
should indicate the index where new data should be inserted.
For text components the location should represent a position
between characters. For components that manage tabular data
(table for example), the drop location should indicate
where to insert new rows, columns, or both, to accommodate
the dropped data.

- INSERT_ROWS

```java
public static final
DropMode
INSERT_ROWS
```

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

- INSERT_COLS

```java
public static final
DropMode
INSERT_COLS
```

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

- ON_OR_INSERT

```java
public static final
DropMode
ON_OR_INSERT
```

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

- ON_OR_INSERT_ROWS

```java
public static final
DropMode
ON_OR_INSERT_ROWS
```

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

- ON_OR_INSERT_COLS

```java
public static final
DropMode
ON_OR_INSERT_COLS
```

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

---

#### Enum Constant Detail

USE_SELECTION

```java
public static final
DropMode
USE_SELECTION
```

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

---

#### USE_SELECTION

public static final

DropMode

USE_SELECTION

A component's own internal selection mechanism (or caret for text
components) should be used to track the drop location.

ON

```java
public static final
DropMode
ON
```

The drop location should be tracked in terms of the index of
existing items. Useful for dropping on items in tables, lists,
and trees.

---

#### ON

public static final

DropMode

ON

The drop location should be tracked in terms of the index of
existing items. Useful for dropping on items in tables, lists,
and trees.

INSERT

```java
public static final
DropMode
INSERT
```

The drop location should be tracked in terms of the position
where new data should be inserted. For components that manage
a list of items (list and tree for example), the drop location
should indicate the index where new data should be inserted.
For text components the location should represent a position
between characters. For components that manage tabular data
(table for example), the drop location should indicate
where to insert new rows, columns, or both, to accommodate
the dropped data.

---

#### INSERT

public static final

DropMode

INSERT

The drop location should be tracked in terms of the position
where new data should be inserted. For components that manage
a list of items (list and tree for example), the drop location
should indicate the index where new data should be inserted.
For text components the location should represent a position
between characters. For components that manage tabular data
(table for example), the drop location should indicate
where to insert new rows, columns, or both, to accommodate
the dropped data.

INSERT_ROWS

```java
public static final
DropMode
INSERT_ROWS
```

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

---

#### INSERT_ROWS

public static final

DropMode

INSERT_ROWS

The drop location should be tracked in terms of the row index
where new rows should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

INSERT_COLS

```java
public static final
DropMode
INSERT_COLS
```

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

---

#### INSERT_COLS

public static final

DropMode

INSERT_COLS

The drop location should be tracked in terms of the column index
where new columns should be inserted to accommodate the dropped
data. This is useful for components that manage tabular data.

ON_OR_INSERT

```java
public static final
DropMode
ON_OR_INSERT
```

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

---

#### ON_OR_INSERT

public static final

DropMode

ON_OR_INSERT

This mode is a combination of

ON

and

INSERT

, specifying that data can be
dropped on existing items, or in insert locations
as specified by

INSERT

.

ON_OR_INSERT_ROWS

```java
public static final
DropMode
ON_OR_INSERT_ROWS
```

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

---

#### ON_OR_INSERT_ROWS

public static final

DropMode

ON_OR_INSERT_ROWS

This mode is a combination of

ON

and

INSERT_ROWS

, specifying that data can be
dropped on existing items, or as insert rows
as specified by

INSERT_ROWS

.

ON_OR_INSERT_COLS

```java
public static final
DropMode
ON_OR_INSERT_COLS
```

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

---

#### ON_OR_INSERT_COLS

public static final

DropMode

ON_OR_INSERT_COLS

This mode is a combination of

ON

and

INSERT_COLS

, specifying that data can be
dropped on existing items, or as insert columns
as specified by

INSERT_COLS

.

Method Detail

- values

```java
public static
DropMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DropMode c : DropMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DropMode
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
DropMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DropMode c : DropMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

DropMode

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DropMode c : DropMode.values())
System.out.println(c);
```

for (DropMode c : DropMode.values())
System.out.println(c);

valueOf

```java
public static
DropMode
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

DropMode

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

