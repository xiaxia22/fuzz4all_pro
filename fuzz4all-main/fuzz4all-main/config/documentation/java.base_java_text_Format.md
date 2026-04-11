# Class Format

**Source:** `java.base\java\text\Format.html`

### Class Description

```java
public abstract class
Format

extends
Object

implements
Serializable
,
Cloneable
```

Format

is an abstract base class for formatting locale-sensitive
information such as dates, messages, and numbers.

Format

defines the programming interface for formatting
locale-sensitive objects into

String

s (the

format

method) and for parsing

String

s back
into objects (the

parseObject

method).

Generally, a format's

parseObject

method must be able to parse
any string formatted by its

format

method. However, there may
be exceptional cases where this is not possible. For example, a

format

method might create two adjacent integer numbers with
no separator in between, and in this case the

parseObject

could
not tell which digits belong to which number.

Subclassing

The Java Platform provides three specialized subclasses of

Format

--

DateFormat

,

MessageFormat

, and

NumberFormat

--for formatting dates, messages, and numbers,
respectively.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Format()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public final
String
format​(
Object
obj)

Formats an object to produce a string. This is equivalent to

format

(obj,
new StringBuffer(), new FieldPosition(0)).toString();

**Parameters:**
- obj

- The object to format

**Returns:**
- Formatted string.

**Throws:**
- IllegalArgumentException

- if the Format cannot format the given
object

---

#### public abstract
StringBuffer
format​(
Object
obj,

StringBuffer
toAppendTo,

FieldPosition
pos)

Formats an object and appends the resulting text to a given string
buffer.
If the

pos

argument identifies a field used by the format,
then its indices are set to the beginning and end of the first such
field encountered.

**Parameters:**
- obj

- The object to format
- toAppendTo

- where the text is to be appended
- pos

- A

FieldPosition

identifying a field
in the formatted text

**Returns:**
- the string buffer passed in as

toAppendTo

,
with formatted text appended

**Throws:**
- NullPointerException

- if

toAppendTo

or

pos

is null
- IllegalArgumentException

- if the Format cannot format the given
object

---

#### public
AttributedCharacterIterator
formatToCharacterIterator​(
Object
obj)

Formats an Object producing an

AttributedCharacterIterator

.
You can use the returned

AttributedCharacterIterator

to build the resulting String, as well as to determine information
about the resulting String.

Each attribute key of the AttributedCharacterIterator will be of type

Field

. It is up to each

Format

implementation
to define what the legal values are for each attribute in the

AttributedCharacterIterator

, but typically the attribute
key is also used as the attribute value.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

**Parameters:**
- obj

- The object to format

**Returns:**
- AttributedCharacterIterator describing the formatted value.

**Throws:**
- NullPointerException

- if obj is null.
- IllegalArgumentException

- when the Format cannot format the
given object.

**Since:**
- 1.4

---

#### public abstract
Object
parseObject​(
String
source,

ParsePosition
pos)

Parses text from a string to produce an object.

The method attempts to parse text starting at the index given by

pos

.
If parsing succeeds, then the index of

pos

is updated
to the index after the last character used (parsing does not necessarily
use all characters up to the end of the string), and the parsed
object is returned. The updated

pos

can be used to
indicate the starting point for the next call to this method.
If an error occurs, then the index of

pos

is not
changed, the error index of

pos

is set to the index of
the character where the error occurred, and null is returned.

**Parameters:**
- source

- A

String

, part of which should be parsed.
- pos

- A

ParsePosition

object with index and error
index information as described above.

**Returns:**
- An

Object

parsed from the string. In case of
error, returns null.

**Throws:**
- NullPointerException

- if

source

or

pos

is null.

---

#### public
Object
parseObject​(
String
source)
throws
ParseException

Parses text from the beginning of the given string to produce an object.
The method may not use the entire text of the given string.

**Parameters:**
- source

- A

String

whose beginning should be parsed.

**Returns:**
- An

Object

parsed from the string.

**Throws:**
- ParseException

- if the beginning of the specified string
cannot be parsed.
- NullPointerException

- if

source

is null.

---

#### public
Object
clone()

Creates and returns a copy of this object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Format

java.lang.Object

- java.text.Format

java.text.Format

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** DateFormat

,

MessageFormat

,

NumberFormat

```java
public abstract class
Format

extends
Object

implements
Serializable
,
Cloneable
```

Format

is an abstract base class for formatting locale-sensitive
information such as dates, messages, and numbers.

Format

defines the programming interface for formatting
locale-sensitive objects into

String

s (the

format

method) and for parsing

String

s back
into objects (the

parseObject

method).

Generally, a format's

parseObject

method must be able to parse
any string formatted by its

format

method. However, there may
be exceptional cases where this is not possible. For example, a

format

method might create two adjacent integer numbers with
no separator in between, and in this case the

parseObject

could
not tell which digits belong to which number.

Subclassing

The Java Platform provides three specialized subclasses of

Format

--

DateFormat

,

MessageFormat

, and

NumberFormat

--for formatting dates, messages, and numbers,
respectively.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

**Since:** 1.1
**See Also:** ParsePosition

,

FieldPosition

,

NumberFormat

,

DateFormat

,

MessageFormat

,

Serialized Form

public abstract class

Format

extends

Object

implements

Serializable

,

Cloneable

Format

is an abstract base class for formatting locale-sensitive
information such as dates, messages, and numbers.

Format

defines the programming interface for formatting
locale-sensitive objects into

String

s (the

format

method) and for parsing

String

s back
into objects (the

parseObject

method).

Generally, a format's

parseObject

method must be able to parse
any string formatted by its

format

method. However, there may
be exceptional cases where this is not possible. For example, a

format

method might create two adjacent integer numbers with
no separator in between, and in this case the

parseObject

could
not tell which digits belong to which number.

Subclassing

The Java Platform provides three specialized subclasses of

Format

--

DateFormat

,

MessageFormat

, and

NumberFormat

--for formatting dates, messages, and numbers,
respectively.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

Format

defines the programming interface for formatting
locale-sensitive objects into

String

s (the

format

method) and for parsing

String

s back
into objects (the

parseObject

method).

Generally, a format's

parseObject

method must be able to parse
any string formatted by its

format

method. However, there may
be exceptional cases where this is not possible. For example, a

format

method might create two adjacent integer numbers with
no separator in between, and in this case the

parseObject

could
not tell which digits belong to which number.

Subclassing

The Java Platform provides three specialized subclasses of

Format

--

DateFormat

,

MessageFormat

, and

NumberFormat

--for formatting dates, messages, and numbers,
respectively.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

Generally, a format's

parseObject

method must be able to parse
any string formatted by its

format

method. However, there may
be exceptional cases where this is not possible. For example, a

format

method might create two adjacent integer numbers with
no separator in between, and in this case the

parseObject

could
not tell which digits belong to which number.

Subclassing

The Java Platform provides three specialized subclasses of

Format

--

DateFormat

,

MessageFormat

, and

NumberFormat

--for formatting dates, messages, and numbers,
respectively.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

---

#### Subclassing

The Java Platform provides three specialized subclasses of

Format

--

DateFormat

,

MessageFormat

, and

NumberFormat

--for formatting dates, messages, and numbers,
respectively.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

Concrete subclasses must implement three methods:

- format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

These general methods allow polymorphic parsing and formatting of objects
and are used, for example, by

MessageFormat

.
Subclasses often also provide additional

format

methods for
specific input types as well as

parse

methods for specific
result types. Any

parse

method that does not take a

ParsePosition

argument should throw

ParseException

when no text in the required format is at the beginning of the input text.

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

format(Object obj, StringBuffer toAppendTo, FieldPosition pos)

formatToCharacterIterator(Object obj)

parseObject(String source, ParsePosition pos)

Most subclasses will also implement the following factory methods:

- getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

In addition, some subclasses may also implement other

getXxxxInstance

methods for more specialized control. For
example, the

NumberFormat

class provides

getPercentInstance

and

getCurrencyInstance

methods for getting specialized number formatters.

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

getInstance

for getting a useful format object appropriate
for the current locale

getInstance(Locale)

for getting a useful format
object appropriate for the specified locale

Subclasses of

Format

that allow programmers to create objects
for locales (with

getInstance(Locale)

for example)
must also implement the following class method:

```java
public static Locale[] getAvailableLocales()
```

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

public static Locale[] getAvailableLocales()

And finally subclasses may define a set of constants to identify the various
fields in the formatted output. These constants are used to create a FieldPosition
object which identifies what information is contained in the field and its
position in the formatted result. These constants should be named

item

_FIELD

where

item

identifies
the field. For examples of these constants, see

ERA_FIELD

and its
friends in

DateFormat

.

Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

---

#### Synchronization

Formats are generally not synchronized.
It is recommended to create separate format instances for each thread.
If multiple threads access a format concurrently, it must be synchronized
externally.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Format.Field

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

Format.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Format

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates and returns a copy of this object.

String

format

​(

Object

obj)

Formats an object to produce a string.

abstract

StringBuffer

format

​(

Object

obj,

StringBuffer

toAppendTo,

FieldPosition

pos)

Formats an object and appends the resulting text to a given string
buffer.

AttributedCharacterIterator

formatToCharacterIterator

​(

Object

obj)

Formats an Object producing an

AttributedCharacterIterator

.

Object

parseObject

​(

String

source)

Parses text from the beginning of the given string to produce an object.

abstract

Object

parseObject

​(

String

source,

ParsePosition

pos)

Parses text from a string to produce an object.

- Methods declared in class java.lang.

Object

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Format.Field

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

Format.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

---

#### Nested Class Summary

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

Format.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Format

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates and returns a copy of this object.

String

format

​(

Object

obj)

Formats an object to produce a string.

abstract

StringBuffer

format

​(

Object

obj,

StringBuffer

toAppendTo,

FieldPosition

pos)

Formats an object and appends the resulting text to a given string
buffer.

AttributedCharacterIterator

formatToCharacterIterator

​(

Object

obj)

Formats an Object producing an

AttributedCharacterIterator

.

Object

parseObject

​(

String

source)

Parses text from the beginning of the given string to produce an object.

abstract

Object

parseObject

​(

String

source,

ParsePosition

pos)

Parses text from a string to produce an object.

- Methods declared in class java.lang.

Object

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

Creates and returns a copy of this object.

Formats an object to produce a string.

Formats an object and appends the resulting text to a given string
buffer.

Formats an Object producing an

AttributedCharacterIterator

.

Parses text from the beginning of the given string to produce an object.

Parses text from a string to produce an object.

Methods declared in class java.lang.

Object

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

- Format

```java
protected Format()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- format

```java
public final
String
format​(
Object
obj)
```

Formats an object to produce a string. This is equivalent to

format

(obj,
new StringBuffer(), new FieldPosition(0)).toString();

**Parameters:** obj

- The object to format
**Returns:** Formatted string.
**Throws:** IllegalArgumentException

- if the Format cannot format the given
object

- format

```java
public abstract
StringBuffer
format​(
Object
obj,

StringBuffer
toAppendTo,

FieldPosition
pos)
```

Formats an object and appends the resulting text to a given string
buffer.
If the

pos

argument identifies a field used by the format,
then its indices are set to the beginning and end of the first such
field encountered.

**Parameters:** obj

- The object to format
**Parameters:** toAppendTo

- where the text is to be appended
**Parameters:** pos

- A

FieldPosition

identifying a field
in the formatted text
**Returns:** the string buffer passed in as

toAppendTo

,
with formatted text appended
**Throws:** NullPointerException

- if

toAppendTo

or

pos

is null
**Throws:** IllegalArgumentException

- if the Format cannot format the given
object

- formatToCharacterIterator

```java
public
AttributedCharacterIterator
formatToCharacterIterator​(
Object
obj)
```

Formats an Object producing an

AttributedCharacterIterator

.
You can use the returned

AttributedCharacterIterator

to build the resulting String, as well as to determine information
about the resulting String.

Each attribute key of the AttributedCharacterIterator will be of type

Field

. It is up to each

Format

implementation
to define what the legal values are for each attribute in the

AttributedCharacterIterator

, but typically the attribute
key is also used as the attribute value.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

**Parameters:** obj

- The object to format
**Returns:** AttributedCharacterIterator describing the formatted value.
**Throws:** NullPointerException

- if obj is null.
**Throws:** IllegalArgumentException

- when the Format cannot format the
given object.
**Since:** 1.4

- parseObject

```java
public abstract
Object
parseObject​(
String
source,

ParsePosition
pos)
```

Parses text from a string to produce an object.

The method attempts to parse text starting at the index given by

pos

.
If parsing succeeds, then the index of

pos

is updated
to the index after the last character used (parsing does not necessarily
use all characters up to the end of the string), and the parsed
object is returned. The updated

pos

can be used to
indicate the starting point for the next call to this method.
If an error occurs, then the index of

pos

is not
changed, the error index of

pos

is set to the index of
the character where the error occurred, and null is returned.

**Parameters:** source

- A

String

, part of which should be parsed.
**Parameters:** pos

- A

ParsePosition

object with index and error
index information as described above.
**Returns:** An

Object

parsed from the string. In case of
error, returns null.
**Throws:** NullPointerException

- if

source

or

pos

is null.

- parseObject

```java
public
Object
parseObject​(
String
source)
throws
ParseException
```

Parses text from the beginning of the given string to produce an object.
The method may not use the entire text of the given string.

**Parameters:** source

- A

String

whose beginning should be parsed.
**Returns:** An

Object

parsed from the string.
**Throws:** ParseException

- if the beginning of the specified string
cannot be parsed.
**Throws:** NullPointerException

- if

source

is null.

- clone

```java
public
Object
clone()
```

Creates and returns a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

Constructor Detail

- Format

```java
protected Format()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

Format

```java
protected Format()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Format

protected Format()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- format

```java
public final
String
format​(
Object
obj)
```

Formats an object to produce a string. This is equivalent to

format

(obj,
new StringBuffer(), new FieldPosition(0)).toString();

**Parameters:** obj

- The object to format
**Returns:** Formatted string.
**Throws:** IllegalArgumentException

- if the Format cannot format the given
object

- format

```java
public abstract
StringBuffer
format​(
Object
obj,

StringBuffer
toAppendTo,

FieldPosition
pos)
```

Formats an object and appends the resulting text to a given string
buffer.
If the

pos

argument identifies a field used by the format,
then its indices are set to the beginning and end of the first such
field encountered.

**Parameters:** obj

- The object to format
**Parameters:** toAppendTo

- where the text is to be appended
**Parameters:** pos

- A

FieldPosition

identifying a field
in the formatted text
**Returns:** the string buffer passed in as

toAppendTo

,
with formatted text appended
**Throws:** NullPointerException

- if

toAppendTo

or

pos

is null
**Throws:** IllegalArgumentException

- if the Format cannot format the given
object

- formatToCharacterIterator

```java
public
AttributedCharacterIterator
formatToCharacterIterator​(
Object
obj)
```

Formats an Object producing an

AttributedCharacterIterator

.
You can use the returned

AttributedCharacterIterator

to build the resulting String, as well as to determine information
about the resulting String.

Each attribute key of the AttributedCharacterIterator will be of type

Field

. It is up to each

Format

implementation
to define what the legal values are for each attribute in the

AttributedCharacterIterator

, but typically the attribute
key is also used as the attribute value.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

**Parameters:** obj

- The object to format
**Returns:** AttributedCharacterIterator describing the formatted value.
**Throws:** NullPointerException

- if obj is null.
**Throws:** IllegalArgumentException

- when the Format cannot format the
given object.
**Since:** 1.4

- parseObject

```java
public abstract
Object
parseObject​(
String
source,

ParsePosition
pos)
```

Parses text from a string to produce an object.

The method attempts to parse text starting at the index given by

pos

.
If parsing succeeds, then the index of

pos

is updated
to the index after the last character used (parsing does not necessarily
use all characters up to the end of the string), and the parsed
object is returned. The updated

pos

can be used to
indicate the starting point for the next call to this method.
If an error occurs, then the index of

pos

is not
changed, the error index of

pos

is set to the index of
the character where the error occurred, and null is returned.

**Parameters:** source

- A

String

, part of which should be parsed.
**Parameters:** pos

- A

ParsePosition

object with index and error
index information as described above.
**Returns:** An

Object

parsed from the string. In case of
error, returns null.
**Throws:** NullPointerException

- if

source

or

pos

is null.

- parseObject

```java
public
Object
parseObject​(
String
source)
throws
ParseException
```

Parses text from the beginning of the given string to produce an object.
The method may not use the entire text of the given string.

**Parameters:** source

- A

String

whose beginning should be parsed.
**Returns:** An

Object

parsed from the string.
**Throws:** ParseException

- if the beginning of the specified string
cannot be parsed.
**Throws:** NullPointerException

- if

source

is null.

- clone

```java
public
Object
clone()
```

Creates and returns a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### Method Detail

format

```java
public final
String
format​(
Object
obj)
```

Formats an object to produce a string. This is equivalent to

format

(obj,
new StringBuffer(), new FieldPosition(0)).toString();

**Parameters:** obj

- The object to format
**Returns:** Formatted string.
**Throws:** IllegalArgumentException

- if the Format cannot format the given
object

---

#### format

public final

String

format​(

Object

obj)

Formats an object to produce a string. This is equivalent to

format

(obj,
new StringBuffer(), new FieldPosition(0)).toString();

format

```java
public abstract
StringBuffer
format​(
Object
obj,

StringBuffer
toAppendTo,

FieldPosition
pos)
```

Formats an object and appends the resulting text to a given string
buffer.
If the

pos

argument identifies a field used by the format,
then its indices are set to the beginning and end of the first such
field encountered.

**Parameters:** obj

- The object to format
**Parameters:** toAppendTo

- where the text is to be appended
**Parameters:** pos

- A

FieldPosition

identifying a field
in the formatted text
**Returns:** the string buffer passed in as

toAppendTo

,
with formatted text appended
**Throws:** NullPointerException

- if

toAppendTo

or

pos

is null
**Throws:** IllegalArgumentException

- if the Format cannot format the given
object

---

#### format

public abstract

StringBuffer

format​(

Object

obj,

StringBuffer

toAppendTo,

FieldPosition

pos)

Formats an object and appends the resulting text to a given string
buffer.
If the

pos

argument identifies a field used by the format,
then its indices are set to the beginning and end of the first such
field encountered.

formatToCharacterIterator

```java
public
AttributedCharacterIterator
formatToCharacterIterator​(
Object
obj)
```

Formats an Object producing an

AttributedCharacterIterator

.
You can use the returned

AttributedCharacterIterator

to build the resulting String, as well as to determine information
about the resulting String.

Each attribute key of the AttributedCharacterIterator will be of type

Field

. It is up to each

Format

implementation
to define what the legal values are for each attribute in the

AttributedCharacterIterator

, but typically the attribute
key is also used as the attribute value.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

**Parameters:** obj

- The object to format
**Returns:** AttributedCharacterIterator describing the formatted value.
**Throws:** NullPointerException

- if obj is null.
**Throws:** IllegalArgumentException

- when the Format cannot format the
given object.
**Since:** 1.4

---

#### formatToCharacterIterator

public

AttributedCharacterIterator

formatToCharacterIterator​(

Object

obj)

Formats an Object producing an

AttributedCharacterIterator

.
You can use the returned

AttributedCharacterIterator

to build the resulting String, as well as to determine information
about the resulting String.

Each attribute key of the AttributedCharacterIterator will be of type

Field

. It is up to each

Format

implementation
to define what the legal values are for each attribute in the

AttributedCharacterIterator

, but typically the attribute
key is also used as the attribute value.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

Each attribute key of the AttributedCharacterIterator will be of type

Field

. It is up to each

Format

implementation
to define what the legal values are for each attribute in the

AttributedCharacterIterator

, but typically the attribute
key is also used as the attribute value.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

The default implementation creates an

AttributedCharacterIterator

with no attributes. Subclasses
that support fields should override this and create an

AttributedCharacterIterator

with meaningful attributes.

parseObject

```java
public abstract
Object
parseObject​(
String
source,

ParsePosition
pos)
```

Parses text from a string to produce an object.

The method attempts to parse text starting at the index given by

pos

.
If parsing succeeds, then the index of

pos

is updated
to the index after the last character used (parsing does not necessarily
use all characters up to the end of the string), and the parsed
object is returned. The updated

pos

can be used to
indicate the starting point for the next call to this method.
If an error occurs, then the index of

pos

is not
changed, the error index of

pos

is set to the index of
the character where the error occurred, and null is returned.

**Parameters:** source

- A

String

, part of which should be parsed.
**Parameters:** pos

- A

ParsePosition

object with index and error
index information as described above.
**Returns:** An

Object

parsed from the string. In case of
error, returns null.
**Throws:** NullPointerException

- if

source

or

pos

is null.

---

#### parseObject

public abstract

Object

parseObject​(

String

source,

ParsePosition

pos)

Parses text from a string to produce an object.

The method attempts to parse text starting at the index given by

pos

.
If parsing succeeds, then the index of

pos

is updated
to the index after the last character used (parsing does not necessarily
use all characters up to the end of the string), and the parsed
object is returned. The updated

pos

can be used to
indicate the starting point for the next call to this method.
If an error occurs, then the index of

pos

is not
changed, the error index of

pos

is set to the index of
the character where the error occurred, and null is returned.

The method attempts to parse text starting at the index given by

pos

.
If parsing succeeds, then the index of

pos

is updated
to the index after the last character used (parsing does not necessarily
use all characters up to the end of the string), and the parsed
object is returned. The updated

pos

can be used to
indicate the starting point for the next call to this method.
If an error occurs, then the index of

pos

is not
changed, the error index of

pos

is set to the index of
the character where the error occurred, and null is returned.

parseObject

```java
public
Object
parseObject​(
String
source)
throws
ParseException
```

Parses text from the beginning of the given string to produce an object.
The method may not use the entire text of the given string.

**Parameters:** source

- A

String

whose beginning should be parsed.
**Returns:** An

Object

parsed from the string.
**Throws:** ParseException

- if the beginning of the specified string
cannot be parsed.
**Throws:** NullPointerException

- if

source

is null.

---

#### parseObject

public

Object

parseObject​(

String

source)
throws

ParseException

Parses text from the beginning of the given string to produce an object.
The method may not use the entire text of the given string.

clone

```java
public
Object
clone()
```

Creates and returns a copy of this object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates and returns a copy of this object.

---

