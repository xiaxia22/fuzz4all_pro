# Interface StyleSheetList

**Source:** `jdk.xml.dom\org\w3c\dom\stylesheets\StyleSheetList.html`

### Class Description

```java
public interface
StyleSheetList
```

The

StyleSheetList

interface provides the abstraction of an
ordered collection of style sheets.

The items in the

StyleSheetList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getLength()

The number of

StyleSheets

in the list. The range of valid
child stylesheet indices is

0

to

length-1

inclusive.

---

#### StyleSheet
item​(int index)

Used to retrieve a style sheet by ordinal index. If index is greater
than or equal to the number of style sheets in the list, this returns

null

.

**Parameters:**
- index

- Index into the collection

**Returns:**
- The style sheet at the

index

position in the

StyleSheetList

, or

null

if that is not a
valid index.

---

### Additional Sections

#### Interface StyleSheetList

```java
public interface
StyleSheetList
```

The

StyleSheetList

interface provides the abstraction of an
ordered collection of style sheets.

The items in the

StyleSheetList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

StyleSheetList

The

StyleSheetList

interface provides the abstraction of an
ordered collection of style sheets.

The items in the

StyleSheetList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The items in the

StyleSheetList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getLength

()

The number of

StyleSheets

in the list.

StyleSheet

item

​(int index)

Used to retrieve a style sheet by ordinal index.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getLength

()

The number of

StyleSheets

in the list.

StyleSheet

item

​(int index)

Used to retrieve a style sheet by ordinal index.

---

#### Method Summary

The number of

StyleSheets

in the list.

Used to retrieve a style sheet by ordinal index.

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
int getLength()
```

The number of

StyleSheets

in the list. The range of valid
child stylesheet indices is

0

to

length-1

inclusive.

- item

```java
StyleSheet
item​(int index)
```

Used to retrieve a style sheet by ordinal index. If index is greater
than or equal to the number of style sheets in the list, this returns

null

.

**Parameters:** index

- Index into the collection
**Returns:** The style sheet at the

index

position in the

StyleSheetList

, or

null

if that is not a
valid index.

Method Detail

- getLength

```java
int getLength()
```

The number of

StyleSheets

in the list. The range of valid
child stylesheet indices is

0

to

length-1

inclusive.

- item

```java
StyleSheet
item​(int index)
```

Used to retrieve a style sheet by ordinal index. If index is greater
than or equal to the number of style sheets in the list, this returns

null

.

**Parameters:** index

- Index into the collection
**Returns:** The style sheet at the

index

position in the

StyleSheetList

, or

null

if that is not a
valid index.

---

#### Method Detail

getLength

```java
int getLength()
```

The number of

StyleSheets

in the list. The range of valid
child stylesheet indices is

0

to

length-1

inclusive.

---

#### getLength

int getLength()

The number of

StyleSheets

in the list. The range of valid
child stylesheet indices is

0

to

length-1

inclusive.

item

```java
StyleSheet
item​(int index)
```

Used to retrieve a style sheet by ordinal index. If index is greater
than or equal to the number of style sheets in the list, this returns

null

.

**Parameters:** index

- Index into the collection
**Returns:** The style sheet at the

index

position in the

StyleSheetList

, or

null

if that is not a
valid index.

---

#### item

StyleSheet

item​(int index)

Used to retrieve a style sheet by ordinal index. If index is greater
than or equal to the number of style sheets in the list, this returns

null

.

---

