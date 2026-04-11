# Class CollationElementIterator

**Source:** `java.base\java\text\CollationElementIterator.html`

### Class Description

```java
public final class
CollationElementIterator

extends
Object
```

The

CollationElementIterator

class is used as an iterator
to walk through each character of an international string. Use the iterator
to return the ordering priority of the positioned character. The ordering
priority of a character, which we refer to as a key, defines how a character
is collated in the given collation object.

For example, consider the following in Spanish:

```java
"ca" → the first key is key('c') and second key is key('a').
"cha" → the first key is key('ch') and second key is key('a').
```

And in German,

```java
"äb" → the first key is key('a'), the second key is key('e'), and
the third key is key('b').
```

The key of a character is an integer composed of primary order(short),
secondary order(byte), and tertiary order(byte). Java strictly defines
the size and signedness of its primitive data types. Therefore, the static
functions

primaryOrder

,

secondaryOrder

, and

tertiaryOrder

return

int

,

short

,
and

short

respectively to ensure the correctness of the key
value.

Example of the iterator usage,

```java
String testString = "This is a test";
Collator col = Collator.getInstance();
if (col instanceof RuleBasedCollator) {
RuleBasedCollator ruleBasedCollator = (RuleBasedCollator)col;
CollationElementIterator collationElementIterator = ruleBasedCollator.getCollationElementIterator(testString);
int primaryOrder = CollationElementIterator.primaryOrder(collationElementIterator.next());
:
}
```

CollationElementIterator.next

returns the collation order
of the next character. A collation order consists of primary order,
secondary order and tertiary order. The data type of the collation
order is

int

. The first 16 bits of a collation order
is its primary order; the next 8 bits is the secondary order and the
last 8 bits is the tertiary order.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

**Since:** 1.1
**See Also:** Collator

,

RuleBasedCollator

---

### Field Details

#### public static final int NULLORDER

Null order which indicates the end of string is reached by the
cursor.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public void reset()

Resets the cursor to the beginning of the string. The next call
to next() will return the first collation element in the string.

---

#### public int next()

Get the next collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the next character in the
string".

This function returns the collation element that the iterator is currently
pointing to and then updates the internal pointer to point to the next element.
previous() updates the pointer first and then returns the element. This
means that when you change direction while iterating (i.e., call next() and
then call previous(), or call previous() and then call next()), you'll get
back the same element twice.

**Returns:**
- the next collation element

---

#### public int previous()

Get the previous collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the previous character in the
string".

This function updates the iterator's internal pointer to point to the
collation element preceding the one it's currently pointing to and then
returns that element, while next() returns the current element and then
updates the pointer. This means that when you change direction while
iterating (i.e., call next() and then call previous(), or call previous()
and then call next()), you'll get back the same element twice.

**Returns:**
- the previous collation element

**Since:**
- 1.2

---

#### public static final int primaryOrder​(int order)

Return the primary component of a collation element.

**Parameters:**
- order

- the collation element

**Returns:**
- the element's primary component

---

#### public static final short secondaryOrder​(int order)

Return the secondary component of a collation element.

**Parameters:**
- order

- the collation element

**Returns:**
- the element's secondary component

---

#### public static final short tertiaryOrder​(int order)

Return the tertiary component of a collation element.

**Parameters:**
- order

- the collation element

**Returns:**
- the element's tertiary component

---

#### public void setOffset​(int newOffset)

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements). The value returned by the next call to next()
will be the collation element corresponding to the specified position
in the text. If that position is in the middle of a contracting
character sequence, the result of the next call to next() is the
collation element for that sequence. This means that getOffset()
is not guaranteed to return the same value as was passed to a preceding
call to setOffset().

**Parameters:**
- newOffset

- The new character offset into the original text.

**Since:**
- 1.2

---

#### public int getOffset()

Returns the character offset in the original text corresponding to the next
collation element. (That is, getOffset() returns the position in the text
corresponding to the collation element that will be returned by the next
call to next().) This value will always be the index of the FIRST character
corresponding to the collation element (a contracting character sequence is
when two or more characters all correspond to the same collation element).
This means if you do setOffset(x) followed immediately by getOffset(), getOffset()
won't necessarily return x.

**Returns:**
- The character offset in the original text corresponding to the collation
element that will be returned by the next call to next().

**Since:**
- 1.2

---

#### public int getMaxExpansion​(int order)

Return the maximum length of any expansion sequences that end
with the specified comparison order.

**Parameters:**
- order

- a collation order returned by previous or next.

**Returns:**
- the maximum length of any expansion sequences ending
with the specified order.

**Since:**
- 1.2

---

#### public void setText​(
String
source)

Set a new string over which to iterate.

**Parameters:**
- source

- the new source text

**Since:**
- 1.2

---

#### public void setText​(
CharacterIterator
source)

Set a new string over which to iterate.

**Parameters:**
- source

- the new source text.

**Since:**
- 1.2

---

### Additional Sections

#### Class CollationElementIterator

java.lang.Object

- java.text.CollationElementIterator

java.text.CollationElementIterator

```java
public final class
CollationElementIterator

extends
Object
```

The

CollationElementIterator

class is used as an iterator
to walk through each character of an international string. Use the iterator
to return the ordering priority of the positioned character. The ordering
priority of a character, which we refer to as a key, defines how a character
is collated in the given collation object.

For example, consider the following in Spanish:

```java
"ca" → the first key is key('c') and second key is key('a').
"cha" → the first key is key('ch') and second key is key('a').
```

And in German,

```java
"äb" → the first key is key('a'), the second key is key('e'), and
the third key is key('b').
```

The key of a character is an integer composed of primary order(short),
secondary order(byte), and tertiary order(byte). Java strictly defines
the size and signedness of its primitive data types. Therefore, the static
functions

primaryOrder

,

secondaryOrder

, and

tertiaryOrder

return

int

,

short

,
and

short

respectively to ensure the correctness of the key
value.

Example of the iterator usage,

```java
String testString = "This is a test";
Collator col = Collator.getInstance();
if (col instanceof RuleBasedCollator) {
RuleBasedCollator ruleBasedCollator = (RuleBasedCollator)col;
CollationElementIterator collationElementIterator = ruleBasedCollator.getCollationElementIterator(testString);
int primaryOrder = CollationElementIterator.primaryOrder(collationElementIterator.next());
:
}
```

CollationElementIterator.next

returns the collation order
of the next character. A collation order consists of primary order,
secondary order and tertiary order. The data type of the collation
order is

int

. The first 16 bits of a collation order
is its primary order; the next 8 bits is the secondary order and the
last 8 bits is the tertiary order.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

**Since:** 1.1
**See Also:** Collator

,

RuleBasedCollator

public final class

CollationElementIterator

extends

Object

The

CollationElementIterator

class is used as an iterator
to walk through each character of an international string. Use the iterator
to return the ordering priority of the positioned character. The ordering
priority of a character, which we refer to as a key, defines how a character
is collated in the given collation object.

For example, consider the following in Spanish:

```java
"ca" → the first key is key('c') and second key is key('a').
"cha" → the first key is key('ch') and second key is key('a').
```

And in German,

```java
"äb" → the first key is key('a'), the second key is key('e'), and
the third key is key('b').
```

The key of a character is an integer composed of primary order(short),
secondary order(byte), and tertiary order(byte). Java strictly defines
the size and signedness of its primitive data types. Therefore, the static
functions

primaryOrder

,

secondaryOrder

, and

tertiaryOrder

return

int

,

short

,
and

short

respectively to ensure the correctness of the key
value.

Example of the iterator usage,

```java
String testString = "This is a test";
Collator col = Collator.getInstance();
if (col instanceof RuleBasedCollator) {
RuleBasedCollator ruleBasedCollator = (RuleBasedCollator)col;
CollationElementIterator collationElementIterator = ruleBasedCollator.getCollationElementIterator(testString);
int primaryOrder = CollationElementIterator.primaryOrder(collationElementIterator.next());
:
}
```

CollationElementIterator.next

returns the collation order
of the next character. A collation order consists of primary order,
secondary order and tertiary order. The data type of the collation
order is

int

. The first 16 bits of a collation order
is its primary order; the next 8 bits is the secondary order and the
last 8 bits is the tertiary order.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

For example, consider the following in Spanish:

```java
"ca" → the first key is key('c') and second key is key('a').
"cha" → the first key is key('ch') and second key is key('a').
```

And in German,

```java
"äb" → the first key is key('a'), the second key is key('e'), and
the third key is key('b').
```

The key of a character is an integer composed of primary order(short),
secondary order(byte), and tertiary order(byte). Java strictly defines
the size and signedness of its primitive data types. Therefore, the static
functions

primaryOrder

,

secondaryOrder

, and

tertiaryOrder

return

int

,

short

,
and

short

respectively to ensure the correctness of the key
value.

Example of the iterator usage,

```java
String testString = "This is a test";
Collator col = Collator.getInstance();
if (col instanceof RuleBasedCollator) {
RuleBasedCollator ruleBasedCollator = (RuleBasedCollator)col;
CollationElementIterator collationElementIterator = ruleBasedCollator.getCollationElementIterator(testString);
int primaryOrder = CollationElementIterator.primaryOrder(collationElementIterator.next());
:
}
```

CollationElementIterator.next

returns the collation order
of the next character. A collation order consists of primary order,
secondary order and tertiary order. The data type of the collation
order is

int

. The first 16 bits of a collation order
is its primary order; the next 8 bits is the secondary order and the
last 8 bits is the tertiary order.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

"ca" → the first key is key('c') and second key is key('a').
"cha" → the first key is key('ch') and second key is key('a').

"äb" → the first key is key('a'), the second key is key('e'), and
the third key is key('b').

Example of the iterator usage,

```java
String testString = "This is a test";
Collator col = Collator.getInstance();
if (col instanceof RuleBasedCollator) {
RuleBasedCollator ruleBasedCollator = (RuleBasedCollator)col;
CollationElementIterator collationElementIterator = ruleBasedCollator.getCollationElementIterator(testString);
int primaryOrder = CollationElementIterator.primaryOrder(collationElementIterator.next());
:
}
```

CollationElementIterator.next

returns the collation order
of the next character. A collation order consists of primary order,
secondary order and tertiary order. The data type of the collation
order is

int

. The first 16 bits of a collation order
is its primary order; the next 8 bits is the secondary order and the
last 8 bits is the tertiary order.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

String testString = "This is a test";
Collator col = Collator.getInstance();
if (col instanceof RuleBasedCollator) {
RuleBasedCollator ruleBasedCollator = (RuleBasedCollator)col;
CollationElementIterator collationElementIterator = ruleBasedCollator.getCollationElementIterator(testString);
int primaryOrder = CollationElementIterator.primaryOrder(collationElementIterator.next());
:
}

CollationElementIterator.next

returns the collation order
of the next character. A collation order consists of primary order,
secondary order and tertiary order. The data type of the collation
order is

int

. The first 16 bits of a collation order
is its primary order; the next 8 bits is the secondary order and the
last 8 bits is the tertiary order.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

Note:

CollationElementIterator

is a part of

RuleBasedCollator

implementation. It is only usable
with

RuleBasedCollator

instances.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

NULLORDER

Null order which indicates the end of string is reached by the
cursor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getMaxExpansion

​(int order)

Return the maximum length of any expansion sequences that end
with the specified comparison order.

int

getOffset

()

Returns the character offset in the original text corresponding to the next
collation element.

int

next

()

Get the next collation element in the string.

int

previous

()

Get the previous collation element in the string.

static int

primaryOrder

​(int order)

Return the primary component of a collation element.

void

reset

()

Resets the cursor to the beginning of the string.

static short

secondaryOrder

​(int order)

Return the secondary component of a collation element.

void

setOffset

​(int newOffset)

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements).

void

setText

​(

String

source)

Set a new string over which to iterate.

void

setText

​(

CharacterIterator

source)

Set a new string over which to iterate.

static short

tertiaryOrder

​(int order)

Return the tertiary component of a collation element.

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

NULLORDER

Null order which indicates the end of string is reached by the
cursor.

---

#### Field Summary

Null order which indicates the end of string is reached by the
cursor.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getMaxExpansion

​(int order)

Return the maximum length of any expansion sequences that end
with the specified comparison order.

int

getOffset

()

Returns the character offset in the original text corresponding to the next
collation element.

int

next

()

Get the next collation element in the string.

int

previous

()

Get the previous collation element in the string.

static int

primaryOrder

​(int order)

Return the primary component of a collation element.

void

reset

()

Resets the cursor to the beginning of the string.

static short

secondaryOrder

​(int order)

Return the secondary component of a collation element.

void

setOffset

​(int newOffset)

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements).

void

setText

​(

String

source)

Set a new string over which to iterate.

void

setText

​(

CharacterIterator

source)

Set a new string over which to iterate.

static short

tertiaryOrder

​(int order)

Return the tertiary component of a collation element.

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

Return the maximum length of any expansion sequences that end
with the specified comparison order.

Returns the character offset in the original text corresponding to the next
collation element.

Get the next collation element in the string.

Get the previous collation element in the string.

Return the primary component of a collation element.

Resets the cursor to the beginning of the string.

Return the secondary component of a collation element.

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements).

Set a new string over which to iterate.

Return the tertiary component of a collation element.

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

- NULLORDER

```java
public static final int NULLORDER
```

Null order which indicates the end of string is reached by the
cursor.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- reset

```java
public void reset()
```

Resets the cursor to the beginning of the string. The next call
to next() will return the first collation element in the string.

- next

```java
public int next()
```

Get the next collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the next character in the
string".

This function returns the collation element that the iterator is currently
pointing to and then updates the internal pointer to point to the next element.
previous() updates the pointer first and then returns the element. This
means that when you change direction while iterating (i.e., call next() and
then call previous(), or call previous() and then call next()), you'll get
back the same element twice.

**Returns:** the next collation element

- previous

```java
public int previous()
```

Get the previous collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the previous character in the
string".

This function updates the iterator's internal pointer to point to the
collation element preceding the one it's currently pointing to and then
returns that element, while next() returns the current element and then
updates the pointer. This means that when you change direction while
iterating (i.e., call next() and then call previous(), or call previous()
and then call next()), you'll get back the same element twice.

**Returns:** the previous collation element
**Since:** 1.2

- primaryOrder

```java
public static final int primaryOrder​(int order)
```

Return the primary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's primary component

- secondaryOrder

```java
public static final short secondaryOrder​(int order)
```

Return the secondary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's secondary component

- tertiaryOrder

```java
public static final short tertiaryOrder​(int order)
```

Return the tertiary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's tertiary component

- setOffset

```java
public void setOffset​(int newOffset)
```

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements). The value returned by the next call to next()
will be the collation element corresponding to the specified position
in the text. If that position is in the middle of a contracting
character sequence, the result of the next call to next() is the
collation element for that sequence. This means that getOffset()
is not guaranteed to return the same value as was passed to a preceding
call to setOffset().

**Parameters:** newOffset

- The new character offset into the original text.
**Since:** 1.2

- getOffset

```java
public int getOffset()
```

Returns the character offset in the original text corresponding to the next
collation element. (That is, getOffset() returns the position in the text
corresponding to the collation element that will be returned by the next
call to next().) This value will always be the index of the FIRST character
corresponding to the collation element (a contracting character sequence is
when two or more characters all correspond to the same collation element).
This means if you do setOffset(x) followed immediately by getOffset(), getOffset()
won't necessarily return x.

**Returns:** The character offset in the original text corresponding to the collation
element that will be returned by the next call to next().
**Since:** 1.2

- getMaxExpansion

```java
public int getMaxExpansion​(int order)
```

Return the maximum length of any expansion sequences that end
with the specified comparison order.

**Parameters:** order

- a collation order returned by previous or next.
**Returns:** the maximum length of any expansion sequences ending
with the specified order.
**Since:** 1.2

- setText

```java
public void setText​(
String
source)
```

Set a new string over which to iterate.

**Parameters:** source

- the new source text
**Since:** 1.2

- setText

```java
public void setText​(
CharacterIterator
source)
```

Set a new string over which to iterate.

**Parameters:** source

- the new source text.
**Since:** 1.2

Field Detail

- NULLORDER

```java
public static final int NULLORDER
```

Null order which indicates the end of string is reached by the
cursor.

**See Also:** Constant Field Values

---

#### Field Detail

NULLORDER

```java
public static final int NULLORDER
```

Null order which indicates the end of string is reached by the
cursor.

**See Also:** Constant Field Values

---

#### NULLORDER

public static final int NULLORDER

Null order which indicates the end of string is reached by the
cursor.

Method Detail

- reset

```java
public void reset()
```

Resets the cursor to the beginning of the string. The next call
to next() will return the first collation element in the string.

- next

```java
public int next()
```

Get the next collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the next character in the
string".

This function returns the collation element that the iterator is currently
pointing to and then updates the internal pointer to point to the next element.
previous() updates the pointer first and then returns the element. This
means that when you change direction while iterating (i.e., call next() and
then call previous(), or call previous() and then call next()), you'll get
back the same element twice.

**Returns:** the next collation element

- previous

```java
public int previous()
```

Get the previous collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the previous character in the
string".

This function updates the iterator's internal pointer to point to the
collation element preceding the one it's currently pointing to and then
returns that element, while next() returns the current element and then
updates the pointer. This means that when you change direction while
iterating (i.e., call next() and then call previous(), or call previous()
and then call next()), you'll get back the same element twice.

**Returns:** the previous collation element
**Since:** 1.2

- primaryOrder

```java
public static final int primaryOrder​(int order)
```

Return the primary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's primary component

- secondaryOrder

```java
public static final short secondaryOrder​(int order)
```

Return the secondary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's secondary component

- tertiaryOrder

```java
public static final short tertiaryOrder​(int order)
```

Return the tertiary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's tertiary component

- setOffset

```java
public void setOffset​(int newOffset)
```

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements). The value returned by the next call to next()
will be the collation element corresponding to the specified position
in the text. If that position is in the middle of a contracting
character sequence, the result of the next call to next() is the
collation element for that sequence. This means that getOffset()
is not guaranteed to return the same value as was passed to a preceding
call to setOffset().

**Parameters:** newOffset

- The new character offset into the original text.
**Since:** 1.2

- getOffset

```java
public int getOffset()
```

Returns the character offset in the original text corresponding to the next
collation element. (That is, getOffset() returns the position in the text
corresponding to the collation element that will be returned by the next
call to next().) This value will always be the index of the FIRST character
corresponding to the collation element (a contracting character sequence is
when two or more characters all correspond to the same collation element).
This means if you do setOffset(x) followed immediately by getOffset(), getOffset()
won't necessarily return x.

**Returns:** The character offset in the original text corresponding to the collation
element that will be returned by the next call to next().
**Since:** 1.2

- getMaxExpansion

```java
public int getMaxExpansion​(int order)
```

Return the maximum length of any expansion sequences that end
with the specified comparison order.

**Parameters:** order

- a collation order returned by previous or next.
**Returns:** the maximum length of any expansion sequences ending
with the specified order.
**Since:** 1.2

- setText

```java
public void setText​(
String
source)
```

Set a new string over which to iterate.

**Parameters:** source

- the new source text
**Since:** 1.2

- setText

```java
public void setText​(
CharacterIterator
source)
```

Set a new string over which to iterate.

**Parameters:** source

- the new source text.
**Since:** 1.2

---

#### Method Detail

reset

```java
public void reset()
```

Resets the cursor to the beginning of the string. The next call
to next() will return the first collation element in the string.

---

#### reset

public void reset()

Resets the cursor to the beginning of the string. The next call
to next() will return the first collation element in the string.

next

```java
public int next()
```

Get the next collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the next character in the
string".

This function returns the collation element that the iterator is currently
pointing to and then updates the internal pointer to point to the next element.
previous() updates the pointer first and then returns the element. This
means that when you change direction while iterating (i.e., call next() and
then call previous(), or call previous() and then call next()), you'll get
back the same element twice.

**Returns:** the next collation element

---

#### next

public int next()

Get the next collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the next character in the
string".

This function returns the collation element that the iterator is currently
pointing to and then updates the internal pointer to point to the next element.
previous() updates the pointer first and then returns the element. This
means that when you change direction while iterating (i.e., call next() and
then call previous(), or call previous() and then call next()), you'll get
back the same element twice.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the next character in the
string".

This function returns the collation element that the iterator is currently
pointing to and then updates the internal pointer to point to the next element.
previous() updates the pointer first and then returns the element. This
means that when you change direction while iterating (i.e., call next() and
then call previous(), or call previous() and then call next()), you'll get
back the same element twice.

previous

```java
public int previous()
```

Get the previous collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the previous character in the
string".

This function updates the iterator's internal pointer to point to the
collation element preceding the one it's currently pointing to and then
returns that element, while next() returns the current element and then
updates the pointer. This means that when you change direction while
iterating (i.e., call next() and then call previous(), or call previous()
and then call next()), you'll get back the same element twice.

**Returns:** the previous collation element
**Since:** 1.2

---

#### previous

public int previous()

Get the previous collation element in the string.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the previous character in the
string".

This function updates the iterator's internal pointer to point to the
collation element preceding the one it's currently pointing to and then
returns that element, while next() returns the current element and then
updates the pointer. This means that when you change direction while
iterating (i.e., call next() and then call previous(), or call previous()
and then call next()), you'll get back the same element twice.

This iterator iterates
over a sequence of collation elements that were built from the string.
Because there isn't necessarily a one-to-one mapping from characters to
collation elements, this doesn't mean the same thing as "return the
collation element [or ordering priority] of the previous character in the
string".

This function updates the iterator's internal pointer to point to the
collation element preceding the one it's currently pointing to and then
returns that element, while next() returns the current element and then
updates the pointer. This means that when you change direction while
iterating (i.e., call next() and then call previous(), or call previous()
and then call next()), you'll get back the same element twice.

primaryOrder

```java
public static final int primaryOrder​(int order)
```

Return the primary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's primary component

---

#### primaryOrder

public static final int primaryOrder​(int order)

Return the primary component of a collation element.

secondaryOrder

```java
public static final short secondaryOrder​(int order)
```

Return the secondary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's secondary component

---

#### secondaryOrder

public static final short secondaryOrder​(int order)

Return the secondary component of a collation element.

tertiaryOrder

```java
public static final short tertiaryOrder​(int order)
```

Return the tertiary component of a collation element.

**Parameters:** order

- the collation element
**Returns:** the element's tertiary component

---

#### tertiaryOrder

public static final short tertiaryOrder​(int order)

Return the tertiary component of a collation element.

setOffset

```java
public void setOffset​(int newOffset)
```

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements). The value returned by the next call to next()
will be the collation element corresponding to the specified position
in the text. If that position is in the middle of a contracting
character sequence, the result of the next call to next() is the
collation element for that sequence. This means that getOffset()
is not guaranteed to return the same value as was passed to a preceding
call to setOffset().

**Parameters:** newOffset

- The new character offset into the original text.
**Since:** 1.2

---

#### setOffset

public void setOffset​(int newOffset)

Sets the iterator to point to the collation element corresponding to
the specified character (the parameter is a CHARACTER offset in the
original string, not an offset into its corresponding sequence of
collation elements). The value returned by the next call to next()
will be the collation element corresponding to the specified position
in the text. If that position is in the middle of a contracting
character sequence, the result of the next call to next() is the
collation element for that sequence. This means that getOffset()
is not guaranteed to return the same value as was passed to a preceding
call to setOffset().

getOffset

```java
public int getOffset()
```

Returns the character offset in the original text corresponding to the next
collation element. (That is, getOffset() returns the position in the text
corresponding to the collation element that will be returned by the next
call to next().) This value will always be the index of the FIRST character
corresponding to the collation element (a contracting character sequence is
when two or more characters all correspond to the same collation element).
This means if you do setOffset(x) followed immediately by getOffset(), getOffset()
won't necessarily return x.

**Returns:** The character offset in the original text corresponding to the collation
element that will be returned by the next call to next().
**Since:** 1.2

---

#### getOffset

public int getOffset()

Returns the character offset in the original text corresponding to the next
collation element. (That is, getOffset() returns the position in the text
corresponding to the collation element that will be returned by the next
call to next().) This value will always be the index of the FIRST character
corresponding to the collation element (a contracting character sequence is
when two or more characters all correspond to the same collation element).
This means if you do setOffset(x) followed immediately by getOffset(), getOffset()
won't necessarily return x.

getMaxExpansion

```java
public int getMaxExpansion​(int order)
```

Return the maximum length of any expansion sequences that end
with the specified comparison order.

**Parameters:** order

- a collation order returned by previous or next.
**Returns:** the maximum length of any expansion sequences ending
with the specified order.
**Since:** 1.2

---

#### getMaxExpansion

public int getMaxExpansion​(int order)

Return the maximum length of any expansion sequences that end
with the specified comparison order.

setText

```java
public void setText​(
String
source)
```

Set a new string over which to iterate.

**Parameters:** source

- the new source text
**Since:** 1.2

---

#### setText

public void setText​(

String

source)

Set a new string over which to iterate.

setText

```java
public void setText​(
CharacterIterator
source)
```

Set a new string over which to iterate.

**Parameters:** source

- the new source text.
**Since:** 1.2

---

#### setText

public void setText​(

CharacterIterator

source)

Set a new string over which to iterate.

---

