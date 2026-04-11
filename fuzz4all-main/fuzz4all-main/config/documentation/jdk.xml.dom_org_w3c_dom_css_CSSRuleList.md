# Interface CSSRuleList

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSRuleList.html`

### Class Description

```java
public interface
CSSRuleList
```

The

CSSRuleList

interface provides the abstraction of an
ordered collection of CSS rules.

The items in the

CSSRuleList

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

CSSRules

in the list. The range of valid
child rule indices is

0

to

length-1

inclusive.

---

#### CSSRule
item​(int index)

Used to retrieve a CSS rule by ordinal index. The order in this
collection represents the order of the rules in the CSS style sheet.
If index is greater than or equal to the number of rules in the list,
this returns

null

.

**Parameters:**
- index

- Index into the collection

**Returns:**
- The style rule at the

index

position in the

CSSRuleList

, or

null

if that is not a
valid index.

---

### Additional Sections

#### Interface CSSRuleList

```java
public interface
CSSRuleList
```

The

CSSRuleList

interface provides the abstraction of an
ordered collection of CSS rules.

The items in the

CSSRuleList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSRuleList

The

CSSRuleList

interface provides the abstraction of an
ordered collection of CSS rules.

The items in the

CSSRuleList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The items in the

CSSRuleList

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

CSSRules

in the list.

CSSRule

item

​(int index)

Used to retrieve a CSS rule by ordinal index.

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

CSSRules

in the list.

CSSRule

item

​(int index)

Used to retrieve a CSS rule by ordinal index.

---

#### Method Summary

The number of

CSSRules

in the list.

Used to retrieve a CSS rule by ordinal index.

============ METHOD DETAIL ==========

- Method Detail

- getLength

```java
int getLength()
```

The number of

CSSRules

in the list. The range of valid
child rule indices is

0

to

length-1

inclusive.

- item

```java
CSSRule
item​(int index)
```

Used to retrieve a CSS rule by ordinal index. The order in this
collection represents the order of the rules in the CSS style sheet.
If index is greater than or equal to the number of rules in the list,
this returns

null

.

**Parameters:** index

- Index into the collection
**Returns:** The style rule at the

index

position in the

CSSRuleList

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

CSSRules

in the list. The range of valid
child rule indices is

0

to

length-1

inclusive.

- item

```java
CSSRule
item​(int index)
```

Used to retrieve a CSS rule by ordinal index. The order in this
collection represents the order of the rules in the CSS style sheet.
If index is greater than or equal to the number of rules in the list,
this returns

null

.

**Parameters:** index

- Index into the collection
**Returns:** The style rule at the

index

position in the

CSSRuleList

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

CSSRules

in the list. The range of valid
child rule indices is

0

to

length-1

inclusive.

---

#### getLength

int getLength()

The number of

CSSRules

in the list. The range of valid
child rule indices is

0

to

length-1

inclusive.

item

```java
CSSRule
item​(int index)
```

Used to retrieve a CSS rule by ordinal index. The order in this
collection represents the order of the rules in the CSS style sheet.
If index is greater than or equal to the number of rules in the list,
this returns

null

.

**Parameters:** index

- Index into the collection
**Returns:** The style rule at the

index

position in the

CSSRuleList

, or

null

if that is not a
valid index.

---

#### item

CSSRule

item​(int index)

Used to retrieve a CSS rule by ordinal index. The order in this
collection represents the order of the rules in the CSS style sheet.
If index is greater than or equal to the number of rules in the list,
this returns

null

.

---

