# Class StringJoiner

**Source:** `java.base\java\util\StringJoiner.html`

### Class Description

```java
public final class
StringJoiner

extends
Object
```

StringJoiner

is used to construct a sequence of characters separated
by a delimiter and optionally starting with a supplied prefix
and ending with a supplied suffix.

Prior to adding something to the

StringJoiner

, its

sj.toString()

method will, by default, return

prefix + suffix

.
However, if the

setEmptyValue

method is called, the

emptyValue

supplied will be returned instead. This can be used, for example, when
creating a string using set notation to indicate an empty set, i.e.

"{}"

, where the

prefix

is

"{"

, the

suffix

is

"}"

and nothing has been added to the

StringJoiner

.

**API Note:** The String

"[George:Sally:Fred]"

may be constructed as follows:

```java
StringJoiner sj = new StringJoiner(":", "[", "]");
sj.add("George").add("Sally").add("Fred");
String desiredString = sj.toString();
```

A

StringJoiner

may be employed to create formatted output from a

Stream

using

Collectors.joining(CharSequence)

. For example:

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
String commaSeparatedNumbers = numbers.stream()
.map(i -> i.toString())
.collect(Collectors.joining(", "));
```
**Since:** 1.8
**See Also:** Collectors.joining(CharSequence)

,

Collectors.joining(CharSequence, CharSequence, CharSequence)

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringJoiner​(
CharSequence
delimiter)

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.
If no characters are added to the

StringJoiner

and methods
accessing the value of it are invoked, it will not return a

prefix

or

suffix

(or properties thereof) in the result,
unless

setEmptyValue

has first been called.

**Parameters:**
- delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner

value

**Throws:**
- NullPointerException

- if

delimiter

is

null

---

#### public StringJoiner​(
CharSequence
delimiter,

CharSequence
prefix,

CharSequence
suffix)

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.
If no characters are added to the

StringJoiner

and methods
accessing the string value of it are invoked, it will return the

prefix + suffix

(or properties thereof) in the result, unless

setEmptyValue

has first been called.

**Parameters:**
- delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner
- prefix

- the sequence of characters to be used at the beginning
- suffix

- the sequence of characters to be used at the end

**Throws:**
- NullPointerException

- if

prefix

,

delimiter

, or

suffix

is

null

---

### Method Details

#### public
StringJoiner
setEmptyValue​(
CharSequence
emptyValue)

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty. A copy of the

emptyValue

parameter is made for this purpose. Note that once an add method has been
called, the

StringJoiner

is no longer considered empty, even if
the element(s) added correspond to the empty

String

.

**Parameters:**
- emptyValue

- the characters to return as the value of an empty

StringJoiner

**Returns:**
- this

StringJoiner

itself so the calls may be chained

**Throws:**
- NullPointerException

- when the

emptyValue

parameter is

null

---

#### public
String
toString()

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of this

StringJoiner

---

#### public
StringJoiner
add​(
CharSequence
newElement)

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value. If

newElement

is

null

, then

"null"

is added.

**Parameters:**
- newElement

- The element to add

**Returns:**
- a reference to this

StringJoiner

---

#### public
StringJoiner
merge​(
StringJoiner
other)

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty. If the given

StringJoiner

is empty, the call has no effect.

A

StringJoiner

is empty if

add()

has never been called, and if

merge()

has never been called
with a non-empty

StringJoiner

argument.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

**Parameters:**
- other

- The

StringJoiner

whose contents should be merged
into this one

**Returns:**
- This

StringJoiner

**Throws:**
- NullPointerException

- if the other

StringJoiner

is null

---

#### public int length()

Returns the length of the

String

representation
of this

StringJoiner

. Note that if
no add methods have been called, then the length of the

String

representation (either

prefix + suffix

or

emptyValue

)
will be returned. The value should be equivalent to

toString().length()

.

**Returns:**
- the length of the current value of

StringJoiner

---

### Additional Sections

#### Class StringJoiner

java.lang.Object

- java.util.StringJoiner

java.util.StringJoiner

```java
public final class
StringJoiner

extends
Object
```

StringJoiner

is used to construct a sequence of characters separated
by a delimiter and optionally starting with a supplied prefix
and ending with a supplied suffix.

Prior to adding something to the

StringJoiner

, its

sj.toString()

method will, by default, return

prefix + suffix

.
However, if the

setEmptyValue

method is called, the

emptyValue

supplied will be returned instead. This can be used, for example, when
creating a string using set notation to indicate an empty set, i.e.

"{}"

, where the

prefix

is

"{"

, the

suffix

is

"}"

and nothing has been added to the

StringJoiner

.

**API Note:** The String

"[George:Sally:Fred]"

may be constructed as follows:

```java
StringJoiner sj = new StringJoiner(":", "[", "]");
sj.add("George").add("Sally").add("Fred");
String desiredString = sj.toString();
```

A

StringJoiner

may be employed to create formatted output from a

Stream

using

Collectors.joining(CharSequence)

. For example:

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
String commaSeparatedNumbers = numbers.stream()
.map(i -> i.toString())
.collect(Collectors.joining(", "));
```
**Since:** 1.8
**See Also:** Collectors.joining(CharSequence)

,

Collectors.joining(CharSequence, CharSequence, CharSequence)

public final class

StringJoiner

extends

Object

StringJoiner

is used to construct a sequence of characters separated
by a delimiter and optionally starting with a supplied prefix
and ending with a supplied suffix.

Prior to adding something to the

StringJoiner

, its

sj.toString()

method will, by default, return

prefix + suffix

.
However, if the

setEmptyValue

method is called, the

emptyValue

supplied will be returned instead. This can be used, for example, when
creating a string using set notation to indicate an empty set, i.e.

"{}"

, where the

prefix

is

"{"

, the

suffix

is

"}"

and nothing has been added to the

StringJoiner

.

Prior to adding something to the

StringJoiner

, its

sj.toString()

method will, by default, return

prefix + suffix

.
However, if the

setEmptyValue

method is called, the

emptyValue

supplied will be returned instead. This can be used, for example, when
creating a string using set notation to indicate an empty set, i.e.

"{}"

, where the

prefix

is

"{"

, the

suffix

is

"}"

and nothing has been added to the

StringJoiner

.

The String

"[George:Sally:Fred]"

may be constructed as follows:

```java
StringJoiner sj = new StringJoiner(":", "[", "]");
sj.add("George").add("Sally").add("Fred");
String desiredString = sj.toString();
```

A

StringJoiner

may be employed to create formatted output from a

Stream

using

Collectors.joining(CharSequence)

. For example:

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
String commaSeparatedNumbers = numbers.stream()
.map(i -> i.toString())
.collect(Collectors.joining(", "));
```

StringJoiner sj = new StringJoiner(":", "[", "]");
sj.add("George").add("Sally").add("Fred");
String desiredString = sj.toString();

A

StringJoiner

may be employed to create formatted output from a

Stream

using

Collectors.joining(CharSequence)

. For example:

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
String commaSeparatedNumbers = numbers.stream()
.map(i -> i.toString())
.collect(Collectors.joining(", "));
```

List<Integer> numbers = Arrays.asList(1, 2, 3, 4);
String commaSeparatedNumbers = numbers.stream()
.map(i -> i.toString())
.collect(Collectors.joining(", "));

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringJoiner

​(

CharSequence

delimiter)

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.

StringJoiner

​(

CharSequence

delimiter,

CharSequence

prefix,

CharSequence

suffix)

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

StringJoiner

add

​(

CharSequence

newElement)

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value.

int

length

()

Returns the length of the

String

representation
of this

StringJoiner

.

StringJoiner

merge

​(

StringJoiner

other)

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty.

StringJoiner

setEmptyValue

​(

CharSequence

emptyValue)

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty.

String

toString

()

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

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

Constructor Summary

Constructors

Constructor

Description

StringJoiner

​(

CharSequence

delimiter)

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.

StringJoiner

​(

CharSequence

delimiter,

CharSequence

prefix,

CharSequence

suffix)

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.

---

#### Constructor Summary

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

StringJoiner

add

​(

CharSequence

newElement)

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value.

int

length

()

Returns the length of the

String

representation
of this

StringJoiner

.

StringJoiner

merge

​(

StringJoiner

other)

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty.

StringJoiner

setEmptyValue

​(

CharSequence

emptyValue)

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty.

String

toString

()

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

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

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value.

Returns the length of the

String

representation
of this

StringJoiner

.

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty.

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty.

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StringJoiner

```java
public StringJoiner​(
CharSequence
delimiter)
```

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.
If no characters are added to the

StringJoiner

and methods
accessing the value of it are invoked, it will not return a

prefix

or

suffix

(or properties thereof) in the result,
unless

setEmptyValue

has first been called.

**Parameters:** delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner

value
**Throws:** NullPointerException

- if

delimiter

is

null

- StringJoiner

```java
public StringJoiner​(
CharSequence
delimiter,

CharSequence
prefix,

CharSequence
suffix)
```

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.
If no characters are added to the

StringJoiner

and methods
accessing the string value of it are invoked, it will return the

prefix + suffix

(or properties thereof) in the result, unless

setEmptyValue

has first been called.

**Parameters:** delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner
**Parameters:** prefix

- the sequence of characters to be used at the beginning
**Parameters:** suffix

- the sequence of characters to be used at the end
**Throws:** NullPointerException

- if

prefix

,

delimiter

, or

suffix

is

null

============ METHOD DETAIL ==========

- Method Detail

- setEmptyValue

```java
public
StringJoiner
setEmptyValue​(
CharSequence
emptyValue)
```

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty. A copy of the

emptyValue

parameter is made for this purpose. Note that once an add method has been
called, the

StringJoiner

is no longer considered empty, even if
the element(s) added correspond to the empty

String

.

**Parameters:** emptyValue

- the characters to return as the value of an empty

StringJoiner
**Returns:** this

StringJoiner

itself so the calls may be chained
**Throws:** NullPointerException

- when the

emptyValue

parameter is

null

- toString

```java
public
String
toString()
```

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this

StringJoiner

- add

```java
public
StringJoiner
add​(
CharSequence
newElement)
```

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value. If

newElement

is

null

, then

"null"

is added.

**Parameters:** newElement

- The element to add
**Returns:** a reference to this

StringJoiner

- merge

```java
public
StringJoiner
merge​(
StringJoiner
other)
```

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty. If the given

StringJoiner

is empty, the call has no effect.

A

StringJoiner

is empty if

add()

has never been called, and if

merge()

has never been called
with a non-empty

StringJoiner

argument.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

**Parameters:** other

- The

StringJoiner

whose contents should be merged
into this one
**Returns:** This

StringJoiner
**Throws:** NullPointerException

- if the other

StringJoiner

is null

- length

```java
public int length()
```

Returns the length of the

String

representation
of this

StringJoiner

. Note that if
no add methods have been called, then the length of the

String

representation (either

prefix + suffix

or

emptyValue

)
will be returned. The value should be equivalent to

toString().length()

.

**Returns:** the length of the current value of

StringJoiner

Constructor Detail

- StringJoiner

```java
public StringJoiner​(
CharSequence
delimiter)
```

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.
If no characters are added to the

StringJoiner

and methods
accessing the value of it are invoked, it will not return a

prefix

or

suffix

(or properties thereof) in the result,
unless

setEmptyValue

has first been called.

**Parameters:** delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner

value
**Throws:** NullPointerException

- if

delimiter

is

null

- StringJoiner

```java
public StringJoiner​(
CharSequence
delimiter,

CharSequence
prefix,

CharSequence
suffix)
```

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.
If no characters are added to the

StringJoiner

and methods
accessing the string value of it are invoked, it will return the

prefix + suffix

(or properties thereof) in the result, unless

setEmptyValue

has first been called.

**Parameters:** delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner
**Parameters:** prefix

- the sequence of characters to be used at the beginning
**Parameters:** suffix

- the sequence of characters to be used at the end
**Throws:** NullPointerException

- if

prefix

,

delimiter

, or

suffix

is

null

---

#### Constructor Detail

StringJoiner

```java
public StringJoiner​(
CharSequence
delimiter)
```

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.
If no characters are added to the

StringJoiner

and methods
accessing the value of it are invoked, it will not return a

prefix

or

suffix

(or properties thereof) in the result,
unless

setEmptyValue

has first been called.

**Parameters:** delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner

value
**Throws:** NullPointerException

- if

delimiter

is

null

---

#### StringJoiner

public StringJoiner​(

CharSequence

delimiter)

Constructs a

StringJoiner

with no characters in it, with no

prefix

or

suffix

, and a copy of the supplied

delimiter

.
If no characters are added to the

StringJoiner

and methods
accessing the value of it are invoked, it will not return a

prefix

or

suffix

(or properties thereof) in the result,
unless

setEmptyValue

has first been called.

StringJoiner

```java
public StringJoiner​(
CharSequence
delimiter,

CharSequence
prefix,

CharSequence
suffix)
```

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.
If no characters are added to the

StringJoiner

and methods
accessing the string value of it are invoked, it will return the

prefix + suffix

(or properties thereof) in the result, unless

setEmptyValue

has first been called.

**Parameters:** delimiter

- the sequence of characters to be used between each
element added to the

StringJoiner
**Parameters:** prefix

- the sequence of characters to be used at the beginning
**Parameters:** suffix

- the sequence of characters to be used at the end
**Throws:** NullPointerException

- if

prefix

,

delimiter

, or

suffix

is

null

---

#### StringJoiner

public StringJoiner​(

CharSequence

delimiter,

CharSequence

prefix,

CharSequence

suffix)

Constructs a

StringJoiner

with no characters in it using copies
of the supplied

prefix

,

delimiter

and

suffix

.
If no characters are added to the

StringJoiner

and methods
accessing the string value of it are invoked, it will return the

prefix + suffix

(or properties thereof) in the result, unless

setEmptyValue

has first been called.

Method Detail

- setEmptyValue

```java
public
StringJoiner
setEmptyValue​(
CharSequence
emptyValue)
```

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty. A copy of the

emptyValue

parameter is made for this purpose. Note that once an add method has been
called, the

StringJoiner

is no longer considered empty, even if
the element(s) added correspond to the empty

String

.

**Parameters:** emptyValue

- the characters to return as the value of an empty

StringJoiner
**Returns:** this

StringJoiner

itself so the calls may be chained
**Throws:** NullPointerException

- when the

emptyValue

parameter is

null

- toString

```java
public
String
toString()
```

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this

StringJoiner

- add

```java
public
StringJoiner
add​(
CharSequence
newElement)
```

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value. If

newElement

is

null

, then

"null"

is added.

**Parameters:** newElement

- The element to add
**Returns:** a reference to this

StringJoiner

- merge

```java
public
StringJoiner
merge​(
StringJoiner
other)
```

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty. If the given

StringJoiner

is empty, the call has no effect.

A

StringJoiner

is empty if

add()

has never been called, and if

merge()

has never been called
with a non-empty

StringJoiner

argument.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

**Parameters:** other

- The

StringJoiner

whose contents should be merged
into this one
**Returns:** This

StringJoiner
**Throws:** NullPointerException

- if the other

StringJoiner

is null

- length

```java
public int length()
```

Returns the length of the

String

representation
of this

StringJoiner

. Note that if
no add methods have been called, then the length of the

String

representation (either

prefix + suffix

or

emptyValue

)
will be returned. The value should be equivalent to

toString().length()

.

**Returns:** the length of the current value of

StringJoiner

---

#### Method Detail

setEmptyValue

```java
public
StringJoiner
setEmptyValue​(
CharSequence
emptyValue)
```

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty. A copy of the

emptyValue

parameter is made for this purpose. Note that once an add method has been
called, the

StringJoiner

is no longer considered empty, even if
the element(s) added correspond to the empty

String

.

**Parameters:** emptyValue

- the characters to return as the value of an empty

StringJoiner
**Returns:** this

StringJoiner

itself so the calls may be chained
**Throws:** NullPointerException

- when the

emptyValue

parameter is

null

---

#### setEmptyValue

public

StringJoiner

setEmptyValue​(

CharSequence

emptyValue)

Sets the sequence of characters to be used when determining the string
representation of this

StringJoiner

and no elements have been
added yet, that is, when it is empty. A copy of the

emptyValue

parameter is made for this purpose. Note that once an add method has been
called, the

StringJoiner

is no longer considered empty, even if
the element(s) added correspond to the empty

String

.

toString

```java
public
String
toString()
```

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this

StringJoiner

---

#### toString

public

String

toString()

Returns the current value, consisting of the

prefix

, the values
added so far separated by the

delimiter

, and the

suffix

,
unless no elements have been added in which case, the

prefix + suffix

or the

emptyValue

characters are returned.

add

```java
public
StringJoiner
add​(
CharSequence
newElement)
```

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value. If

newElement

is

null

, then

"null"

is added.

**Parameters:** newElement

- The element to add
**Returns:** a reference to this

StringJoiner

---

#### add

public

StringJoiner

add​(

CharSequence

newElement)

Adds a copy of the given

CharSequence

value as the next
element of the

StringJoiner

value. If

newElement

is

null

, then

"null"

is added.

merge

```java
public
StringJoiner
merge​(
StringJoiner
other)
```

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty. If the given

StringJoiner

is empty, the call has no effect.

A

StringJoiner

is empty if

add()

has never been called, and if

merge()

has never been called
with a non-empty

StringJoiner

argument.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

**Parameters:** other

- The

StringJoiner

whose contents should be merged
into this one
**Returns:** This

StringJoiner
**Throws:** NullPointerException

- if the other

StringJoiner

is null

---

#### merge

public

StringJoiner

merge​(

StringJoiner

other)

Adds the contents of the given

StringJoiner

without prefix and
suffix as the next element if it is non-empty. If the given

StringJoiner

is empty, the call has no effect.

A

StringJoiner

is empty if

add()

has never been called, and if

merge()

has never been called
with a non-empty

StringJoiner

argument.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

A

StringJoiner

is empty if

add()

has never been called, and if

merge()

has never been called
with a non-empty

StringJoiner

argument.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

If the other

StringJoiner

is using a different delimiter,
then elements from the other

StringJoiner

are concatenated with
that delimiter and the result is appended to this

StringJoiner

as a single element.

length

```java
public int length()
```

Returns the length of the

String

representation
of this

StringJoiner

. Note that if
no add methods have been called, then the length of the

String

representation (either

prefix + suffix

or

emptyValue

)
will be returned. The value should be equivalent to

toString().length()

.

**Returns:** the length of the current value of

StringJoiner

---

#### length

public int length()

Returns the length of the

String

representation
of this

StringJoiner

. Note that if
no add methods have been called, then the length of the

String

representation (either

prefix + suffix

or

emptyValue

)
will be returned. The value should be equivalent to

toString().length()

.

---

