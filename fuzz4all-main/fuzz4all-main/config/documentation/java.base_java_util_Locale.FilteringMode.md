# Enum Locale.FilteringMode

**Source:** `java.base\java\util\Locale.FilteringMode.html`

### Class Description

```java
public static enum
Locale.FilteringMode

extends
Enum
<
Locale.FilteringMode
>
```

This enum provides constants to select a filtering mode for locale
matching. Refer to

RFC 4647
Matching of Language Tags

for details.

As an example, think of two Language Priority Lists each of which
includes only one language range and a set of following language tags:

```java
de (German)
de-DE (German, Germany)
de-Deva (German, in Devanagari script)
de-Deva-DE (German, in Devanagari script, Germany)
de-DE-1996 (German, Germany, orthography of 1996)
de-Latn-DE (German, in Latin script, Germany)
de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)
```

The filtering method will behave as follows:

Filtering method behavior

Filtering Mode

Language Priority List:

"de-DE"

Language Priority List:

"de-*-DE"

AUTOSELECT_FILTERING

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

EXTENDED_FILTERING

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

Same as above.

IGNORE_EXTENDED_RANGES

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

basic

filtering and returns

null

because
nothing matches.

MAP_EXTENDED_RANGES

Same as above.

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

because

"de-*-DE"

is mapped to

"de-DE"

.

REJECT_EXTENDED_RANGES

Same as above.

Throws

IllegalArgumentException

because

"de-*-DE"

is
not a valid basic language range.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Locale.FilteringMode

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Locale.FilteringMode
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.FilteringMode c : Locale.FilteringMode.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Locale.FilteringMode
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

#### Enum Locale.FilteringMode

java.lang.Object

- java.lang.Enum

<

Locale.FilteringMode

>
- - java.util.Locale.FilteringMode

java.lang.Enum

<

Locale.FilteringMode

>

- java.util.Locale.FilteringMode

java.util.Locale.FilteringMode

**All Implemented Interfaces:** Serializable

,

Comparable

<

Locale.FilteringMode

>

**Enclosing class:** Locale

```java
public static enum
Locale.FilteringMode

extends
Enum
<
Locale.FilteringMode
>
```

This enum provides constants to select a filtering mode for locale
matching. Refer to

RFC 4647
Matching of Language Tags

for details.

As an example, think of two Language Priority Lists each of which
includes only one language range and a set of following language tags:

```java
de (German)
de-DE (German, Germany)
de-Deva (German, in Devanagari script)
de-Deva-DE (German, in Devanagari script, Germany)
de-DE-1996 (German, Germany, orthography of 1996)
de-Latn-DE (German, in Latin script, Germany)
de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)
```

The filtering method will behave as follows:

Filtering method behavior

Filtering Mode

Language Priority List:

"de-DE"

Language Priority List:

"de-*-DE"

AUTOSELECT_FILTERING

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

EXTENDED_FILTERING

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

Same as above.

IGNORE_EXTENDED_RANGES

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

basic

filtering and returns

null

because
nothing matches.

MAP_EXTENDED_RANGES

Same as above.

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

because

"de-*-DE"

is mapped to

"de-DE"

.

REJECT_EXTENDED_RANGES

Same as above.

Throws

IllegalArgumentException

because

"de-*-DE"

is
not a valid basic language range.

**Since:** 1.8
**See Also:** Locale.filter(List, Collection, FilteringMode)

,

Locale.filterTags(List, Collection, FilteringMode)

public static enum

Locale.FilteringMode

extends

Enum

<

Locale.FilteringMode

>

This enum provides constants to select a filtering mode for locale
matching. Refer to

RFC 4647
Matching of Language Tags

for details.

As an example, think of two Language Priority Lists each of which
includes only one language range and a set of following language tags:

```java
de (German)
de-DE (German, Germany)
de-Deva (German, in Devanagari script)
de-Deva-DE (German, in Devanagari script, Germany)
de-DE-1996 (German, Germany, orthography of 1996)
de-Latn-DE (German, in Latin script, Germany)
de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)
```

The filtering method will behave as follows:

Filtering method behavior

Filtering Mode

Language Priority List:

"de-DE"

Language Priority List:

"de-*-DE"

AUTOSELECT_FILTERING

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

EXTENDED_FILTERING

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

Same as above.

IGNORE_EXTENDED_RANGES

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

basic

filtering and returns

null

because
nothing matches.

MAP_EXTENDED_RANGES

Same as above.

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

because

"de-*-DE"

is mapped to

"de-DE"

.

REJECT_EXTENDED_RANGES

Same as above.

Throws

IllegalArgumentException

because

"de-*-DE"

is
not a valid basic language range.

As an example, think of two Language Priority Lists each of which
includes only one language range and a set of following language tags:

```java
de (German)
de-DE (German, Germany)
de-Deva (German, in Devanagari script)
de-Deva-DE (German, in Devanagari script, Germany)
de-DE-1996 (German, Germany, orthography of 1996)
de-Latn-DE (German, in Latin script, Germany)
de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)
```

The filtering method will behave as follows:

Filtering method behavior

Filtering Mode

Language Priority List:

"de-DE"

Language Priority List:

"de-*-DE"

AUTOSELECT_FILTERING

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

EXTENDED_FILTERING

Performs

extended

filtering and returns

"de-DE"

,

"de-Deva-DE"

,

"de-DE-1996"

,

"de-Latn-DE"

, and

"de-Latn-DE-1996"

.

Same as above.

IGNORE_EXTENDED_RANGES

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

.

Performs

basic

filtering and returns

null

because
nothing matches.

MAP_EXTENDED_RANGES

Same as above.

Performs

basic

filtering and returns

"de-DE"

and

"de-DE-1996"

because

"de-*-DE"

is mapped to

"de-DE"

.

REJECT_EXTENDED_RANGES

Same as above.

Throws

IllegalArgumentException

because

"de-*-DE"

is
not a valid basic language range.

de (German)
de-DE (German, Germany)
de-Deva (German, in Devanagari script)
de-Deva-DE (German, in Devanagari script, Germany)
de-DE-1996 (German, Germany, orthography of 1996)
de-Latn-DE (German, in Latin script, Germany)
de-Latn-DE-1996 (German, in Latin script, Germany, orthography of 1996)

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

AUTOSELECT_FILTERING

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges.

EXTENDED_FILTERING

Specifies extended filtering.

IGNORE_EXTENDED_RANGES

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

MAP_EXTENDED_RANGES

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range.

REJECT_EXTENDED_RANGES

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Locale.FilteringMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Locale.FilteringMode

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

AUTOSELECT_FILTERING

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges.

EXTENDED_FILTERING

Specifies extended filtering.

IGNORE_EXTENDED_RANGES

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

MAP_EXTENDED_RANGES

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range.

REJECT_EXTENDED_RANGES

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

---

#### Enum Constant Summary

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges.

Specifies extended filtering.

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range.

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Locale.FilteringMode

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Locale.FilteringMode

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

- AUTOSELECT_FILTERING

```java
public static final
Locale.FilteringMode
AUTOSELECT_FILTERING
```

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges. If all of the ranges
are basic, basic filtering is selected. Otherwise, extended
filtering is selected.

- EXTENDED_FILTERING

```java
public static final
Locale.FilteringMode
EXTENDED_FILTERING
```

Specifies extended filtering.

- IGNORE_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
IGNORE_EXTENDED_RANGES
```

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

- MAP_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
MAP_EXTENDED_RANGES
```

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range. Specifically, a language range starting with a
subtag

"*"

is treated as a language range

"*"

. For
example,

"*-US"

is treated as

"*"

. If

"*"

is
not the first subtag,

"*"

and extra

"-"

are removed.
For example,

"ja-*-JP"

is mapped to

"ja-JP"

.

- REJECT_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
REJECT_EXTENDED_RANGES
```

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Locale.FilteringMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.FilteringMode c : Locale.FilteringMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Locale.FilteringMode
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

- AUTOSELECT_FILTERING

```java
public static final
Locale.FilteringMode
AUTOSELECT_FILTERING
```

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges. If all of the ranges
are basic, basic filtering is selected. Otherwise, extended
filtering is selected.

- EXTENDED_FILTERING

```java
public static final
Locale.FilteringMode
EXTENDED_FILTERING
```

Specifies extended filtering.

- IGNORE_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
IGNORE_EXTENDED_RANGES
```

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

- MAP_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
MAP_EXTENDED_RANGES
```

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range. Specifically, a language range starting with a
subtag

"*"

is treated as a language range

"*"

. For
example,

"*-US"

is treated as

"*"

. If

"*"

is
not the first subtag,

"*"

and extra

"-"

are removed.
For example,

"ja-*-JP"

is mapped to

"ja-JP"

.

- REJECT_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
REJECT_EXTENDED_RANGES
```

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

---

#### Enum Constant Detail

AUTOSELECT_FILTERING

```java
public static final
Locale.FilteringMode
AUTOSELECT_FILTERING
```

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges. If all of the ranges
are basic, basic filtering is selected. Otherwise, extended
filtering is selected.

---

#### AUTOSELECT_FILTERING

public static final

Locale.FilteringMode

AUTOSELECT_FILTERING

Specifies automatic filtering mode based on the given Language
Priority List consisting of language ranges. If all of the ranges
are basic, basic filtering is selected. Otherwise, extended
filtering is selected.

EXTENDED_FILTERING

```java
public static final
Locale.FilteringMode
EXTENDED_FILTERING
```

Specifies extended filtering.

---

#### EXTENDED_FILTERING

public static final

Locale.FilteringMode

EXTENDED_FILTERING

Specifies extended filtering.

IGNORE_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
IGNORE_EXTENDED_RANGES
```

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

---

#### IGNORE_EXTENDED_RANGES

public static final

Locale.FilteringMode

IGNORE_EXTENDED_RANGES

Specifies basic filtering: Note that any extended language ranges
included in the given Language Priority List are ignored.

MAP_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
MAP_EXTENDED_RANGES
```

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range. Specifically, a language range starting with a
subtag

"*"

is treated as a language range

"*"

. For
example,

"*-US"

is treated as

"*"

. If

"*"

is
not the first subtag,

"*"

and extra

"-"

are removed.
For example,

"ja-*-JP"

is mapped to

"ja-JP"

.

---

#### MAP_EXTENDED_RANGES

public static final

Locale.FilteringMode

MAP_EXTENDED_RANGES

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, they are mapped to the
basic language range. Specifically, a language range starting with a
subtag

"*"

is treated as a language range

"*"

. For
example,

"*-US"

is treated as

"*"

. If

"*"

is
not the first subtag,

"*"

and extra

"-"

are removed.
For example,

"ja-*-JP"

is mapped to

"ja-JP"

.

REJECT_EXTENDED_RANGES

```java
public static final
Locale.FilteringMode
REJECT_EXTENDED_RANGES
```

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

---

#### REJECT_EXTENDED_RANGES

public static final

Locale.FilteringMode

REJECT_EXTENDED_RANGES

Specifies basic filtering: If any extended language ranges are
included in the given Language Priority List, the list is rejected
and the filtering method throws

IllegalArgumentException

.

Method Detail

- values

```java
public static
Locale.FilteringMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.FilteringMode c : Locale.FilteringMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Locale.FilteringMode
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
Locale.FilteringMode
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.FilteringMode c : Locale.FilteringMode.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Locale.FilteringMode

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Locale.FilteringMode c : Locale.FilteringMode.values())
System.out.println(c);
```

for (Locale.FilteringMode c : Locale.FilteringMode.values())
System.out.println(c);

valueOf

```java
public static
Locale.FilteringMode
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

Locale.FilteringMode

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

